"""
Configuration for the HF activated-parameters dataset builder.
Tweak these values to control which models get scraped.
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class SearchConfig:
    # HF Hub filters. We target text-generation transformer checkpoints,
    # since our parameter formulas are written for decoder-only LLMs.
    pipeline_tags: List[str] = field(default_factory=lambda: ["text-generation"])

    # When True (default): walk the Hub's text-generation models strictly
    # ordered by number of likes (descending), check each one's config.json,
    # and only keep it if architectures.normalize_config().is_moe is True.
    # There is no keyword prefilter - every model in scope gets checked.
    moe_only: bool = True
    target_moe_count: int = 1000

    sort: str = "likes"
    direction: int = -1  # descending

    # Where results are written.
    output_csv: str = "data/hf_activated_params_dataset.csv"

    # Every model we check (kept or not) is appended here as one JSON line.
    # On restart, this file is read first so already-checked models are
    # never re-fetched - this is what makes the script resumable.
    log_path: str = "data/scrape_log.jsonl"

    # Seconds to sleep between API calls to stay well under rate limits.
    request_sleep_s: float = 0.05

    # Non-MoE-only mode: hard cap on how many models to scrape.
    max_models: int = 1500
    min_downloads: int = 50
    library: str = "transformers"
