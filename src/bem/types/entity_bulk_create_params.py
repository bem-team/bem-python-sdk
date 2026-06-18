# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EntityBulkCreateParams", "Entity"]


class EntityBulkCreateParams(TypedDict, total=False):
    entities: Required[Iterable[Entity]]
    """The entities to seed. Must be non-empty."""

    bucket: str
    """Optional bucket public ID (`bkt_...`) to seed into.

    Omit to use the account+environment default bucket.
    """

    on_conflict: Annotated[Literal["merge"], PropertyInfo(alias="onConflict")]
    """Conflict strategy for an entity that already exists.

    Only `merge` is supported and it is the default: synonyms are added additively,
    a longer description replaces the old one, and attributes are merged with new
    keys winning.
    """


class Entity(TypedDict, total=False):
    """One entity to seed in a `POST /v3/entities/bulk` batch."""

    canonical: Required[str]
    """The canonical (longest / most descriptive) surface form for the entity, e.g.

    `Acme Corporation`. Required. Normalized (lowercased, whitespace-folded) for the
    uniqueness key.
    """

    type: Required[str]
    """The entity type name, e.g.

    `instrument` or `organization`. Required. Resolved against your taxonomy and
    created if it does not yet exist.
    """

    attributes: object
    """
    Optional per-entity structured attribute values, e.g.
    `{ "manufacturer": "Acme", "dosageMg": 50 }`. When the entity's type declares an
    attribute schema, keys not present in that schema cause the row to be rejected.
    """

    description: str
    """Optional free-form description of the entity."""

    synonyms: SequenceNotStr[str]
    """Optional additional surface forms to attach as `customer_defined` synonyms."""
