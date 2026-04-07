# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkflowEdgeResponse"]


class WorkflowEdgeResponse(BaseModel):
    """Read representation of a directed edge between call-site nodes."""

    destination_node_name: str = FieldInfo(alias="destinationNodeName")
    """Name of the destination node."""

    source_node_name: str = FieldInfo(alias="sourceNodeName")
    """Name of the source node."""

    destination_name: Optional[str] = FieldInfo(alias="destinationName", default=None)
    """Labelled outlet on the source node, if any."""
