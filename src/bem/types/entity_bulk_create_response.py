# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .seed_row_result import SeedRowResult

__all__ = ["EntityBulkCreateResponse", "Summary"]


class Summary(BaseModel):
    """Per-outcome tally across a batch."""

    created: int
    """Number of rows that created a new entity."""

    merged: int
    """Number of rows merged into an existing entity."""

    rejected: int
    """Number of rows rejected."""


class EntityBulkCreateResponse(BaseModel):
    """`200` response for a synchronously processed (small) batch."""

    results: List[SeedRowResult]
    """Per-row outcomes, in request order."""

    summary: Summary
    """Per-outcome tally across a batch."""
