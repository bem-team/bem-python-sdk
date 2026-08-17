# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WorkflowListParams"]


class WorkflowListParams(TypedDict, total=False):
    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]

    function_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionIDs")]

    function_id_version_nums: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionIDVersionNums")]
    """Return only workflows with a node pinned to a specific function version.

    Each entry is `<functionID>.<versionNum>` — for example
    `fn_2c9AXIj48cUYJtCuv1gsQtHGDzK.4`.
    """

    function_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionNames")]

    function_name_version_nums: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionNameVersionNums")]
    """
    Return only workflows with a node pinned to a specific function version, keyed
    by function name. Each entry is `<functionName>.<versionNum>` — for example
    `invoice-extract.4`.
    """

    limit: int

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]

    tags: SequenceNotStr[str]

    workflow_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowIDs")]

    workflow_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowNames")]
