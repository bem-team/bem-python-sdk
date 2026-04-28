# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ResultFetchResultsResponse", "Failed", "Pending"]


class Failed(BaseModel):
    """A transformation whose evaluation failed or was not found."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Server timestamp associated with the failure."""

    error_message: str = FieldInfo(alias="errorMessage")
    """Human-readable failure reason."""

    transformation_id: str = FieldInfo(alias="transformationId")


class Pending(BaseModel):
    """A transformation whose evaluation is still running."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Server timestamp when the evaluation was queued."""

    transformation_id: str = FieldInfo(alias="transformationId")


class ResultFetchResultsResponse(BaseModel):
    """
    Batched response containing the evaluation state for every requested
    transformation ID, partitioned into completed `results`, still-running
    `pending`, and terminal `failed` groups.
    """

    results: object
    """Completed evaluation results, keyed by transformation ID.

    A transformation appears here only if its evaluation completed successfully.
    Still-running evaluations appear in `pending`; failed evaluations appear in
    `failed`.
    """

    errors: Optional[object] = None
    """
    Reserved map of transformation ID to error message for validation failures on
    the request itself. Populated only in edge cases.
    """

    failed: Optional[List[Failed]] = None
    """Transformations whose evaluation failed or was not found."""

    pending: Optional[List[Pending]] = None
    """Transformations whose evaluation is still running."""
