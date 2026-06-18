# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BucketListResponse", "Bucket"]


class Bucket(BaseModel):
    """
    A Bucket is a named partition of the knowledge graph within an
    account+environment. Entities, mentions, and relations are scoped to a
    bucket so a single account+environment can host multiple isolated graphs.

    Every account+environment has exactly one default bucket. The default
    bucket can be renamed but never deleted.
    """

    bucket_id: str = FieldInfo(alias="bucketID")
    """Stable public identifier for the bucket (`bkt_...`)."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp (RFC 3339)."""

    description: str
    """Optional human-facing note about the bucket."""

    is_default: bool = FieldInfo(alias="isDefault")
    """Whether this is the account+environment's default bucket."""

    name: str
    """Human-facing bucket name. Unique within an account+environment."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Last-update timestamp (RFC 3339)."""


class BucketListResponse(BaseModel):
    """Response body for listing buckets."""

    buckets: List[Bucket]

    total_count: int = FieldInfo(alias="totalCount")
    """Total number of buckets matching the query, ignoring pagination."""
