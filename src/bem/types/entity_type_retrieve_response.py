# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EntityTypeRetrieveResponse"]


class EntityTypeRetrieveResponse(BaseModel):
    """
    An EntityType is a customer-defined type in the knowledge-graph taxonomy,
    scoped to an account+environment. Types may be organised into hierarchies
    via `parentTypeID`, and may carry per-type structured attribute metadata in
    `attributeSchema` (for example `{"unit": "mg", "range": [0, 100]}`).
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp (RFC 3339)."""

    description: str
    """Optional human-facing note about the type."""

    name: str
    """Human-facing type name.

    Unique within an account+environment, and immutable once set.
    """

    parent_type_id: str = FieldInfo(alias="parentTypeID")
    """
    Public ID (`ety_...`) of the parent type, or an empty string when the type is
    top-level.
    """

    type_id: str = FieldInfo(alias="typeID")
    """Stable public identifier for the entity type (`ety_...`)."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Last-update timestamp (RFC 3339)."""

    attribute_schema: Optional[object] = FieldInfo(alias="attributeSchema", default=None)
    """Optional per-type structured attribute metadata."""
