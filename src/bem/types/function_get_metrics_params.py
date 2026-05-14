# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .function_type import FunctionType

__all__ = ["FunctionGetMetricsParams"]


class FunctionGetMetricsParams(TypedDict, total=False):
    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]
    """Cursor — a `functionID` defining your place in the list."""

    function_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionIDs")]

    function_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionNames")]

    limit: int

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Sort direction over the result set (default `asc`).

    Pagination works symmetrically in both directions via `startingAfter` /
    `endingBefore`.
    """

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]
    """Cursor — a `functionID` defining your place in the list."""

    types: List[FunctionType]
