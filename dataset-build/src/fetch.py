"""
Talks to the HuggingFace Hub: walks models ordered by likes (via the stable
public REST API, see hub_rest.py), downloads their config.json, plus the
ground-truth total parameter count from safetensors metadata when the repo
exposes it (more reliable than our own formula).

NOTE: this module requires network access to huggingface.co.
"""
import inspect
import json
import time
import logging
from typing import Iterator, Optional, Dict, Any, Callable

from huggingface_hub import HfApi, hf_hub_download
from huggingface_hub.utils import HfHubHTTPError

from .config import SearchConfig
from .hub_rest import iter_models, SimpleModelInfo

logger = logging.getLogger(__name__)


def _supported_kwargs(func: Callable, candidate_kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """Keep only the kwargs that `func`'s current signature actually accepts.
    Used only for HfApi.model_info(), which is much more stable than
    list_models() but still worth guarding defensively."""
    try:
        sig = inspect.signature(func)
    except (TypeError, ValueError):
        return candidate_kwargs

    params = sig.parameters
    if any(p.kind == inspect.Parameter.VAR_KEYWORD for p in params.values()):
        return candidate_kwargs

    return {k: v for k, v in candidate_kwargs.items() if k in params}


def iter_models_by_likes(cfg: SearchConfig) -> Iterator[SimpleModelInfo]:
    """
    Yield every model matching cfg.pipeline_tags, ordered by number of
    likes descending, across all configured pipeline tags. No keyword
    prefilter: every model in scope is walked in turn, lazily paginated.
    """
    for tag in cfg.pipeline_tags:
        yield from iter_models(pipeline_tag=tag, sort=cfg.sort, direction=cfg.direction)


def fetch_raw_config(model_id: str) -> Optional[Dict[str, Any]]:
    """Download and parse config.json for a given model_id. None on failure."""
    try:
        path = hf_hub_download(repo_id=model_id, filename="config.json")
        with open(path, "r") as f:
            return json.load(f)
    except (HfHubHTTPError, FileNotFoundError, json.JSONDecodeError, OSError) as e:
        logger.debug("Skipping %s: %s", model_id, e)
        return None


def fetch_ground_truth_total_params(model_id: str) -> Optional[int]:
    """
    Try to read the real total parameter count from the repo's safetensors
    metadata (HF computes this from the actual weight files). Returns None
    if unavailable, in which case the caller should fall back to the
    analytical formula.
    """
    api = HfApi()
    candidate_kwargs = _supported_kwargs(api.model_info, {"files_metadata": False})
    try:
        info = api.model_info(model_id, **candidate_kwargs)
        safet = getattr(info, "safetensors", None)
        if safet and getattr(safet, "total", None):
            return int(safet.total)
    except (HfHubHTTPError, TypeError) as e:
        logger.debug("No model_info for %s: %s", model_id, e)
    return None


def iter_raw_records(cfg: SearchConfig):
    """
    Generic (non-MoE-only) collection loop, kept for cfg.moe_only = False:
    yields (model_id, raw_config_dict, ground_truth_total_params_or_None)
    for up to cfg.max_models models meeting cfg.min_downloads.
    """
    seen = set()
    count = 0
    for m in iter_models_by_likes(cfg):
        if count >= cfg.max_models:
            return
        if m.id in seen:
            continue
        if (m.downloads or 0) < cfg.min_downloads:
            continue
        seen.add(m.id)

        raw_config = fetch_raw_config(m.id)
        if raw_config is None:
            continue
        gt_total = fetch_ground_truth_total_params(m.id)
        time.sleep(cfg.request_sleep_s)
        count += 1
        yield m.id, raw_config, gt_total
