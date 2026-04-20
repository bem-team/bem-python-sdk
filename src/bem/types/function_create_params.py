# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .enrich_config_param import EnrichConfigParam
from .split_function_semantic_page_item_class_param import SplitFunctionSemanticPageItemClassParam

__all__ = [
    "FunctionCreateParams",
    "CreateExtractFunction",
    "CreateClassifyFunction",
    "CreateClassifyFunctionClassification",
    "CreateClassifyFunctionClassificationOrigin",
    "CreateClassifyFunctionClassificationOriginEmail",
    "CreateClassifyFunctionClassificationRegex",
    "CreateSendFunction",
    "CreateSplitFunction",
    "CreateSplitFunctionPrintPageSplitConfig",
    "CreateSplitFunctionSemanticPageSplitConfig",
    "CreateJoinFunction",
    "CreatePayloadShapingFunction",
    "CreateEnrichFunction",
]


class CreateExtractFunction(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Required[Literal["extract"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    output_schema: Annotated[object, PropertyInfo(alias="outputSchema")]
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: Annotated[str, PropertyInfo(alias="outputSchemaName")]
    """Name of output schema object."""

    tabular_chunking_enabled: Annotated[bool, PropertyInfo(alias="tabularChunkingEnabled")]
    """Whether tabular chunking is enabled.

    When true, tables in CSV/Excel files are processed in row batches rather than
    all at once.
    """

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class CreateClassifyFunction(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Required[Literal["classify"]]

    classifications: Iterable[CreateClassifyFunctionClassification]
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

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class CreateClassifyFunctionClassificationOriginEmail(TypedDict, total=False):
    patterns: SequenceNotStr[str]


class CreateClassifyFunctionClassificationOrigin(TypedDict, total=False):
    email: CreateClassifyFunctionClassificationOriginEmail


class CreateClassifyFunctionClassificationRegex(TypedDict, total=False):
    patterns: SequenceNotStr[str]


class CreateClassifyFunctionClassification(TypedDict, total=False):
    name: Required[str]

    description: str

    function_id: Annotated[str, PropertyInfo(alias="functionID")]

    function_name: Annotated[str, PropertyInfo(alias="functionName")]

    is_error_fallback: Annotated[bool, PropertyInfo(alias="isErrorFallback")]

    origin: CreateClassifyFunctionClassificationOrigin

    regex: CreateClassifyFunctionClassificationRegex


class CreateSendFunction(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Required[Literal["send"]]

    destination_type: Annotated[Literal["webhook", "s3", "google_drive"], PropertyInfo(alias="destinationType")]
    """Destination type for a Send function."""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    google_drive_folder_id: Annotated[str, PropertyInfo(alias="googleDriveFolderId")]
    """Google Drive folder ID.

    Required when destinationType is google_drive. Managed via Paragon OAuth.
    """

    s3_bucket: Annotated[str, PropertyInfo(alias="s3Bucket")]
    """S3 bucket to upload the payload to. Required when destinationType is s3."""

    s3_prefix: Annotated[str, PropertyInfo(alias="s3Prefix")]
    """Optional S3 key prefix (folder path)."""

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""

    webhook_signing_enabled: Annotated[bool, PropertyInfo(alias="webhookSigningEnabled")]
    """
    Whether to sign webhook deliveries with an HMAC-SHA256 `bem-signature` header.
    Defaults to `true` when omitted — signing is on by default for new send
    functions. Set explicitly to `false` to disable.
    """

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """Webhook URL to POST the payload to. Required when destinationType is webhook."""


class CreateSplitFunction(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Required[Literal["split"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    print_page_split_config: Annotated[
        CreateSplitFunctionPrintPageSplitConfig, PropertyInfo(alias="printPageSplitConfig")
    ]

    semantic_page_split_config: Annotated[
        CreateSplitFunctionSemanticPageSplitConfig, PropertyInfo(alias="semanticPageSplitConfig")
    ]

    split_type: Annotated[Literal["print_page", "semantic_page"], PropertyInfo(alias="splitType")]

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class CreateSplitFunctionPrintPageSplitConfig(TypedDict, total=False):
    next_function_id: Annotated[str, PropertyInfo(alias="nextFunctionID")]

    next_function_name: Annotated[str, PropertyInfo(alias="nextFunctionName")]


class CreateSplitFunctionSemanticPageSplitConfig(TypedDict, total=False):
    item_classes: Annotated[Iterable[SplitFunctionSemanticPageItemClassParam], PropertyInfo(alias="itemClasses")]


class CreateJoinFunction(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Required[Literal["join"]]

    description: str
    """Description of join function."""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    join_type: Annotated[Literal["standard"], PropertyInfo(alias="joinType")]
    """The type of join to perform."""

    output_schema: Annotated[object, PropertyInfo(alias="outputSchema")]
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: Annotated[str, PropertyInfo(alias="outputSchemaName")]
    """Name of output schema object."""

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class CreatePayloadShapingFunction(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Required[Literal["payload_shaping"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    shaping_schema: Annotated[str, PropertyInfo(alias="shapingSchema")]
    """
    JMESPath expression that defines how to transform and customize the input
    payload structure. Payload shaping allows you to extract, reshape, and
    reorganize data from complex input payloads into a simplified, standardized
    output format. Use JMESPath syntax to select specific fields, perform
    calculations, and create new data structures tailored to your needs.
    """

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class CreateEnrichFunction(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Required[Literal["enrich"]]

    config: EnrichConfigParam
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

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


FunctionCreateParams: TypeAlias = Union[
    CreateExtractFunction,
    CreateClassifyFunction,
    CreateSendFunction,
    CreateSplitFunction,
    CreateJoinFunction,
    CreatePayloadShapingFunction,
    CreateEnrichFunction,
]
