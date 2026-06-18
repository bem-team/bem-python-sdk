# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EntityTypeCreateParams"]


class EntityTypeCreateParams(TypedDict, total=False):
    name: Required[str]
    """Type name. Required and unique within the account+environment."""

    attribute_schema: Annotated[object, PropertyInfo(alias="attributeSchema")]
    """Optional per-type structured attribute metadata."""

    description: str
    """Optional description."""

    parent_type_id: Annotated[str, PropertyInfo(alias="parentTypeID")]
    """Optional public ID (`ety_...`) of the parent type.

    Must belong to the same account+environment.
    """
