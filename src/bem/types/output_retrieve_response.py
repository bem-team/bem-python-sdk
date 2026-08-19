# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .event import Event
from .._models import BaseModel

__all__ = ["OutputRetrieveResponse"]


class OutputRetrieveResponse(BaseModel):
    output: Event
    """The output event. Polymorphic by `eventType`."""
