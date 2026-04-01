# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .user_action_summary import UserActionSummary

__all__ = ["FunctionAudit"]


class FunctionAudit(BaseModel):
    function_created_by: Optional[UserActionSummary] = FieldInfo(alias="functionCreatedBy", default=None)
    """Information about who created the function."""

    function_last_updated_by: Optional[UserActionSummary] = FieldInfo(alias="functionLastUpdatedBy", default=None)
    """Information about who last updated the function."""

    version_created_by: Optional[UserActionSummary] = FieldInfo(alias="versionCreatedBy", default=None)
    """Information about who created the current version."""
