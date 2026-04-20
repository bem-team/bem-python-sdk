# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow import Workflow

__all__ = ["WorkflowUpdateResponse", "ConnectorError"]


class ConnectorError(BaseModel):
    """Per-connector failure surfaced alongside a successful workflow DAG save."""

    code: str
    """Machine-readable error code."""

    message: str
    """Human-readable error message."""

    operation: Literal["create", "update", "delete"]
    """Which diff operation was attempted."""

    connector_id: Optional[str] = FieldInfo(alias="connectorID", default=None)
    """Populated for update/delete failures."""

    name: Optional[str] = None
    """Populated for create failures."""


class WorkflowUpdateResponse(BaseModel):
    connector_errors: Optional[List[ConnectorError]] = FieldInfo(alias="connectorErrors", default=None)
    """Per-connector failures from the diff/apply phase.

    Empty or omitted when all operations succeeded.
    """

    error: Optional[str] = None
    """Error message if the workflow update failed."""

    workflow: Optional[Workflow] = None
    """V3 read representation of a workflow version."""
