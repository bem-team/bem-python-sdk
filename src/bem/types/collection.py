# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .collection_item import CollectionItem

__all__ = ["Collection"]


class Collection(BaseModel):
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

    items: Optional[List[CollectionItem]] = None
    """List of items in the collection (when fetching collection details)"""

    limit: Optional[int] = None
    """Number of items per page"""

    page: Optional[int] = None
    """Current page number"""

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
    """Total number of pages"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the collection was last updated"""
