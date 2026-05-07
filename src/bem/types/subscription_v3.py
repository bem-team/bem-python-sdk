# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SubscriptionV3"]


class SubscriptionV3(BaseModel):
    name: str
    """Name of subscription."""

    subscription_id: str = FieldInfo(alias="subscriptionID")
    """The unique identifier of the subscription."""

    type: Literal[
        "transform",
        "analyze",
        "route",
        "join",
        "split_collection",
        "split_item",
        "evaluation",
        "error",
        "payload_shaping",
        "enrich",
        "collection_processing",
    ]
    """Type of subscription."""

    collection_id: Optional[str] = FieldInfo(alias="collectionID", default=None)
    """Unique identifier of collection this subscription listens to."""

    collection_name: Optional[str] = FieldInfo(alias="collectionName", default=None)
    """Name of collection this subscription listens to."""

    disabled: Optional[bool] = None
    """Toggles whether subscription is active or not."""

    function_id: Optional[str] = FieldInfo(alias="functionID", default=None)
    """Unique identifier of function this subscription listens to."""

    function_name: Optional[str] = FieldInfo(alias="functionName", default=None)
    """Unique name of function this subscription listens to."""

    google_drive_folder_id: Optional[str] = FieldInfo(alias="googleDriveFolderID", default=None)
    """Google Drive folder ID for syncing output data to Google Drive."""

    s3_bucket: Optional[str] = FieldInfo(alias="s3Bucket", default=None)
    """S3 bucket name for syncing output data to AWS S3."""

    s3_file_path: Optional[str] = FieldInfo(alias="s3FilePath", default=None)
    """S3 file path for syncing output data to AWS S3."""

    webhook_url: Optional[str] = FieldInfo(alias="webhookURL", default=None)
    """URL bem will send webhook requests to."""
