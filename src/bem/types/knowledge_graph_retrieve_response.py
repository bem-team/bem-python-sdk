# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["KnowledgeGraphRetrieveResponse", "Edge", "Node"]


class Edge(BaseModel):
    """One directed edge between two entities, addressed by their public ids."""

    mention_count: int = FieldInfo(alias="mentionCount")
    """How many times this edge has been observed."""

    relation_type: str = FieldInfo(alias="relationType")
    """Free-form relation label."""

    source_id: str = FieldInfo(alias="sourceId")
    """Source entity public id (`ent_...`)."""

    target_id: str = FieldInfo(alias="targetId")
    """Target entity public id (`ent_...`)."""


class Node(BaseModel):
    """One entity node in the knowledge graph."""

    id: str
    """Stable public identifier for the entity (`ent_...`)."""

    canonical: str
    """Canonical (most descriptive) surface form."""

    depth: int
    """
    Hops from the center node when the request centers the graph on one entity
    (`nodeID`). The center is depth 0. When the request is uncentered (no `nodeID`),
    this is 0 for every node.
    """

    mention_count: int = FieldInfo(alias="mentionCount")
    """Total mentions of this entity across all parsed documents."""

    type: str
    """Effective entity type."""


class KnowledgeGraphRetrieveResponse(BaseModel):
    """Response body for `GET /v3/knowledge-graph`.

    Pagination is over edges;
    `nodes` are the distinct endpoint entities of the returned edge page (both
    endpoints of every edge are included).
    """

    edges: List[Edge]
    """The page of edges."""

    nodes: List[Node]
    """Distinct endpoint entities of the returned edge page."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """
    Opaque cursor for the next page of edges, or absent on the last page. Pass it
    back as `cursor`.
    """
