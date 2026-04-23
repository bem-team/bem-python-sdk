# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ItemUpdateParams", "Item"]


class ItemUpdateParams(TypedDict, total=False):
    collection_name: Required[Annotated[str, PropertyInfo(alias="collectionName")]]
    """The name/path of the collection.

    Must use only letters, digits, underscores, and dots. Each segment must start
    with a letter or underscore.
    """

    items: Required[Iterable[Item]]
    """Array of items to update (maximum 100 items per request)"""


class Item(TypedDict, total=False):
    """Data for updating an existing item in a collection"""

    collection_item_id: Required[Annotated[str, PropertyInfo(alias="collectionItemID")]]
    """Unique identifier for the item to update"""

    data: Required[Union[str, object]]
    """The updated data to be embedded and stored (string or JSON object)"""
