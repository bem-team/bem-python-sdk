# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .enrich_step_param import EnrichStepParam

__all__ = ["EnrichConfigParam"]


class EnrichConfigParam(TypedDict, total=False):
    """Configuration for enrich function with semantic search steps.

    **How Enrich Functions Work:**

    Enrich functions use semantic search to augment JSON data with relevant information from collections.
    They take JSON input (typically from a transform function), extract specified fields, perform vector-based
    semantic search against collections, and inject the results back into the data.

    **Input Requirements:**
    - Must receive JSON input (typically uploaded to S3 from a previous function)
    - Can be chained after transform or other functions that produce JSON output

    **Example Use Cases:**
    - Match product descriptions to SKU codes from a product catalog
    - Enrich customer data with account information
    - Link order line items to inventory records

    **Configuration:**
    - Define one or more enrichment steps
    - Each step extracts values, searches a collection, and injects results
    - Steps are executed sequentially
    """

    steps: Required[Iterable[EnrichStepParam]]
    """Array of enrichment steps to execute sequentially"""
