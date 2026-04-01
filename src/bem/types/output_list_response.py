# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .event import Event
from .._models import BaseModel

__all__ = ["OutputListResponse"]


class OutputListResponse(BaseModel):
    outputs: List[Event]
    """Array of terminal non-error output events.

    Each element is polymorphic by `eventType`. Intermediate events (those that
    spawned a downstream function call) are excluded by default; pass
    `includeIntermediate=true` to include them.
    """

    total_count: int = FieldInfo(alias="totalCount")
    """The total number of results available."""
