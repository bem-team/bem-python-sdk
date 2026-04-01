# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .function import Function

__all__ = ["ListFunctionsResponse"]


class ListFunctionsResponse(BaseModel):
    functions: Optional[List[Function]] = None

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
    """The total number of results available."""
