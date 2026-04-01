# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .workflow import Workflow

__all__ = ["WorkflowCreateResponse"]


class WorkflowCreateResponse(BaseModel):
    error: Optional[str] = None
    """Error message if the workflow creation failed."""

    workflow: Optional[Workflow] = None
