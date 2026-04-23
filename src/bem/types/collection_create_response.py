# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CollectionCreateResponse", "Item"]


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


class CollectionCreateResponse(BaseModel):
    """Collection details"""

    collection_id: str = FieldInfo(alias="collectionID")
    """Unique identifier for the collection"""

    collection_name: str = FieldInfo(alias="collectionName")
    """The collection name/path.

    Only letters, digits, underscores, and dots are allowed.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the collection was created"""

    item_count: int = FieldInfo(alias="itemCount")
    """Number of items in the collection"""

    items: Optional[List[Item]] = None
    """List of items in the collection (when fetching collection details)"""

    limit: Optional[int] = None
    """Number of items per page"""

    page: Optional[int] = None
    """Current page number"""

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
    """Total number of pages"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the collection was last updated"""
