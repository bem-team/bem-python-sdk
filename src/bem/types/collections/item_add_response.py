# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..collection_item import CollectionItem

__all__ = ["ItemAddResponse"]


class ItemAddResponse(BaseModel):
    """Response after queuing items for async processing"""

    event_id: str = FieldInfo(alias="eventID")
    """Event ID for tracking this operation.

    Use this to correlate with webhook notifications.
    """

    message: str
    """Status message"""

    status: Literal["pending"]
    """Processing status"""

    added_count: Optional[int] = FieldInfo(alias="addedCount", default=None)
    """Number of new items added (only present in synchronous mode, deprecated)"""

    items: Optional[List[CollectionItem]] = None
    """Array of items that were added (only present in synchronous mode, deprecated)"""
