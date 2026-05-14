# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ViewListParams"]


class ViewListParams(TypedDict, total=False):
    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]
    """Cursor — a `viewID` defining your place in the list."""

    function_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionIDs")]
    """Return only views that read from at least one of the named functions."""

    function_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionNames")]
    """Return only views that read from at least one of the named functions."""

    limit: int

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Sort order over view IDs (default `asc`)."""

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]
    """Cursor — a `viewID` defining your place in the list."""

    view_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="viewIDs")]
    """Return only the specified view IDs."""

    view_name_substring: Annotated[str, PropertyInfo(alias="viewNameSubstring")]
    """Case-insensitive substring search over view names."""
