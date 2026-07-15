# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bucket_v3 import BucketV3

__all__ = ["BucketListResponse"]


class BucketListResponse(BaseModel):
    """Response body for listing buckets."""

    buckets: List[BucketV3]

    total_count: int = FieldInfo(alias="totalCount")
    """Total number of buckets matching the query, ignoring pagination."""
