# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .enrich_config import EnrichConfig
from .function_audit import FunctionAudit
from .workflow_usage_info import WorkflowUsageInfo
from .split_function_semantic_page_item_class import SplitFunctionSemanticPageItemClass

__all__ = [
    "FunctionListResponse",
    "TransformFunction",
    "ExtractFunction",
    "AnalyzeFunction",
    "ClassifyFunction",
    "ClassifyFunctionClassification",
    "ClassifyFunctionClassificationOrigin",
    "ClassifyFunctionClassificationOriginEmail",
    "ClassifyFunctionClassificationRegex",
    "SendFunction",
    "SplitFunction",
    "SplitFunctionPrintPageSplitConfig",
    "SplitFunctionSemanticPageSplitConfig",
    "JoinFunction",
    "PayloadShapingFunction",
    "EnrichFunction",
]


class TransformFunction(BaseModel):
    email_address: str = FieldInfo(alias="emailAddress")
    """Email address automatically created by bem.

    You can forward emails with or without attachments, to be transformed.
    """

    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    output_schema: object = FieldInfo(alias="outputSchema")
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: str = FieldInfo(alias="outputSchemaName")
    """Name of output schema object."""

    tabular_chunking_enabled: bool = FieldInfo(alias="tabularChunkingEnabled")
    """Whether tabular chunking is enabled on the pipeline.

    This processes tables in CSV/Excel in row batches, rather than all rows at once.
    """

    type: Literal["transform"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class ExtractFunction(BaseModel):
    """
    A function that extracts structured JSON from documents and images.
    Accepts a wide range of input types including PDFs, images, spreadsheets, emails, and more.
    """

    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    output_schema: object = FieldInfo(alias="outputSchema")
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: str = FieldInfo(alias="outputSchemaName")
    """Name of output schema object."""

    tabular_chunking_enabled: bool = FieldInfo(alias="tabularChunkingEnabled")
    """Whether tabular chunking is enabled.

    When true, tables in CSV/Excel files are processed in row batches rather than
    all at once.
    """

    type: Literal["extract"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class AnalyzeFunction(BaseModel):
    enable_bounding_boxes: bool = FieldInfo(alias="enableBoundingBoxes")
    """Whether bounding box extraction is enabled.

    Only applicable to analyze and extract functions. When true, the function
    returns the document regions (page, coordinates) from which each field was
    extracted.
    """

    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    output_schema: object = FieldInfo(alias="outputSchema")
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: str = FieldInfo(alias="outputSchemaName")
    """Name of output schema object."""

    pre_count: bool = FieldInfo(alias="preCount")
    """
    Reducing the risk of the model stopping early on long documents. Trade-off:
    Increases total latency.
    """

    type: Literal["analyze"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class ClassifyFunctionClassificationOriginEmail(BaseModel):
    patterns: Optional[List[str]] = None


class ClassifyFunctionClassificationOrigin(BaseModel):
    email: Optional[ClassifyFunctionClassificationOriginEmail] = None


class ClassifyFunctionClassificationRegex(BaseModel):
    patterns: Optional[List[str]] = None


class ClassifyFunctionClassification(BaseModel):
    name: str

    description: Optional[str] = None

    function_id: Optional[str] = FieldInfo(alias="functionID", default=None)

    function_name: Optional[str] = FieldInfo(alias="functionName", default=None)

    is_error_fallback: Optional[bool] = FieldInfo(alias="isErrorFallback", default=None)

    origin: Optional[ClassifyFunctionClassificationOrigin] = None

    regex: Optional[ClassifyFunctionClassificationRegex] = None


class ClassifyFunction(BaseModel):
    """V3 read-side shape of a Classify (internally Route) function.

    Mirrors
    {
    """

    classifications: List[ClassifyFunctionClassification]
    """V3 create/update variants of the shared function payloads.

    The V3 Functions API no longer accepts the legacy `transform` or `analyze`
    function types when creating new functions or updating existing ones — both have
    been unified under `extract`. Existing functions of those types remain readable
    and callable via V3, so the V3 read-side unions still include `transform` and
    `analyze` variants.

    The V3 API also renames the internal `route` function type to `classify` on the
    wire, and the associated `routes` field to `classifications` (type
    `ClassificationList`). Platform-internal storage and processing still use
    `route` / `routes`; the rename is applied only at the V3 API boundary.V3-facing
    name for the list of classifications a classify function can produce.
    """

    description: str
    """Description of classifier.

    Can be used to provide additional context on classifier's purpose and expected
    inputs.
    """

    email_address: str = FieldInfo(alias="emailAddress")
    """Email address automatically created by bem.

    You can forward emails with or without attachments, to be classified.
    """

    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Literal["classify"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class SendFunction(BaseModel):
    """
    A function that delivers workflow outputs to an external destination.
    Send functions receive the output of an upstream workflow node and forward it
    to a webhook, S3 bucket, or Google Drive folder.
    """

    destination_type: Literal["webhook", "s3", "google_drive"] = FieldInfo(alias="destinationType")
    """Destination type for a Send function."""

    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Literal["send"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    google_drive_folder_id: Optional[str] = FieldInfo(alias="googleDriveFolderId", default=None)
    """Google Drive folder ID.

    Present when destinationType is google_drive. Managed via Paragon OAuth.
    """

    s3_bucket: Optional[str] = FieldInfo(alias="s3Bucket", default=None)
    """S3 bucket to upload the payload to. Present when destinationType is s3."""

    s3_prefix: Optional[str] = FieldInfo(alias="s3Prefix", default=None)
    """S3 key prefix (folder path). Optional, present when destinationType is s3."""

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""

    webhook_signing_enabled: Optional[bool] = FieldInfo(alias="webhookSigningEnabled", default=None)
    """Whether webhook payloads are signed with an HMAC-SHA256 `bem-signature` header."""

    webhook_url: Optional[str] = FieldInfo(alias="webhookUrl", default=None)
    """Webhook URL to POST the payload to. Present when destinationType is webhook."""


class SplitFunctionPrintPageSplitConfig(BaseModel):
    """Configuration for print page splitting."""

    next_function_id: Optional[str] = FieldInfo(alias="nextFunctionID", default=None)


class SplitFunctionSemanticPageSplitConfig(BaseModel):
    """Configuration for semantic page splitting."""

    item_classes: Optional[List[SplitFunctionSemanticPageItemClass]] = FieldInfo(alias="itemClasses", default=None)


class SplitFunction(BaseModel):
    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    split_type: Literal["print_page", "semantic_page"] = FieldInfo(alias="splitType")
    """The method used to split pages."""

    type: Literal["split"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    print_page_split_config: Optional[SplitFunctionPrintPageSplitConfig] = FieldInfo(
        alias="printPageSplitConfig", default=None
    )
    """Configuration for print page splitting."""

    semantic_page_split_config: Optional[SplitFunctionSemanticPageSplitConfig] = FieldInfo(
        alias="semanticPageSplitConfig", default=None
    )
    """Configuration for semantic page splitting."""

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class JoinFunction(BaseModel):
    description: str
    """Description of join function."""

    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    join_type: Literal["standard"] = FieldInfo(alias="joinType")
    """The type of join to perform."""

    output_schema: object = FieldInfo(alias="outputSchema")
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: str = FieldInfo(alias="outputSchemaName")
    """Name of output schema object."""

    type: Literal["join"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class PayloadShapingFunction(BaseModel):
    """
    A function that transforms and customizes input payloads using JMESPath expressions.
    Payload shaping allows you to extract specific data, perform calculations, and reshape
    complex input structures into simplified, standardized output formats tailored to your
    downstream systems or business requirements.
    """

    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    shaping_schema: str = FieldInfo(alias="shapingSchema")
    """
    JMESPath expression that defines how to transform and customize the input
    payload structure. Payload shaping allows you to extract, reshape, and
    reorganize data from complex input payloads into a simplified, standardized
    output format. Use JMESPath syntax to select specific fields, perform
    calculations, and create new data structures tailored to your needs.
    """

    type: Literal["payload_shaping"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class EnrichFunction(BaseModel):
    config: EnrichConfig
    """Configuration for enrich function with semantic search steps.

    **How Enrich Functions Work:**

    Enrich functions use semantic search to augment JSON data with relevant
    information from collections. They take JSON input (typically from a transform
    function), extract specified fields, perform vector-based semantic search
    against collections, and inject the results back into the data.

    **Input Requirements:**

    - Must receive JSON input (typically uploaded to S3 from a previous function)
    - Can be chained after transform or other functions that produce JSON output

    **Example Use Cases:**

    - Match product descriptions to SKU codes from a product catalog
    - Enrich customer data with account information
    - Link order line items to inventory records

    **Configuration:**

    - Define one or more enrichment steps
    - Each step extracts values, searches a collection, and injects results
    - Steps are executed sequentially
    """

    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Literal["enrich"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


FunctionListResponse: TypeAlias = Annotated[
    Union[
        TransformFunction,
        ExtractFunction,
        AnalyzeFunction,
        ClassifyFunction,
        SendFunction,
        SplitFunction,
        JoinFunction,
        PayloadShapingFunction,
        EnrichFunction,
    ],
    PropertyInfo(discriminator="type"),
]
