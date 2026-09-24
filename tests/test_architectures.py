"""
Sanity checks: run our formulas against real config.json fields for a few
well-known models, and compare against their publicly reported total /
active parameter counts. We allow ~10% tolerance since our formulas ignore
norm layers, biases, and some architecture-specific quirks (e.g. DeepSeek's
latent attention).
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from hf_param_dataset.architectures import normalize_config, estimate_params


def check(name, raw_config, expected_total_b, expected_active_b, tol=0.10):
    cfg = normalize_config(raw_config)
    assert cfg is not None, f"{name}: failed to normalize config"
    est = estimate_params(cfg)

    total_b = est.total_params / 1e9
    active_b = est.activated_params / 1e9

    total_err = abs(total_b - expected_total_b) / expected_total_b
    active_err = abs(active_b - expected_active_b) / expected_active_b

    print(f"{name}: total={total_b:.2f}B (expected {expected_total_b}B, err {total_err:.1%}) | "
          f"active={active_b:.2f}B (expected {expected_active_b}B, err {active_err:.1%})")

    assert total_err < tol, f"{name}: total params off by {total_err:.1%}"
    assert active_err < tol, f"{name}: active params off by {active_err:.1%}"


def test_mixtral_8x7b():
    # config.json fields for mistralai/Mixtral-8x7B-v0.1
    raw = {
        "model_type": "mixtral",
        "hidden_size": 4096,
        "num_hidden_layers": 32,
        "num_attention_heads": 32,
        "num_key_value_heads": 8,
        "intermediate_size": 14336,
        "vocab_size": 32000,
        "num_local_experts": 8,
        "num_experts_per_tok": 2,
        "tie_word_embeddings": False,
    }
    # Publicly reported: 46.7B total, 12.9B active
    check("Mixtral-8x7B", raw, 46.7, 12.9)


def test_dense_llama_7b():
    # config.json fields for meta-llama/Llama-2-7b (dense model: active == total)
    raw = {
        "model_type": "llama",
        "hidden_size": 4096,
        "num_hidden_layers": 32,
        "num_attention_heads": 32,
        "num_key_value_heads": 32,
        "intermediate_size": 11008,
        "vocab_size": 32000,
        "tie_word_embeddings": False,
    }
    # Publicly reported: ~6.7B
    check("Llama-2-7B", raw, 6.7, 6.7)


if __name__ == "__main__":
    test_mixtral_8x7b()
    test_dense_llama_7b()
    print("All formula validation tests passed.")
