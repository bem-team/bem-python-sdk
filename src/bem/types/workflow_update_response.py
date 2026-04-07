# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .workflow import Workflow

__all__ = ["WorkflowUpdateResponse"]


class WorkflowUpdateResponse(BaseModel):
    error: Optional[str] = None
    """Error message if the workflow update failed."""

    workflow: Optional[Workflow] = None
    """V3 read representation of a workflow version."""
