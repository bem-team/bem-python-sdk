# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .entity_type import EntityType

__all__ = ["EntityTypeListResponse"]


class EntityTypeListResponse(BaseModel):
    """Response body for listing entity types."""

    entity_types: List[EntityType] = FieldInfo(alias="entityTypes")

    total_count: int = FieldInfo(alias="totalCount")
    """Total number of entity types matching the query, ignoring pagination."""
