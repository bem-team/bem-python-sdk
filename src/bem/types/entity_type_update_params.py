# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EntityTypeUpdateParams"]


class EntityTypeUpdateParams(TypedDict, total=False):
    attribute_schema: Annotated[object, PropertyInfo(alias="attributeSchema")]
    """New per-type structured attribute metadata."""

    description: str
    """New description."""

    parent_type_id: Annotated[str, PropertyInfo(alias="parentTypeID")]
    """
    New parent type public ID (`ety_...`), or an empty string to clear the parent
    (promote to top-level). Must belong to the same account+environment and may not
    be the type itself.
    """
