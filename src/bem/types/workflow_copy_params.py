# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WorkflowCopyParams"]


class WorkflowCopyParams(TypedDict, total=False):
    source_workflow_name: Required[Annotated[str, PropertyInfo(alias="sourceWorkflowName")]]
    """Name of the source workflow to copy from."""

    target_workflow_name: Required[Annotated[str, PropertyInfo(alias="targetWorkflowName")]]
    """Name for the new copied workflow. Must be unique within the target environment."""

    source_workflow_version_num: Annotated[int, PropertyInfo(alias="sourceWorkflowVersionNum")]
    """Optional version number of the source workflow to copy.

    If not provided, copies the current version.
    """

    tags: SequenceNotStr[str]
    """Optional tags for the copied workflow.

    If not provided, uses the source workflow's tags.
    """

    target_display_name: Annotated[str, PropertyInfo(alias="targetDisplayName")]
    """Optional display name for the copied workflow.

    If not provided, uses the source workflow's display name with " (Copy)"
    appended.
    """

    target_environment: Annotated[str, PropertyInfo(alias="targetEnvironment")]
    """Optional target environment name.

    If provided, copies the workflow to a different environment. When copying to a
    different environment, all functions used in the workflow will also be copied.
    """
