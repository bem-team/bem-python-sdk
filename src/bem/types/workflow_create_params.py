# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .workflow_edge_param import WorkflowEdgeParam
from .workflow_node_param import WorkflowNodeParam
from .workflow_connector_param import WorkflowConnectorParam

__all__ = ["WorkflowCreateParams"]


class WorkflowCreateParams(TypedDict, total=False):
    main_node_name: Required[Annotated[str, PropertyInfo(alias="mainNodeName")]]
    """Name of the entry-point node. Must not be a destination of any edge."""

    name: Required[str]
    """Unique name for the workflow. Must match `^[a-zA-Z0-9_-]{1,128}$`."""

    nodes: Required[Iterable[WorkflowNodeParam]]
    """Call-site nodes in the DAG. At least one is required."""

    connectors: Iterable[WorkflowConnectorParam]
    """Connectors to attach to the workflow at creation.

    If any entry fails to provision, the entire workflow creation is rolled back.
    """

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Human-readable display name."""

    edges: Iterable[WorkflowEdgeParam]
    """Directed edges between nodes. Omit or leave empty for single-node workflows."""

    tags: SequenceNotStr[str]
    """Tags to categorize and organize the workflow."""
