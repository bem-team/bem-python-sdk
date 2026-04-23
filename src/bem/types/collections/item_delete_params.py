# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ItemDeleteParams"]


class ItemDeleteParams(TypedDict, total=False):
    collection_item_id: Required[Annotated[str, PropertyInfo(alias="collectionItemID")]]
    """The unique identifier of the item to delete"""

    collection_name: Required[Annotated[str, PropertyInfo(alias="collectionName")]]
    """The name/path of the collection.

    Must use only letters, digits, underscores, and dots. Each segment must start
    with a letter or underscore.
    """
