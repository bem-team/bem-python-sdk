# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .user_action_summary import UserActionSummary

__all__ = ["WorkflowAudit"]


class WorkflowAudit(BaseModel):
    version_created_by: Optional[UserActionSummary] = FieldInfo(alias="versionCreatedBy", default=None)
    """Information about who created the current version."""

    workflow_created_by: Optional[UserActionSummary] = FieldInfo(alias="workflowCreatedBy", default=None)
    """Information about who created the workflow."""

    workflow_last_updated_by: Optional[UserActionSummary] = FieldInfo(alias="workflowLastUpdatedBy", default=None)
    """Information about who last updated the workflow."""
