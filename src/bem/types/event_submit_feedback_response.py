# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EventSubmitFeedbackResponse"]


class EventSubmitFeedbackResponse(BaseModel):
    """Echoed response after a correction is recorded."""

    correction: object

    created_at: datetime = FieldInfo(alias="createdAt")
    """Server timestamp when the correction was persisted (RFC 3339)."""

    event_id: str = FieldInfo(alias="eventID")

    function_type: Literal["extract", "classify", "join"] = FieldInfo(alias="functionType")
    """Function types that support feedback submission."""
