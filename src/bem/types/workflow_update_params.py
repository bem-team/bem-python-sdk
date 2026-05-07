# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .workflow_edge_param import WorkflowEdgeParam
from .workflow_node_param import WorkflowNodeParam
from .workflow_connector_param import WorkflowConnectorParam

__all__ = ["WorkflowUpdateParams"]


class WorkflowUpdateParams(TypedDict, total=False):
    connectors: Iterable[WorkflowConnectorParam]
    """Declarative, full-desired-state array of connectors.

    If omitted, existing connectors are left unchanged. If provided, it replaces the
    current set: entries with `connectorID` are updates, entries without are
    creates, and existing connectors whose `connectorID` is absent are deleted.
    """

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Human-readable display name."""

    edges: Iterable[WorkflowEdgeParam]

    main_node_name: Annotated[str, PropertyInfo(alias="mainNodeName")]
    """
    `mainNodeName`, `nodes`, and `edges` must be provided together to update the DAG
    topology. If none are provided the topology is copied unchanged from the current
    version.
    """

    name: str
    """New name for the workflow (renames it). Must match `^[a-zA-Z0-9_-]{1,128}$`."""

    nodes: Iterable[WorkflowNodeParam]

    tags: SequenceNotStr[str]
    """Tags to categorize and organize the workflow."""
