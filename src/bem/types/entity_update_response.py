# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EntityUpdateResponse"]


class EntityUpdateResponse(BaseModel):
    """An entity record, including its curation status and assigned type."""

    canonical: str
    """The canonical (longest / most descriptive) surface form."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp."""

    entity_id: str = FieldInfo(alias="entityID")
    """Public ID (`ent_...`)."""

    mention_count: int = FieldInfo(alias="mentionCount")
    """Total mentions across parsed documents."""

    status: Literal["extracted", "proposed", "approved", "rejected"]
    """Curation lifecycle state."""

    surface_forms: List[str] = FieldInfo(alias="surfaceForms")
    """Distinct surface forms resolved to this entity."""

    type: str
    """The entity's effective type name (assigned type if set, else inferred)."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Last-update timestamp."""

    description: Optional[str] = None
    """Free-form description."""

    type_id: Optional[str] = FieldInfo(alias="typeID", default=None)
    """`ety_...` public ID of the assigned type, when one is set."""

    validated_at: Optional[datetime] = FieldInfo(alias="validatedAt", default=None)
    """When the entity was approved/rejected. Present only once validated."""

    validated_by_user_id: Optional[str] = FieldInfo(alias="validatedByUserID", default=None)
    """`usr_...` public ID of the validating user (dashboard transitions only)."""
