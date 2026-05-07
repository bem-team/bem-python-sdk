# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .workflow_connector_type import WorkflowConnectorType

__all__ = ["WorkflowConnectorParam", "Paragon"]


class Paragon(TypedDict, total=False):
    """Request-side config block for a Paragon connector.

    Fields absent on update are unchanged.
    """

    configuration: object
    """Opaque per-integration configuration. Required on create."""

    integration: str
    """Paragon integration key. Required on create."""


class WorkflowConnectorParam(TypedDict, total=False):
    """Create/update entry for a connector inline with the workflow."""

    name: Required[str]
    """Human-friendly connector name."""

    type: Required[WorkflowConnectorType]
    """Discriminator for a workflow connector. V3 supports `paragon` only."""

    connector_id: Annotated[str, PropertyInfo(alias="connectorID")]
    """Present → update. Absent → create."""

    paragon: Paragon
    """Request-side config block for a Paragon connector.

    Fields absent on update are unchanged.
    """
