# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionDeleteParams"]


class CollectionDeleteParams(TypedDict, total=False):
    collection_name: Required[Annotated[str, PropertyInfo(alias="collectionName")]]
    """The name/path of the collection to delete.

    Must use only letters, digits, underscores, and dots. Each segment must start
    with a letter or underscore.
    """
