# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ItemAddParams", "Item"]


class ItemAddParams(TypedDict, total=False):
    collection_name: Required[Annotated[str, PropertyInfo(alias="collectionName")]]
    """The name/path of the collection.

    Must use only letters, digits, underscores, and dots. Each segment must start
    with a letter or underscore.
    """

    items: Required[Iterable[Item]]
    """Array of items to add (maximum 100 items per request)"""


class Item(TypedDict, total=False):
    """Data for creating a new item in a collection"""

    data: Required[Union[str, object]]
    """The data to be embedded and stored (string or JSON object)"""
