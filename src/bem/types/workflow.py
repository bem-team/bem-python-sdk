# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow_audit import WorkflowAudit
from .workflow_edge_response import WorkflowEdgeResponse
from .workflow_node_response import WorkflowNodeResponse

__all__ = ["Workflow"]


class Workflow(BaseModel):
    """V3 read representation of a workflow version."""

    id: str
    """Unique identifier of the workflow."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time the workflow was created."""

    edges: List[WorkflowEdgeResponse]
    """All directed edges in this workflow version's DAG."""

    main_node_name: str = FieldInfo(alias="mainNodeName")
    """Name of the entry-point call-site node."""

    name: str
    """Unique name of the workflow within the environment."""

    nodes: List[WorkflowNodeResponse]
    """All call-site nodes in this workflow version's DAG."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time the workflow was last updated."""

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of this workflow version."""

    audit: Optional[WorkflowAudit] = None
    """Audit trail information."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Human-readable display name."""

    email_address: Optional[str] = FieldInfo(alias="emailAddress", default=None)
    """Inbound email address associated with the workflow, if any."""

    tags: Optional[List[str]] = None
    """Tags associated with the workflow."""
