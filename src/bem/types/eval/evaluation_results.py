# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EvaluationResults", "Failed", "Pending"]


class Failed(BaseModel):
    """An event whose evaluation failed or was not found."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Server timestamp associated with the failure."""

    error_message: str = FieldInfo(alias="errorMessage")
    """Human-readable failure reason."""

    event_id: str = FieldInfo(alias="eventID")
    """Event KSUID."""


class Pending(BaseModel):
    """An event whose evaluation is still running."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Server timestamp when the evaluation was queued."""

    event_id: str = FieldInfo(alias="eventID")
    """Event KSUID."""


class EvaluationResults(BaseModel):
    """
    Batched response containing the evaluation state for every requested
    ID, partitioned into completed `results`, still-running `pending`, and
    terminal `failed` groups. All identifiers in the response are event
    KSUIDs regardless of whether the request used `eventIDs` or
    `transformationIDs`.
    """

    results: object
    """Completed evaluation results, keyed by event KSUID.

    An event appears here only if its evaluation completed successfully.
    Still-running evaluations appear in `pending`; failed evaluations appear in
    `failed`.
    """

    errors: Optional[object] = None
    """
    Reserved map of event KSUID to error message for validation failures on the
    request itself. Populated only in edge cases.
    """

    failed: Optional[List[Failed]] = None
    """Events whose evaluation failed or was not found."""

    pending: Optional[List[Pending]] = None
    """Events whose evaluation is still running."""
