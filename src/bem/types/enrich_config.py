# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .enrich_step import EnrichStep

__all__ = ["EnrichConfig"]


class EnrichConfig(BaseModel):
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

    steps: List[EnrichStep]
    """Array of enrichment steps to execute sequentially"""
