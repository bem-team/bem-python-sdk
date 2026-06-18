# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EntityRetrieveSeedStatusResponse", "Result"]


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


class EntityRetrieveSeedStatusResponse(BaseModel):
    """`GET /v3/entities/seed/{id}` response."""

    created_count: int = FieldInfo(alias="createdCount")
    """Rows that created a new entity."""

    merged_count: int = FieldInfo(alias="mergedCount")
    """Rows merged into an existing entity."""

    rejected_count: int = FieldInfo(alias="rejectedCount")
    """Rows rejected."""

    seed_job_id: str = FieldInfo(alias="seedJobID")
    """Public ID (`esj_...`) of the seed job."""

    status: Literal["pending", "processing", "completed", "failed"]
    """Lifecycle state."""

    total_rows: int = FieldInfo(alias="totalRows")
    """Total rows in the submitted batch."""

    error: Optional[str] = None
    """Terminal error message when `status` is `failed`."""

    results: Optional[List[Result]] = None
    """Per-row outcomes. Present only once `status` is `completed`."""
