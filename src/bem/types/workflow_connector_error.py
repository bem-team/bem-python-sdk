# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkflowConnectorError"]


class WorkflowConnectorError(BaseModel):
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
