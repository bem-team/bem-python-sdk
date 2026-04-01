# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .error_event import ErrorEvent

__all__ = ["ErrorRetrieveResponse"]


class ErrorRetrieveResponse(BaseModel):
    error: ErrorEvent
    """The error event."""
