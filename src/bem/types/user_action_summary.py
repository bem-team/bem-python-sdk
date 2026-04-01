# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserActionSummary"]


class UserActionSummary(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time the action was created."""

    user_action_id: str = FieldInfo(alias="userActionID")
    """Unique identifier of the user action."""

    api_key_name: Optional[str] = FieldInfo(alias="apiKeyName", default=None)
    """API key name. Present for API key-initiated actions."""

    email_address: Optional[str] = FieldInfo(alias="emailAddress", default=None)
    """Email address. Present for email-initiated actions."""

    user_email: Optional[str] = FieldInfo(alias="userEmail", default=None)
    """User's email address. Present for user-initiated actions."""

    user_id: Optional[str] = FieldInfo(alias="userID", default=None)
    """User's ID. Present for user-initiated actions."""
