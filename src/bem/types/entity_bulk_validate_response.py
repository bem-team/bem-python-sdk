# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EntityBulkValidateResponse", "Result", "Summary"]


class Result(BaseModel):
    """The outcome of validating one row."""

    entity_id: str = FieldInfo(alias="entityID")
    """The `ent_...` ID from the request."""

    outcome: Literal["validated", "skipped", "rejected-row"]
    """
    `validated` (transition applied), `skipped` (not found or not authorized), or
    `rejected-row` (the transition itself was illegal, e.g. already terminal).
    """

    reason: Optional[str] = None
    """Explanation for a `skipped` or `rejected-row` outcome."""


class Summary(BaseModel):
    """Per-outcome tally across a bulk-validate batch."""

    rejected_row: int = FieldInfo(alias="rejectedRow")
    """Rows whose transition was illegal."""

    skipped: int
    """Rows skipped (not found / not authorized)."""

    validated: int
    """Rows whose transition was applied."""


class EntityBulkValidateResponse(BaseModel):
    """`200` response for `POST /v3/entities/bulk-validate`."""

    results: List[Result]
    """Per-row outcomes, in request order."""

    summary: Summary
    """Per-outcome tally across a bulk-validate batch."""
