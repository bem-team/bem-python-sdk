# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BucketListParams"]


class BucketListParams(TypedDict, total=False):
    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]
    """Cursor: return buckets whose `bucketID` sorts before this value."""

    limit: int
    """Maximum number of buckets to return (default 50, max 200)."""

    name_substring: Annotated[str, PropertyInfo(alias="nameSubstring")]
    """Case-insensitive substring match on the bucket name."""

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]
    """Cursor: return buckets whose `bucketID` sorts after this value."""
