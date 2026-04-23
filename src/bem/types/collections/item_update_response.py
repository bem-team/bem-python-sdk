# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ItemUpdateResponse", "Item"]


class Item(BaseModel):
    """A single item in a collection"""

    collection_item_id: str = FieldInfo(alias="collectionItemID")
    """Unique identifier for the item"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the item was created"""

    data: Union[str, object]
    """The data stored in this item"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the item was last updated"""


class ItemUpdateResponse(BaseModel):
    """Response after queuing items for async update"""

    event_id: str = FieldInfo(alias="eventID")
    """Event ID for tracking this operation.

    Use this to correlate with webhook notifications.
    """

    message: str
    """Status message"""

    status: Literal["pending"]
    """Processing status"""

    items: Optional[List[Item]] = None
    """Array of items that were updated (only present in synchronous mode, deprecated)"""

    updated_count: Optional[int] = FieldInfo(alias="updatedCount", default=None)
    """Number of items updated (only present in synchronous mode, deprecated)"""
