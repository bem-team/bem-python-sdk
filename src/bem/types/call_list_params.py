# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["CallListParams"]


class CallListParams(TypedDict, total=False):
    call_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="callIDs")]

    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]

    limit: int

    reference_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="referenceIDs")]

    reference_id_substring: Annotated[str, PropertyInfo(alias="referenceIDSubstring")]
    """Case-insensitive substring match against `callReferenceID`."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]

    statuses: List[Literal["pending", "running", "completed", "failed"]]
    """Filter by one or more statuses."""

    workflow_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowIDs")]

    workflow_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowNames")]
