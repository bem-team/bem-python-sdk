# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .user_action_summary import UserActionSummary
from .function_version_identifier import FunctionVersionIdentifier

__all__ = ["WorkflowUpdateResponse", "Workflow", "WorkflowEdge", "WorkflowNode", "WorkflowAudit"]


class WorkflowEdge(BaseModel):
    """Read representation of a directed edge between call-site nodes."""

    destination_node_name: str = FieldInfo(alias="destinationNodeName")
    """Name of the destination node."""

    source_node_name: str = FieldInfo(alias="sourceNodeName")
    """Name of the source node."""

    destination_name: Optional[str] = FieldInfo(alias="destinationName", default=None)
    """Labelled outlet on the source node, if any."""


class WorkflowNode(BaseModel):
    """Read representation of a call-site node."""

    function: FunctionVersionIdentifier
    """Function (and version) executing at this call site."""

    name: str
    """Name of this call site, unique within the workflow version."""


class WorkflowAudit(BaseModel):
    """Audit trail information."""

    version_created_by: Optional[UserActionSummary] = FieldInfo(alias="versionCreatedBy", default=None)
    """Information about who created the current version."""

    workflow_created_by: Optional[UserActionSummary] = FieldInfo(alias="workflowCreatedBy", default=None)
    """Information about who created the workflow."""

    workflow_last_updated_by: Optional[UserActionSummary] = FieldInfo(alias="workflowLastUpdatedBy", default=None)
    """Information about who last updated the workflow."""


class Workflow(BaseModel):
    """V3 read representation of a workflow version."""

    id: str
    """Unique identifier of the workflow."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time the workflow was created."""

    edges: List[WorkflowEdge]
    """All directed edges in this workflow version's DAG."""

    main_node_name: str = FieldInfo(alias="mainNodeName")
    """Name of the entry-point call-site node."""

    name: str
    """Unique name of the workflow within the environment."""

    nodes: List[WorkflowNode]
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


class WorkflowUpdateResponse(BaseModel):
    error: Optional[str] = None
    """Error message if the workflow update failed."""

    workflow: Optional[Workflow] = None
    """V3 read representation of a workflow version."""
