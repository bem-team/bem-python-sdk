# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .call_v3 import CallV3
from .._models import BaseModel

__all__ = ["CallListResponse"]


class CallListResponse(BaseModel):
    calls: Optional[List[CallV3]] = None

    error: Optional[str] = None
    """Error message if the calls listing failed."""

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
    """The total number of results available."""
