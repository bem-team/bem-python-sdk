# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkflowUsageInfo"]


class WorkflowUsageInfo(BaseModel):
    current_version_num: int = FieldInfo(alias="currentVersionNum")
    """
    Current version number of workflow, provided for reference - compare to
    usedInWorkflowVersionNums to see whether the current version of the workflow
    uses this function version.
    """

    used_in_workflow_version_nums: List[int] = FieldInfo(alias="usedInWorkflowVersionNums")
    """Version numbers of workflows that this function version is used in."""

    workflow_id: str = FieldInfo(alias="workflowID")
    """Unique identifier of workflow."""

    workflow_name: str = FieldInfo(alias="workflowName")
    """Name of workflow."""
