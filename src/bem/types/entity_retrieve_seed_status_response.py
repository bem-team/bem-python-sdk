# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .seed_row_result import SeedRowResult

__all__ = ["EntityRetrieveSeedStatusResponse"]


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

    results: Optional[List[SeedRowResult]] = None
    """Per-row outcomes. Present only once `status` is `completed`."""
