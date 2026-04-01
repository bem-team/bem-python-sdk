# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .function_version import FunctionVersion

__all__ = ["ListFunctionVersionsResponse"]


class ListFunctionVersionsResponse(BaseModel):
    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
    """The total number of results available."""

    versions: Optional[List[FunctionVersion]] = None
