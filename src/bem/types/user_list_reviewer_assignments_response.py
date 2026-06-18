# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserListReviewerAssignmentsResponse", "Assignment"]


class Assignment(BaseModel):
    """
    One entity type a user reviews, as returned by the reverse-lookup endpoint.
    The type is exposed via its public ID plus its name and description.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the assignment was created (RFC 3339)."""

    description: str
    """The entity type's description."""

    name: str
    """The entity type's human-facing name."""

    type_id: str = FieldInfo(alias="typeID")
    """Public ID (`ety_...`) of the entity type the user reviews."""


class UserListReviewerAssignmentsResponse(BaseModel):
    """Response body for the reverse lookup of a user's reviewer assignments."""

    assignments: List[Assignment]
