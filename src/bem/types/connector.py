# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .connector_type import ConnectorType

__all__ = ["Connector"]


class Connector(BaseModel):
    """
    A Connector represents an integration that triggers a Bem workflow from an external system.
    """

    box_client_id: str = FieldInfo(alias="boxClientID")
    """Box client ID (from your Box application)."""

    box_client_secret: str = FieldInfo(alias="boxClientSecret")
    """Box client secret (from your Box application).

    Note: This value is sensitive and should be stored securely.
    """

    box_enterprise_id: str = FieldInfo(alias="boxEnterpriseID")
    """Box enterprise ID."""

    box_folder_id: str = FieldInfo(alias="boxFolderID")
    """Box folder ID to watch for new uploads."""

    connector_id: str = FieldInfo(alias="connectorID")
    """Unique identifier for the connector."""

    name: str
    """Human-friendly name for this connector."""

    paragon_configuration: object = FieldInfo(alias="paragonConfiguration")
    """Configuration specific to the type of integration."""

    paragon_integration: str = FieldInfo(alias="paragonIntegration")
    """Paragon integration, eg. "googledrive"."""

    paragon_sync_id: str = FieldInfo(alias="paragonSyncID")
    """Paragon sync ID."""

    type: ConnectorType
    """Connector type."""

    workflow_id: str = FieldInfo(alias="workflowID")
    """Workflow API ID that will be triggered by this connector."""

    workflow_name: str = FieldInfo(alias="workflowName")
    """Workflow name that will be triggered by this connector."""
