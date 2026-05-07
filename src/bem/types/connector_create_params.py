# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .connector_type import ConnectorType

__all__ = ["ConnectorCreateParams"]


class ConnectorCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-friendly name for this connector."""

    type: Required[ConnectorType]
    """Connector type."""

    box_client_id: Annotated[str, PropertyInfo(alias="boxClientID")]
    """Box client ID (from your Box application)."""

    box_client_secret: Annotated[str, PropertyInfo(alias="boxClientSecret")]
    """Box client secret (from your Box application)."""

    box_enterprise_id: Annotated[str, PropertyInfo(alias="boxEnterpriseID")]
    """Box enterprise ID."""

    box_folder_id: Annotated[str, PropertyInfo(alias="boxFolderID")]
    """Box folder ID to watch for new uploads."""

    paragon_configuration: Annotated[object, PropertyInfo(alias="paragonConfiguration")]
    """Configuration specific to the type of integration."""

    paragon_integration: Annotated[str, PropertyInfo(alias="paragonIntegration")]
    """Paragon integration, eg. "googledrive"."""

    workflow_id: Annotated[str, PropertyInfo(alias="workflowID")]
    """One of `workflowID` or `workflowName` must be provided.

    If both are provided, they must refer to the same workflow.
    """

    workflow_name: Annotated[str, PropertyInfo(alias="workflowName")]
    """One of `workflowID` or `workflowName` must be provided.

    If both are provided, they must refer to the same workflow.
    """
