"""
Orchestrates the full pipeline: walk Hub models ordered by likes, keep the
ones confirmed as Mixture-of-Experts, and write the resulting table to CSV.

Resumable by design: every model checked (kept or not) is appended to
cfg.log_path immediately, and every confirmed MoE row is appended to
cfg.output_csv immediately - so killing and re-running this script picks
up exactly where it left off, without re-checking anything.

Usage:
    python -m hf_param_dataset.build_dataset
"""
import csv
import logging
import os

from tqdm import tqdm

from .config import SearchConfig
from .fetch import iter_models_by_likes, iter_raw_records, fetch_raw_config, fetch_ground_truth_total_params
from .architectures import normalize_config, estimate_params
from .scrape_log import load_checked_ids, append_log

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def build_row(model_id: str, raw_config: dict, gt_total_params, likes=None) -> dict:
    """Turn a raw config.json + ground truth into one output row, or None if unparseable."""
    norm = normalize_config(raw_config)
    if norm is None:
        return None

    est = estimate_params(norm)

    # Prefer the ground-truth total param count (from actual weight files)
    # over our formula's estimate, when available. Re-derive the activation
    # ratio from our formula and apply it to the ground truth, so the label
    # stays consistent with the real model size.
    if gt_total_params:
        activated_params = int(gt_total_params * est.activation_ratio)
        total_params = gt_total_params
        total_source = "safetensors"
    else:
        activated_params = est.activated_params
        total_params = est.total_params
        total_source = "formula"

    row = norm.to_dict()
    row.update({
        "model_id": model_id,
        "likes": likes,
        "total_params": total_params,
        "activated_params": activated_params,
        "activation_ratio": activated_params / total_params if total_params else 1.0,
        "total_params_source": total_source,
    })
    return row


def _count_csv_rows(path: str) -> int:
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return 0
    with open(path, "r") as f:
        return max(sum(1 for _ in f) - 1, 0)  # minus header


def run_moe_only(cfg: SearchConfig) -> None:
    already_checked = load_checked_ids(cfg.log_path)
    logger.info("%d models already checked in a previous run - skipping those", len(already_checked))

    kept = _count_csv_rows(cfg.output_csv)
    logger.info("%d MoE models already confirmed from a previous run", kept)

    write_header = not os.path.exists(cfg.output_csv) or os.path.getsize(cfg.output_csv) == 0
    os.makedirs(os.path.dirname(cfg.output_csv) or ".", exist_ok=True)

    csv_file = open(cfg.output_csv, "a", newline="")
    csv_writer = None  # created lazily, once we know the row's field names

    pbar = tqdm(total=cfg.target_moe_count, initial=kept, desc="Confirmed MoE models")
    checked_this_run = 0

    try:
        for m in iter_models_by_likes(cfg):
            if kept >= cfg.target_moe_count:
                break
            if m.id in already_checked:
                continue

            likes = getattr(m, "likes", None)
            raw_config = fetch_raw_config(m.id)
            checked_this_run += 1

            if raw_config is None:
                append_log(cfg.log_path, m.id, status="no_config", is_moe=False, likes=likes)
                already_checked.add(m.id)
                continue

            norm = normalize_config(raw_config)
            if norm is None or not norm.is_moe:
                append_log(cfg.log_path, m.id, status="not_moe", is_moe=False, likes=likes)
                already_checked.add(m.id)
                continue

            gt_total = fetch_ground_truth_total_params(m.id)
            row = build_row(m.id, raw_config, gt_total, likes)
            if row is None:
                append_log(cfg.log_path, m.id, status="error_building_row", is_moe=True, likes=likes)
                already_checked.add(m.id)
                continue

            if csv_writer is None:
                csv_writer = csv.DictWriter(csv_file, fieldnames=list(row.keys()))
                if write_header:
                    csv_writer.writeheader()
            csv_writer.writerow(row)
            csv_file.flush()

            append_log(cfg.log_path, m.id, status="moe_confirmed", is_moe=True, likes=likes)
            already_checked.add(m.id)
            kept += 1
            pbar.update(1)

            if checked_this_run % 200 == 0:
                logger.info("Checked %d models this run, %d confirmed MoE so far", checked_this_run, kept)
    finally:
        csv_file.close()
        pbar.close()

    logger.info("Done. %d MoE models total in %s (checked %d new models this run)",
                kept, cfg.output_csv, checked_this_run)


def run_generic(cfg: SearchConfig) -> None:
    """Non-MoE-only mode: kept simple, no resumability (rarely needed here)."""
    import pandas as pd
    os.makedirs(os.path.dirname(cfg.output_csv) or ".", exist_ok=True)
    rows = []
    for model_id, raw_config, gt_total in tqdm(iter_raw_records(cfg), desc="Scraping models"):
        row = build_row(model_id, raw_config, gt_total)
        if row is not None:
            rows.append(row)
    pd.DataFrame(rows).to_csv(cfg.output_csv, index=False)
    logger.info("Done. %d rows written to %s", len(rows), cfg.output_csv)


def main():
    cfg = SearchConfig()
    if cfg.moe_only:
        run_moe_only(cfg)
    else:
        run_generic(cfg)


if __name__ == "__main__":
    main()
