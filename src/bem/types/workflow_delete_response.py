# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow_connector_error import WorkflowConnectorError

__all__ = ["WorkflowDeleteResponse", "Workflow"]


class Workflow(BaseModel):
    """
    Identifies the workflow that was deleted, pinned to the version number it
    was on at deletion time.
    """

    id: str
    """Unique identifier of workflow."""

    name: str
    """Unique name of workflow. Must be UNIQUE on a per-environment basis."""

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of workflow version."""


class WorkflowDeleteResponse(BaseModel):
    connector_errors: Optional[List[WorkflowConnectorError]] = FieldInfo(alias="connectorErrors", default=None)
    """Per-connector failures from tearing down the deleted workflow's connectors.

    Connector teardown is best-effort: a failure here is reported but does not block
    the deletion, so a `200` response with a non-empty `connectorErrors` means the
    workflow is gone while one or more of its connectors may still need manual
    cleanup. Empty or omitted when all teardowns succeeded.
    """

    error: Optional[str] = None
    """Error message if the workflow deletion failed."""

    workflow: Optional[Workflow] = None
    """
    Identifies the workflow that was deleted, pinned to the version number it was on
    at deletion time.
    """
