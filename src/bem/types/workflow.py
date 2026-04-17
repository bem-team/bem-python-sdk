# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow_audit import WorkflowAudit
from .workflow_edge_response import WorkflowEdgeResponse
from .workflow_node_response import WorkflowNodeResponse

__all__ = ["Workflow", "Connector", "ConnectorParagon"]


class ConnectorParagon(BaseModel):
    """Paragon-integration configuration on a workflow connector."""

    configuration: object
    """Opaque per-integration configuration (e.g. `{"folderId": "..."}`)."""

    integration: str
    """Paragon integration key (e.g. "googledrive")."""

    sync_id: str = FieldInfo(alias="syncID")
    """Paragon sync ID managed by the server. Read-only."""


class Connector(BaseModel):
    """A connector attached to a workflow. Ingestion point that triggers the workflow."""

    connector_id: str = FieldInfo(alias="connectorID")
    """Unique connector API ID."""

    name: str
    """Human-friendly connector name."""

    type: Literal["paragon"]
    """Discriminator for a workflow connector. V3 supports `paragon` only."""

    paragon: Optional[ConnectorParagon] = None
    """Paragon-integration configuration on a workflow connector."""


class Workflow(BaseModel):
    """V3 read representation of a workflow version."""

    id: str
    """Unique identifier of the workflow."""

    connectors: List[Connector]
    """Connectors currently attached to this workflow.

    For version-scoped reads (`/versions/{n}`) this is always empty — connectors are
    current-state and not part of version history.
    """

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
