# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionListParams"]


class CollectionListParams(TypedDict, total=False):
    collection_name_search: Annotated[str, PropertyInfo(alias="collectionNameSearch")]
    """
    Optional substring search filter for collection names (case-insensitive). For
    example, "premium" will match "customers.premium", "products.premium", etc.
    """

    limit: int
    """Number of collections per page"""

    page: int
    """Page number for pagination"""

    parent_collection_name: Annotated[str, PropertyInfo(alias="parentCollectionName")]
    """
    Optional filter to list only collections under a specific parent collection
    path. For example, "customers" will return "customers", "customers.premium",
    "customers.premium.vip", etc.
    """
