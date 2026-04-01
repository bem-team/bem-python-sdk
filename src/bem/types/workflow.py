# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .user_action_summary import UserActionSummary
from .function_version_identifier import FunctionVersionIdentifier

__all__ = ["Workflow", "Audit", "Relationship"]


class Audit(BaseModel):
    """Audit trail information for the workflow."""

    version_created_by: Optional[UserActionSummary] = FieldInfo(alias="versionCreatedBy", default=None)
    """Information about who created the current version."""

    workflow_created_by: Optional[UserActionSummary] = FieldInfo(alias="workflowCreatedBy", default=None)
    """Information about who created the workflow."""

    workflow_last_updated_by: Optional[UserActionSummary] = FieldInfo(alias="workflowLastUpdatedBy", default=None)
    """Information about who last updated the workflow."""


class Relationship(BaseModel):
    destination_function: FunctionVersionIdentifier = FieldInfo(alias="destinationFunction")

    source_function: FunctionVersionIdentifier = FieldInfo(alias="sourceFunction")

    destination_name: Optional[str] = FieldInfo(alias="destinationName", default=None)
    """Name of destination."""


class Workflow(BaseModel):
    id: str
    """Unique identifier of workflow."""

    main_function: FunctionVersionIdentifier = FieldInfo(alias="mainFunction")

    name: str
    """Unique name of workflow. Must be UNIQUE on a per-environment basis."""

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of workflow version."""

    audit: Optional[Audit] = None
    """Audit trail information for the workflow."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time the workflow was created."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of workflow."""

    email_address: Optional[str] = FieldInfo(alias="emailAddress", default=None)
    """Email address of workflow."""

    relationships: Optional[List[Relationship]] = None

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize workflows."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time the workflow was last updated."""
