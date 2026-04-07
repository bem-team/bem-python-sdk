# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .function_version_identifier_param import FunctionVersionIdentifierParam

__all__ = ["WorkflowUpdateParams", "Edge", "Node"]


class WorkflowUpdateParams(TypedDict, total=False):
    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Human-readable display name."""

    edges: Iterable[Edge]

    main_node_name: Annotated[str, PropertyInfo(alias="mainNodeName")]
    """
    `mainNodeName`, `nodes`, and `edges` must be provided together to update the DAG
    topology. If none are provided the topology is copied unchanged from the current
    version.
    """

    name: str
    """New name for the workflow (renames it). Must match `^[a-zA-Z0-9_-]{1,128}$`."""

    nodes: Iterable[Node]

    tags: SequenceNotStr[str]
    """Tags to categorize and organize the workflow."""


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


class Node(TypedDict, total=False):
    """A single function call-site node in a workflow DAG."""

    function: Required[FunctionVersionIdentifierParam]
    """The function (and version) to execute at this call site."""

    name: str
    """Name for this call site.

    Must be unique within the workflow version. Defaults to the function's own name
    when omitted.
    """
