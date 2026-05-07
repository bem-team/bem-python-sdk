# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkflowEdgeParam"]


class WorkflowEdgeParam(TypedDict, total=False):
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
