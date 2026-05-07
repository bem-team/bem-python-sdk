# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow import Workflow
from .workflow_connector_error import WorkflowConnectorError

__all__ = ["WorkflowUpdateResponse"]


class WorkflowUpdateResponse(BaseModel):
    connector_errors: Optional[List[WorkflowConnectorError]] = FieldInfo(alias="connectorErrors", default=None)
    """Per-connector failures from the diff/apply phase.

    Empty or omitted when all operations succeeded.
    """

    error: Optional[str] = None
    """Error message if the workflow update failed."""

    workflow: Optional[Workflow] = None
    """V3 read representation of a workflow version."""
