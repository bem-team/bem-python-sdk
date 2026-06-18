# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EntityTypeListParams"]


class EntityTypeListParams(TypedDict, total=False):
    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]
    """Cursor: return types whose `typeID` sorts before this value."""

    limit: int
    """Maximum number of entity types to return (default 50, max 200)."""

    parent_type_id: Annotated[str, PropertyInfo(alias="parentTypeId")]
    """Filter to the direct children of this parent type (`ety_...`)."""

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]
    """Cursor: return types whose `typeID` sorts after this value."""
