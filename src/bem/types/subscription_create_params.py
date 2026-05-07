# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of subscription."""

    type: Required[
        Literal[
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
    ]
    """Type of subscription."""

    collection_id: Annotated[str, PropertyInfo(alias="collectionID")]
    """
    Unique identifier of collection this subscription listens to (alternative to
    collectionName).
    """

    collection_name: Annotated[str, PropertyInfo(alias="collectionName")]
    """
    Name of collection this subscription listens to (required for collection-based
    subscriptions).
    """

    disabled: bool
    """Toggles whether subscription is active or not."""

    function_id: Annotated[str, PropertyInfo(alias="functionID")]
    """
    Unique identifier of function this subscription listens to (alternative to
    functionName).
    """

    function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """
    Unique name of function this subscription listens to (required for
    function-based subscriptions).
    """

    google_drive_folder_id: Annotated[str, PropertyInfo(alias="googleDriveFolderID")]
    """Google Drive folder ID for syncing output data to Google Drive."""

    s3_bucket: Annotated[str, PropertyInfo(alias="s3Bucket")]
    """S3 bucket name for syncing output data to AWS S3."""

    s3_file_path: Annotated[str, PropertyInfo(alias="s3FilePath")]
    """S3 file path for syncing output data to AWS S3."""

    webhook_url: Annotated[str, PropertyInfo(alias="webhookURL")]
    """URL bem will send webhook requests to."""
