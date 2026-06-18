# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ReviewerListResponse", "Reviewer"]


class Reviewer(BaseModel):
    """
    A reviewer assignment links a user to an entity type they are responsible
    for reviewing. The assignment is scoped to an account+environment and is
    unique per (entity type, user).
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the assignment was created (RFC 3339)."""

    email: str
    """The assigned user's email."""

    reviewer_id: str = FieldInfo(alias="reviewerID")
    """Stable public identifier for the assignment (`etr_...`)."""

    role: str
    """The assigned user's account role (for example `operator`, `admin`)."""

    user_id: str = FieldInfo(alias="userID")
    """Public identifier of the assigned user (`usr_...`)."""


class ReviewerListResponse(BaseModel):
    """Response body for listing the reviewers of an entity type."""

    reviewers: List[Reviewer]
