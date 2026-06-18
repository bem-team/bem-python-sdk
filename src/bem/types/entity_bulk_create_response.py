# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EntityBulkCreateResponse", "Result", "Summary"]


class Result(BaseModel):
    """The outcome of seeding one row."""

    canonical: str
    """The canonical name from the input row."""

    outcome: Literal["created", "merged-with", "rejected"]
    """
    What happened to this row: `created` (new entity), `merged-with` (matched an
    existing entity), or `rejected` (see `reason`).
    """

    entity_id: Optional[str] = FieldInfo(alias="entityID", default=None)
    """Public ID (`ent_...`) of the created or merged entity. Absent when rejected."""

    reason: Optional[str] = None
    """Human-readable explanation when `outcome` is `rejected`."""


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

    results: List[Result]
    """Per-row outcomes, in request order."""

    summary: Summary
    """Per-outcome tally across a batch."""
