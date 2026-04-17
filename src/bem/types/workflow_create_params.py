# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .function_version_identifier_param import FunctionVersionIdentifierParam

__all__ = ["WorkflowCreateParams", "Node", "Connector", "ConnectorParagon", "Edge"]


class WorkflowCreateParams(TypedDict, total=False):
    main_node_name: Required[Annotated[str, PropertyInfo(alias="mainNodeName")]]
    """Name of the entry-point node. Must not be a destination of any edge."""

    name: Required[str]
    """Unique name for the workflow. Must match `^[a-zA-Z0-9_-]{1,128}$`."""

    nodes: Required[Iterable[Node]]
    """Call-site nodes in the DAG. At least one is required."""

    connectors: Iterable[Connector]
    """Connectors to attach to the workflow at creation.

    If any entry fails to provision, the entire workflow creation is rolled back.
    """

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Human-readable display name."""

    edges: Iterable[Edge]
    """Directed edges between nodes. Omit or leave empty for single-node workflows."""

    tags: SequenceNotStr[str]
    """Tags to categorize and organize the workflow."""


class Node(TypedDict, total=False):
    """A single function call-site node in a workflow DAG."""

    function: Required[FunctionVersionIdentifierParam]
    """The function (and version) to execute at this call site."""

    metadata: object
    """Opaque free-form JSON object attached to this node.

    Stored and returned verbatim; the server does not interpret it. Intended for
    client-side concerns such as canvas display properties (position, color,
    collapsed state, etc.).
    """

    name: str
    """Name for this call site.

    Must be unique within the workflow version. Defaults to the function's own name
    when omitted.
    """


class ConnectorParagon(TypedDict, total=False):
    """Request-side config block for a Paragon connector.

    Fields absent on update are unchanged.
    """

    configuration: object
    """Opaque per-integration configuration. Required on create."""

    integration: str
    """Paragon integration key. Required on create."""


class Connector(TypedDict, total=False):
    """Create/update entry for a connector inline with the workflow."""

    name: Required[str]
    """Human-friendly connector name."""

    type: Required[Literal["paragon"]]
    """Discriminator for a workflow connector. V3 supports `paragon` only."""

    connector_id: Annotated[str, PropertyInfo(alias="connectorID")]
    """Present → update. Absent → create."""

    paragon: ConnectorParagon
    """Request-side config block for a Paragon connector.

    Fields absent on update are unchanged.
    """


class Edge(TypedDict, total=False):
    """A directed edge between two named call-site nodes."""

    destination_node_name: Required[Annotated[str, PropertyInfo(alias="destinationNodeName")]]
    """Name of the destination node."""

    source_node_name: Required[Annotated[str, PropertyInfo(alias="sourceNodeName")]]
    """Name of the source node."""

    destination_name: Annotated[str, PropertyInfo(alias="destinationName")]
    """
    Labelled outlet on the source node that activates this edge. Omit for the
    default (unlabelled) outlet.
    """

    metadata: object
    """Opaque free-form JSON object attached to this edge.

    Stored and returned verbatim; the server does not interpret it.
    """
