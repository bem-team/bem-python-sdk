# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["OutputListParams"]


class OutputListParams(TypedDict, total=False):
    call_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="callIDs")]
    """Filter to outputs from specific calls."""

    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]

    event_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="eventIDs")]
    """Filter to specific output events by their event IDs (KSUIDs)."""

    function_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionIDs")]

    function_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionNames")]

    function_version_nums: Annotated[Iterable[int], PropertyInfo(alias="functionVersionNums")]
    """Filter to specific function version numbers."""

    include_intermediate: Annotated[bool, PropertyInfo(alias="includeIntermediate")]
    """
    When `true`, includes intermediate events (those that spawned a downstream
    function call). Default: `false`.
    """

    is_labelled: Annotated[bool, PropertyInfo(alias="isLabelled")]
    """
    If `true`, only outputs with a corrected (labelled) payload. If `false`, only
    outputs that are not labelled. If omitted, no filter is applied.
    """

    is_regression: Annotated[bool, PropertyInfo(alias="isRegression")]
    """If `true`, only regression-marked outputs.

    If `false`, only non-regression outputs. If omitted, no filter is applied.

    Note: clients migrating from `/v1-beta/transformations` should pass
    `isRegression=false` explicitly to preserve the legacy default (regressions
    hidden unless explicitly requested).
    """

    limit: int

    reference_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="referenceIDs")]

    reference_id_substring: Annotated[str, PropertyInfo(alias="referenceIDSubstring")]
    """Case-insensitive substring match against `referenceID`."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]

    transformation_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="transformationIDs")]
    """Filter by legacy transformation IDs.

    Provided for backwards compatibility with clients migrating from
    `/v1-beta/transformations`.
    """

    workflow_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowIDs")]

    workflow_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowNames")]
