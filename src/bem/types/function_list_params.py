# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .function_type import FunctionType

__all__ = ["FunctionListParams"]


class FunctionListParams(TypedDict, total=False):
    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]

    function_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionIDs")]

    function_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionNames")]

    limit: int

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]

    tags: SequenceNotStr[str]

    types: List[FunctionType]

    workflow_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowIDs")]

    workflow_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowNames")]
