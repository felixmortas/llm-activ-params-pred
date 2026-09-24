"""
Minimal, dependency-light client for the public HuggingFace Hub REST API
(https://huggingface.co/api/models).

We talk to this endpoint directly with `requests` instead of going through
`HfApi.list_models()`, because that wrapper's accepted keyword arguments
(`sort`, `direction`, `library`...) have changed repeatedly across
huggingface_hub releases and kept breaking this script. The underlying
REST endpoint itself is stable, documented, and needs no authentication
for read access. Pagination follows the same GitHub-style `Link` header
convention that huggingface_hub itself uses internally, so we lean on
`requests`'s built-in `response.links` parsing rather than hand-rolling it.

Docs: https://huggingface.co/docs/hub/api
"""
import logging
import time
from dataclasses import dataclass
from typing import Iterator, Optional, Dict, Any

import requests

logger = logging.getLogger(__name__)

API_URL = "https://huggingface.co/api/models"


@dataclass
class SimpleModelInfo:
    """Just enough fields for our scraping loop; avoids depending on
    huggingface_hub's own (also-changing) ModelInfo dataclass shape."""
    id: str
    likes: Optional[int] = None
    downloads: Optional[int] = None


def _get(session: requests.Session, url: str, params: Optional[Dict[str, Any]], max_retries: int = 5) -> requests.Response:
    """GET with basic exponential backoff on transient errors / rate limiting."""
    delay = 1.0
    for attempt in range(max_retries):
        try:
            resp = session.get(url, params=params, timeout=30)
            if resp.status_code == 429 or resp.status_code >= 500:
                logger.warning("Hub API returned %d, retrying in %.1fs", resp.status_code, delay)
                time.sleep(delay)
                delay *= 2
                continue
            resp.raise_for_status()
            return resp
        except requests.exceptions.RequestException as e:
            logger.warning("Request failed (%s), retrying in %.1fs", e, delay)
            time.sleep(delay)
            delay *= 2
    raise RuntimeError(f"Giving up on {url} after {max_retries} retries")


def iter_models(
    pipeline_tag: Optional[str] = None,
    sort: str = "likes",
    direction: int = -1,
    page_size: int = 1000,
) -> Iterator[SimpleModelInfo]:
    """
    Yield models from the Hub, sorted by `sort`/`direction`, following
    pagination until exhausted. `page_size` only controls how many results
    come back per HTTP call; the generator itself has no upper bound - the
    caller decides when to stop (e.g. once enough MoE models are found).
    """
    params = {"sort": sort, "direction": direction, "limit": page_size}
    if pipeline_tag:
        params["pipeline_tag"] = pipeline_tag

    session = requests.Session()
    url = API_URL
    first_request = True

    while url:
        resp = _get(session, url, params if first_request else None)
        first_request = False

        page = resp.json()
        if not page:
            return

        for item in page:
            model_id = item.get("id") or item.get("modelId")
            if not model_id:
                continue
            yield SimpleModelInfo(
                id=model_id,
                likes=item.get("likes"),
                downloads=item.get("downloads"),
            )

        url = resp.links.get("next", {}).get("url")
