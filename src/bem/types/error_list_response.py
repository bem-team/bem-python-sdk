# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .error_event import ErrorEvent

__all__ = ["ErrorListResponse"]


class ErrorListResponse(BaseModel):
    errors: List[ErrorEvent]
    """Array of terminal error events."""

    total_count: int = FieldInfo(alias="totalCount")
    """The total number of results available."""
