# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VersionListParams"]


class VersionListParams(TypedDict, total=False):
    ending_before: Annotated[int, PropertyInfo(alias="endingBefore")]

    limit: int

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]

    starting_after: Annotated[int, PropertyInfo(alias="startingAfter")]
