# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .function_type import FunctionType

__all__ = ["FunctionGetMetricsParams"]


class FunctionGetMetricsParams(TypedDict, total=False):
    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Case-insensitive substring match on the function display name."""

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

    tags: SequenceNotStr[str]
    """Returns metrics for functions tagged with any of the supplied tags."""

    types: List[FunctionType]

    workflow_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowIDs")]
    """Returns metrics only for functions referenced by the named workflows."""

    workflow_id_version_nums: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowIDVersionNums")]
    """Narrow the workflow filter to a specific workflow version.

    Each entry is `<workflowID>.<versionNum>`.
    """

    workflow_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowNames")]
    """Returns metrics only for functions referenced by the named workflows."""

    workflow_name_version_nums: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowNameVersionNums")]
    """
    Narrow the workflow filter to a specific workflow version, keyed by workflow
    name. Each entry is `<workflowName>.<versionNum>`.
    """
