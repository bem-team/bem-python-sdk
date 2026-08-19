# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .workflow_connector_type import WorkflowConnectorType

__all__ = ["WorkflowConnectorParam", "Paragon"]


class Paragon(TypedDict, total=False):
    """Paragon configuration. Required on create for `type: "paragon"`."""

    configuration: object
    """Opaque per-integration configuration. Required on create."""

    integration: str
    """Paragon integration key. Required on create."""


class WorkflowConnectorParam(TypedDict, total=False):
    """Create/update entry for a connector inline with the workflow."""

    name: Required[str]
    """Human-friendly connector name."""

    type: Required[WorkflowConnectorType]
    """Connector type. Must match stored type on update."""

    connector_id: Annotated[str, PropertyInfo(alias="connectorID")]
    """Present → update. Absent → create."""

    paragon: Paragon
    """Paragon configuration. Required on create for `type: "paragon"`."""
