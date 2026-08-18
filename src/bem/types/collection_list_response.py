# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CollectionListResponse"]


class CollectionListResponse(BaseModel):
    """Collection metadata without items"""

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

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the collection was last updated"""
