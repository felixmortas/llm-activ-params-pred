"""
Normalizes heterogeneous HuggingFace `config.json` files into a common
schema, and estimates total vs. activated parameter counts.

"Activated parameters" = the number of parameters actually used in a single
forward pass for one token. For dense models this equals total_params.
For Mixture-of-Experts (MoE) models, only `num_experts_per_tok` out of
`num_local_experts` are routed per token, so activated_params < total_params.

The formulas below are analytical approximations (they ignore norm layers,
biases, and rotary/absolute position embeddings, all negligible in size).
They were validated against known public figures, e.g. Mixtral-8x7B
(46.7B total / 12.9B active) - see tests/test_architectures.py.
"""
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any


def _first(raw: Dict[str, Any], *keys, default=None):
    """Return the first present, non-None key from a list of aliases."""
    for k in keys:
        if k in raw and raw[k] is not None:
            return raw[k]
    return default


@dataclass
class NormalizedConfig:
    model_type: str
    hidden_size: int
    num_hidden_layers: int
    num_attention_heads: int
    num_key_value_heads: int
    head_dim: int
    intermediate_size: int
    vocab_size: int
    tie_word_embeddings: bool

    # MoE-specific fields (0 / False when the model is dense)
    is_moe: bool
    num_local_experts: int
    num_experts_per_tok: int
    num_shared_experts: int
    moe_intermediate_size: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def normalize_config(raw: Dict[str, Any], model_type_hint: Optional[str] = None) -> Optional[NormalizedConfig]:
    """
    Map a raw HF config.json dict onto our common schema.
    Returns None if essential fields (hidden size, layer count) are missing,
    since we then cannot compute anything reliable.
    """
    model_type = raw.get("model_type", model_type_hint or "unknown")

    hidden_size = _first(raw, "hidden_size", "n_embd", "d_model", "dim", "hidden_dim")
    num_hidden_layers = _first(raw, "num_hidden_layers", "n_layer", "num_layers", "n_layers")
    if hidden_size is None or num_hidden_layers is None:
        return None

    num_attention_heads = _first(raw, "num_attention_heads", "n_head", "num_heads", default=1)
    num_key_value_heads = _first(raw, "num_key_value_heads", "num_kv_heads", default=num_attention_heads)
    head_dim = _first(raw, "head_dim", default=hidden_size // max(num_attention_heads, 1))

    intermediate_size = _first(
        raw, "intermediate_size", "n_inner", "ffn_dim", "ffn_hidden_size",
        default=4 * hidden_size,
    )
    vocab_size = _first(raw, "vocab_size", default=32000)
    tie_word_embeddings = bool(_first(raw, "tie_word_embeddings", default=False))

    # MoE aliases: naming is very inconsistent across model families
    # (Mixtral, Qwen2MoE, DeepSeek-V2/V3, DBRX, Jamba, OLMoE...).
    num_local_experts = _first(
        raw, "num_local_experts", "n_routed_experts", "num_experts",
        "ffn_num_experts", "n_experts", "moe_num_experts",
        default=0,
    )
    num_experts_per_tok = _first(
        raw, "num_experts_per_tok", "num_selected_experts", "moe_topk",
        "n_experts_per_token", "moe_top_k",
        default=0,
    )
    num_shared_experts = _first(
        raw, "n_shared_experts", "num_shared_experts", "moe_num_shared_experts",
        default=0,
    )
    moe_intermediate_size = _first(
        raw, "moe_intermediate_size", "expert_intermediate_size", "ffn_dim",
        default=intermediate_size,
    )

    is_moe = bool(num_local_experts) and bool(num_experts_per_tok)

    return NormalizedConfig(
        model_type=model_type,
        hidden_size=int(hidden_size),
        num_hidden_layers=int(num_hidden_layers),
        num_attention_heads=int(num_attention_heads),
        num_key_value_heads=int(num_key_value_heads),
        head_dim=int(head_dim),
        intermediate_size=int(intermediate_size),
        vocab_size=int(vocab_size),
        tie_word_embeddings=tie_word_embeddings,
        is_moe=is_moe,
        num_local_experts=int(num_local_experts or 0),
        num_experts_per_tok=int(num_experts_per_tok or 0),
        num_shared_experts=int(num_shared_experts or 0),
        moe_intermediate_size=int(moe_intermediate_size),
    )


def _attention_params(cfg: NormalizedConfig) -> int:
    """Q, K, V, O projection weights for one transformer block (GQA-aware)."""
    q = cfg.hidden_size * (cfg.num_attention_heads * cfg.head_dim)
    k = cfg.hidden_size * (cfg.num_key_value_heads * cfg.head_dim)
    v = cfg.hidden_size * (cfg.num_key_value_heads * cfg.head_dim)
    o = (cfg.num_attention_heads * cfg.head_dim) * cfg.hidden_size
    return q + k + v + o


def _gated_mlp_params(hidden_size: int, ffn_size: int) -> int:
    """SwiGLU-style MLP: gate + up + down projections (used by ~all modern LLMs)."""
    return 3 * hidden_size * ffn_size


@dataclass
class ParamEstimate:
    total_params: int
    activated_params: int
    activation_ratio: float  # activated / total, useful diagnostic feature


def estimate_params(cfg: NormalizedConfig) -> ParamEstimate:
    """
    Estimate total and activated parameter counts from a normalized config.
    """
    attn = _attention_params(cfg)

    if cfg.is_moe:
        expert_mlp = _gated_mlp_params(cfg.hidden_size, cfg.moe_intermediate_size)
        shared_mlp = cfg.num_shared_experts * expert_mlp
        router = cfg.num_local_experts * cfg.hidden_size  # gating linear layer

        total_layer = attn + cfg.num_local_experts * expert_mlp + shared_mlp + router
        active_layer = attn + cfg.num_experts_per_tok * expert_mlp + shared_mlp + router
    else:
        dense_mlp = _gated_mlp_params(cfg.hidden_size, cfg.intermediate_size)
        total_layer = attn + dense_mlp
        active_layer = total_layer  # dense: everything is always active

    total_from_layers = cfg.num_hidden_layers * total_layer
    active_from_layers = cfg.num_hidden_layers * active_layer

    embedding = cfg.vocab_size * cfg.hidden_size
    lm_head = 0 if cfg.tie_word_embeddings else cfg.vocab_size * cfg.hidden_size

    total_params = embedding + lm_head + total_from_layers
    activated_params = embedding + lm_head + active_from_layers

    ratio = activated_params / total_params if total_params else 1.0
    return ParamEstimate(total_params=total_params, activated_params=activated_params, activation_ratio=ratio)
