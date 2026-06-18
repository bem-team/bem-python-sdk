# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ReviewQueueListParams"]


class ReviewQueueListParams(TypedDict, total=False):
    assigned_to: Annotated[str, PropertyInfo(alias="assignedTo")]
    """
    `me` or a `usr_...` ID — restrict to entities whose effective type that user
    reviews.
    """

    bucket: str
    """Optional bucket public ID (`bkt_...`) to scope to. Omit for all buckets."""

    cursor: str
    """Cursor — an `entityID` defining your place in the list."""

    limit: int

    since: str
    """RFC3339 timestamp — restrict to entities created at or after this time."""

    status: SequenceNotStr[str]
    """Restrict to these lifecycle states. Defaults to `extracted` + `proposed`."""

    type: SequenceNotStr[str]
    """Restrict to entities whose effective type is one of these `ety_...` IDs."""
