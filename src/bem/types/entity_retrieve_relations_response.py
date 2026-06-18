# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EntityRetrieveRelationsResponse", "Inbound", "InboundSourceEntity", "Outbound", "OutboundTargetEntity"]


class InboundSourceEntity(BaseModel):
    """
    A compact view of an entity sitting on the far end of a relation edge — the
    stable public id, the canonical name, and the effective type. The full
    entity is fetched separately via the entity detail / File System endpoints.
    """

    id: str
    """Stable public identifier for the entity (`ent_...`)."""

    canonical: str
    """Canonical (most descriptive) surface form of the entity."""

    type: str
    """Effective entity type."""


class Inbound(BaseModel):
    """One edge pointing AT the queried entity (some other entity is the source)."""

    first_seen_at: datetime = FieldInfo(alias="firstSeenAt")
    """First-seen timestamp of the edge (RFC 3339)."""

    mention_count: int = FieldInfo(alias="mentionCount")
    """How many times this edge has been observed across parsed documents."""

    relation_type: str = FieldInfo(alias="relationType")
    """Free-form relation label (e.g. `author_of`, `affiliated_with`)."""

    source_entity: InboundSourceEntity = FieldInfo(alias="sourceEntity")
    """
    A compact view of an entity sitting on the far end of a relation edge — the
    stable public id, the canonical name, and the effective type. The full entity is
    fetched separately via the entity detail / File System endpoints.
    """


class OutboundTargetEntity(BaseModel):
    """
    A compact view of an entity sitting on the far end of a relation edge — the
    stable public id, the canonical name, and the effective type. The full
    entity is fetched separately via the entity detail / File System endpoints.
    """

    id: str
    """Stable public identifier for the entity (`ent_...`)."""

    canonical: str
    """Canonical (most descriptive) surface form of the entity."""

    type: str
    """Effective entity type."""


class Outbound(BaseModel):
    """One edge pointing AWAY from the queried entity (it is the source)."""

    first_seen_at: datetime = FieldInfo(alias="firstSeenAt")
    """First-seen timestamp of the edge (RFC 3339)."""

    mention_count: int = FieldInfo(alias="mentionCount")
    """How many times this edge has been observed across parsed documents."""

    relation_type: str = FieldInfo(alias="relationType")
    """Free-form relation label (e.g. `author_of`, `affiliated_with`)."""

    target_entity: OutboundTargetEntity = FieldInfo(alias="targetEntity")
    """
    A compact view of an entity sitting on the far end of a relation edge — the
    stable public id, the canonical name, and the effective type. The full entity is
    fetched separately via the entity detail / File System endpoints.
    """


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
