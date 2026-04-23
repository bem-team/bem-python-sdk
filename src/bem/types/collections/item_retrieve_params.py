# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ItemRetrieveParams"]


class ItemRetrieveParams(TypedDict, total=False):
    collection_name: Required[Annotated[str, PropertyInfo(alias="collectionName")]]
    """The name/path of the collection.

    Must use only letters, digits, underscores, and dots. Each segment must start
    with a letter or underscore.
    """

    include_subcollections: Annotated[bool, PropertyInfo(alias="includeSubcollections")]
    """
    When true, includes items from all subcollections under the specified collection
    path. For example, querying "customers" with this flag will return items from
    "customers", "customers.premium", "customers.premium.vip", etc.
    """

    limit: int
    """Number of items per page"""

    page: int
    """Page number for pagination"""
