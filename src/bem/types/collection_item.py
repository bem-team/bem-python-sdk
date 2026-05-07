# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CollectionItem"]


class CollectionItem(BaseModel):
    """A single item in a collection"""

    collection_item_id: str = FieldInfo(alias="collectionItemID")
    """Unique identifier for the item"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the item was created"""

    data: Union[str, object]
    """The data stored in this item"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the item was last updated"""
