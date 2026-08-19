# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .related_entity import RelatedEntity

__all__ = ["EntityRetrieveRelationsResponse", "Inbound", "Outbound"]


class Inbound(BaseModel):
    """One edge pointing AT the queried entity (some other entity is the source)."""

    first_seen_at: datetime = FieldInfo(alias="firstSeenAt")
    """First-seen timestamp of the edge (RFC 3339)."""

    mention_count: int = FieldInfo(alias="mentionCount")
    """How many times this edge has been observed across parsed documents."""

    relation_type: str = FieldInfo(alias="relationType")
    """Free-form relation label (e.g. `author_of`, `affiliated_with`)."""

    source_entity: RelatedEntity = FieldInfo(alias="sourceEntity")
    """The entity at the tail of the edge."""


class Outbound(BaseModel):
    """One edge pointing AWAY from the queried entity (it is the source)."""

    first_seen_at: datetime = FieldInfo(alias="firstSeenAt")
    """First-seen timestamp of the edge (RFC 3339)."""

    mention_count: int = FieldInfo(alias="mentionCount")
    """How many times this edge has been observed across parsed documents."""

    relation_type: str = FieldInfo(alias="relationType")
    """Free-form relation label (e.g. `author_of`, `affiliated_with`)."""

    target_entity: RelatedEntity = FieldInfo(alias="targetEntity")
    """The entity at the head of the edge."""


class EntityRetrieveRelationsResponse(BaseModel):
    """Response body for `GET /v3/entities/{id}/relations`."""

    inbound: List[Inbound]
    """Edges pointing at the queried entity."""

    outbound: List[Outbound]
    """Edges pointing away from the queried entity."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """
    Opaque cursor for the next page of edges, or absent on the last page. Pass it
    back as `cursor`.
    """
