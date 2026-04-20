# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..enrich_config import EnrichConfig
from ..function_audit import FunctionAudit
from ..workflow_usage_info import WorkflowUsageInfo
from ..split_function_semantic_page_item_class import SplitFunctionSemanticPageItemClass

__all__ = [
    "VersionListResponse",
    "Version",
    "VersionTransformFunctionVersion",
    "VersionExtractFunctionVersion",
    "VersionAnalyzeFunctionVersion",
    "VersionClassifyFunctionVersion",
    "VersionClassifyFunctionVersionClassification",
    "VersionClassifyFunctionVersionClassificationOrigin",
    "VersionClassifyFunctionVersionClassificationOriginEmail",
    "VersionClassifyFunctionVersionClassificationRegex",
    "VersionSendFunctionVersion",
    "VersionSplitFunctionVersion",
    "VersionSplitFunctionVersionPrintPageSplitConfig",
    "VersionSplitFunctionVersionSemanticPageSplitConfig",
    "VersionJoinFunctionVersion",
    "VersionEnrichFunctionVersion",
    "VersionPayloadShapingFunctionVersion",
]


class VersionTransformFunctionVersion(BaseModel):
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
    """Audit trail information for the function version."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time the function version was created."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class VersionExtractFunctionVersion(BaseModel):
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
    """Audit trail information for the function version."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time the function version was created."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class VersionAnalyzeFunctionVersion(BaseModel):
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
    """Audit trail information for the function version."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time the function version was created."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class VersionClassifyFunctionVersionClassificationOriginEmail(BaseModel):
    patterns: Optional[List[str]] = None


class VersionClassifyFunctionVersionClassificationOrigin(BaseModel):
    email: Optional[VersionClassifyFunctionVersionClassificationOriginEmail] = None


class VersionClassifyFunctionVersionClassificationRegex(BaseModel):
    patterns: Optional[List[str]] = None


class VersionClassifyFunctionVersionClassification(BaseModel):
    name: str

    description: Optional[str] = None

    function_id: Optional[str] = FieldInfo(alias="functionID", default=None)

    function_name: Optional[str] = FieldInfo(alias="functionName", default=None)

    is_error_fallback: Optional[bool] = FieldInfo(alias="isErrorFallback", default=None)

    origin: Optional[VersionClassifyFunctionVersionClassificationOrigin] = None

    regex: Optional[VersionClassifyFunctionVersionClassificationRegex] = None


class VersionClassifyFunctionVersion(BaseModel):
    """
    V3 read-side shape of a Classify (internally Route) function version.
    Mirrors {
    """

    classifications: List[VersionClassifyFunctionVersionClassification]
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
    """Audit trail information for the function version."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time the function version was created."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class VersionSendFunctionVersion(BaseModel):
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
    """Audit trail information for the function version."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time the function version was created."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    google_drive_folder_id: Optional[str] = FieldInfo(alias="googleDriveFolderId", default=None)

    s3_bucket: Optional[str] = FieldInfo(alias="s3Bucket", default=None)

    s3_prefix: Optional[str] = FieldInfo(alias="s3Prefix", default=None)

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""

    webhook_signing_enabled: Optional[bool] = FieldInfo(alias="webhookSigningEnabled", default=None)
    """
    Whether webhook deliveries are signed with an HMAC-SHA256 `bem-signature`
    header.
    """

    webhook_url: Optional[str] = FieldInfo(alias="webhookUrl", default=None)


class VersionSplitFunctionVersionPrintPageSplitConfig(BaseModel):
    next_function_id: Optional[str] = FieldInfo(alias="nextFunctionID", default=None)


class VersionSplitFunctionVersionSemanticPageSplitConfig(BaseModel):
    item_classes: Optional[List[SplitFunctionSemanticPageItemClass]] = FieldInfo(alias="itemClasses", default=None)


class VersionSplitFunctionVersion(BaseModel):
    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    split_type: Literal["print_page", "semantic_page"] = FieldInfo(alias="splitType")

    type: Literal["split"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function version."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time the function version was created."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    print_page_split_config: Optional[VersionSplitFunctionVersionPrintPageSplitConfig] = FieldInfo(
        alias="printPageSplitConfig", default=None
    )

    semantic_page_split_config: Optional[VersionSplitFunctionVersionSemanticPageSplitConfig] = FieldInfo(
        alias="semanticPageSplitConfig", default=None
    )

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class VersionJoinFunctionVersion(BaseModel):
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
    """Audit trail information for the function version."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time the function version was created."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class VersionEnrichFunctionVersion(BaseModel):
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
    """Audit trail information for the function version."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time the function version was created."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class VersionPayloadShapingFunctionVersion(BaseModel):
    """
    A version of a payload shaping function that transforms and customizes input payloads using JMESPath expressions.
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
    """Audit trail information for the function version."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time the function version was created."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


Version: TypeAlias = Annotated[
    Union[
        VersionTransformFunctionVersion,
        VersionExtractFunctionVersion,
        VersionAnalyzeFunctionVersion,
        VersionClassifyFunctionVersion,
        VersionSendFunctionVersion,
        VersionSplitFunctionVersion,
        VersionJoinFunctionVersion,
        VersionEnrichFunctionVersion,
        VersionPayloadShapingFunctionVersion,
    ],
    PropertyInfo(discriminator="type"),
]


class VersionListResponse(BaseModel):
    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
    """The total number of results available."""

    versions: Optional[List[Version]] = None
