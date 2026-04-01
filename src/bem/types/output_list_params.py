# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["OutputListParams"]


class OutputListParams(TypedDict, total=False):
    call_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="callIDs")]
    """Filter to outputs from specific calls."""

    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]

    function_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionIDs")]

    function_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionNames")]

    include_intermediate: Annotated[bool, PropertyInfo(alias="includeIntermediate")]
    """
    When `true`, includes intermediate events (those that spawned a downstream
    function call). Default: `false`.
    """

    limit: int

    reference_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="referenceIDs")]

    reference_id_substring: Annotated[str, PropertyInfo(alias="referenceIDSubstring")]
    """Case-insensitive substring match against `referenceID`."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]

    workflow_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowIDs")]

    workflow_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowNames")]
