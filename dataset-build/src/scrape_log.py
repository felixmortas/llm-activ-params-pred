"""
Append-only JSONL log of every model the scraper has already looked at
(kept as MoE or not, or failed to fetch), so re-running build_dataset.py
never re-checks the same model twice.

One line per model, e.g.:
    {"model_id": "mistralai/Mixtral-8x7B-v0.1", "likes": 4231,
     "is_moe": true, "status": "moe_confirmed", "checked_at": "..."}
"""
import json
import os
from datetime import datetime, timezone
from typing import Optional, Set


def load_checked_ids(log_path: str) -> Set[str]:
    """Read the log and return the set of model_ids already processed."""
    checked = set()
    if not os.path.exists(log_path):
        return checked
    with open(log_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                checked.add(rec["model_id"])
            except (json.JSONDecodeError, KeyError):
                continue  # skip corrupted lines rather than crash a long run
    return checked


def append_log(log_path: str, model_id: str, status: str, is_moe: bool, likes: Optional[int] = None) -> None:
    """
    Append one record to the log. `status` is a short machine-readable
    reason, e.g. "moe_confirmed", "not_moe", "no_config", "error".
    """
    os.makedirs(os.path.dirname(log_path) or ".", exist_ok=True)
    rec = {
        "model_id": model_id,
        "likes": likes,
        "is_moe": is_moe,
        "status": status,
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }
    with open(log_path, "a") as f:
        f.write(json.dumps(rec) + "\n")
