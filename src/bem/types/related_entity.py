# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RelatedEntity"]


class RelatedEntity(BaseModel):
    """
    A compact view of an entity sitting on the far end of a relation edge — the
    stable public id, the canonical name, and the effective type. The full
    entity is fetched separately via the entity detail / File System endpoints.
    """

    id: str
    """Stable public identifier for the entity (`ent_...`)."""

    canonical: str
    """Canonical (most descriptive) surface form of the entity."""

    depth: int
    """Hops from the queried entity.

    This endpoint returns direct relations, so this is 1 (a self-loop's far end is
    the queried entity itself, 0).
    """

    type: str
    """Effective entity type."""
