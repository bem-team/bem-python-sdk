# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .view import View
from .._models import BaseModel

__all__ = ["ViewListResponse"]


class ViewListResponse(BaseModel):
    """Response containing a list of views"""

    total_count: int = FieldInfo(alias="totalCount")
    """Total number of views matching the query"""

    views: List[View]
    """Array of views"""
