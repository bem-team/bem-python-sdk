# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow import Workflow

__all__ = ["WorkflowListResponse"]


class WorkflowListResponse(BaseModel):
    error: Optional[str] = None
    """Error message if the workflow listing failed."""

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
    """The total number of results available."""

    workflows: Optional[List[Workflow]] = None
