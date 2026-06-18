# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReviewQueueListResponse", "Entity", "EntityPreviewMention"]


class EntityPreviewMention(BaseModel):
    """A single per-document occurrence of an entity, used in review-queue previews."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When this mention was recorded."""

    entity_id: str = FieldInfo(alias="entityID")
    """Public ID (`ent_...`) of the entity this mention resolves to."""

    mention_id: str = FieldInfo(alias="mentionID")
    """Public ID (`emn_...`) of this mention."""

    page: int
    """1-indexed page number within the source document."""

    reference_id: str = FieldInfo(alias="referenceID")
    """The user-provided document handle this mention came from."""

    surface: str
    """The exact surface string Parse extracted on the page."""

    section_label: Optional[str] = FieldInfo(alias="sectionLabel", default=None)
    """The parse-emitted section label this mention sat under, when present."""

    transformation_id: Optional[str] = FieldInfo(alias="transformationID", default=None)
    """Public ID of the parse transformation that produced this mention, when known."""


class Entity(BaseModel):
    """One row of the review queue: an entity plus a small preview of its mentions."""

    canonical: str
    """The canonical (longest / most descriptive) surface form."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the entity was created."""

    entity_id: str = FieldInfo(alias="entityID")
    """Public ID (`ent_...`) of the entity."""

    mention_count: int = FieldInfo(alias="mentionCount")
    """Total mentions across all parsed documents."""

    preview_mentions: List[EntityPreviewMention] = FieldInfo(alias="previewMentions")
    """
    A capped preview (up to 2) of the entity's first mentions, ordered by page then
    time, so a reviewer can triage without opening each entity.
    """

    status: str
    """Curation lifecycle state: `extracted`, `proposed`, `approved`, `rejected`."""

    surface_forms: List[str] = FieldInfo(alias="surfaceForms")
    """Distinct surface forms that have resolved to this entity."""

    type: str
    """The effective type name (assigned override if set, else bem-inferred)."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the entity was last updated."""

    description: Optional[str] = None
    """Free-form description of the entity, when present."""

    type_id: Optional[str] = FieldInfo(alias="typeID", default=None)
    """Public ID (`ety_...`) of the customer-assigned type, when one is set."""

    validated_at: Optional[datetime] = FieldInfo(alias="validatedAt", default=None)
    """When a human approved/rejected the entity. Omitted while un-validated."""

    validated_by_user_id: Optional[str] = FieldInfo(alias="validatedByUserID", default=None)
    """Public ID (`usr_...`) of the user who validated the entity, when known."""


class ReviewQueueListResponse(BaseModel):
    """`GET /v3/review-queue` response. Cursor-paginated by `entityID` ascending."""

    entities: List[Entity]
    """The page of entities awaiting curation."""

    has_more: bool = FieldInfo(alias="hasMore")
    """Whether more rows exist beyond this page."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Opaque cursor to pass as `?cursor=` for the next page.

    Empty when `hasMore` is false.
    """
