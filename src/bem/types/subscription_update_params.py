# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionUpdateParams"]


class SubscriptionUpdateParams(TypedDict, total=False):
    disabled: bool
    """Toggles whether subscription is active or not."""

    function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Unique name of function this subscription listens to."""

    google_drive_folder_id: Annotated[str, PropertyInfo(alias="googleDriveFolderID")]
    """Google Drive folder ID for syncing output data to Google Drive."""

    name: str
    """Name of subscription."""

    s3_bucket: Annotated[str, PropertyInfo(alias="s3Bucket")]
    """S3 bucket name for syncing output data to AWS S3."""

    s3_file_path: Annotated[str, PropertyInfo(alias="s3FilePath")]
    """S3 file path for syncing output data to AWS S3."""

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

    webhook_url: Annotated[str, PropertyInfo(alias="webhookURL")]
    """URL bem will send webhook requests to."""
