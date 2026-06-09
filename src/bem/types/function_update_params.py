# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .parse_config_param import ParseConfigParam
from .enrich_config_param import EnrichConfigParam
from .send_destination_type import SendDestinationType
from .classification_list_item_param import ClassificationListItemParam
from .split_function_semantic_page_item_class_param import SplitFunctionSemanticPageItemClassParam

__all__ = [
    "FunctionUpdateParams",
    "UpsertExtractFunction",
    "UpsertClassifyFunction",
    "UpsertSendFunction",
    "UpsertSplitFunction",
    "UpsertSplitFunctionPrintPageSplitConfig",
    "UpsertSplitFunctionSemanticPageSplitConfig",
    "UpsertJoinFunction",
    "UpsertPayloadShapingFunction",
    "UpsertEnrichFunction",
    "UpsertParseFunction",
    "UpsertParseFunctionExtraConfig",
]


class UpsertExtractFunction(TypedDict, total=False):
    type: Required[Literal["extract"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    enable_bounding_boxes: Annotated[bool, PropertyInfo(alias="enableBoundingBoxes")]
    """Whether bounding box extraction is enabled.

    Applies to vision input types (pdf, png, jpeg, heic, heif, webp) that dispatch
    through the analyze path. When true, the function returns the document regions
    (page, coordinates) from which each field was extracted. Enabling this
    automatically configures the function to use the bounding box model. Disabling
    resets to the default.
    """

    function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    output_schema: Annotated[object, PropertyInfo(alias="outputSchema")]
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: Annotated[str, PropertyInfo(alias="outputSchemaName")]
    """Name of output schema object."""

    pre_count: Annotated[bool, PropertyInfo(alias="preCount")]
    """
    Reducing the risk of the model stopping early on long documents. Trade-off:
    Increases total latency. Compatible with `enableBoundingBoxes`.
    """

    tabular_chunking_enabled: Annotated[bool, PropertyInfo(alias="tabularChunkingEnabled")]
    """Whether tabular chunking is enabled.

    When true, tables in CSV/Excel files are processed in row batches rather than
    all at once.
    """

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class UpsertClassifyFunction(TypedDict, total=False):
    type: Required[Literal["classify"]]

    classifications: Iterable[ClassificationListItemParam]
    """List of classifications a classify function can produce.

    Shares the underlying route list shape.
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

    function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class UpsertSendFunction(TypedDict, total=False):
    type: Required[Literal["send"]]

    destination_type: Annotated[SendDestinationType, PropertyInfo(alias="destinationType")]
    """Destination type for a Send function."""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Name of function. Must be UNIQUE on a per-environment basis."""

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


class UpsertSplitFunction(TypedDict, total=False):
    type: Required[Literal["split"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    print_page_split_config: Annotated[
        UpsertSplitFunctionPrintPageSplitConfig, PropertyInfo(alias="printPageSplitConfig")
    ]

    semantic_page_split_config: Annotated[
        UpsertSplitFunctionSemanticPageSplitConfig, PropertyInfo(alias="semanticPageSplitConfig")
    ]

    split_type: Annotated[Literal["print_page", "semantic_page"], PropertyInfo(alias="splitType")]

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class UpsertSplitFunctionPrintPageSplitConfig(TypedDict, total=False):
    next_function_id: Annotated[str, PropertyInfo(alias="nextFunctionID")]

    next_function_name: Annotated[str, PropertyInfo(alias="nextFunctionName")]


class UpsertSplitFunctionSemanticPageSplitConfig(TypedDict, total=False):
    item_classes: Annotated[Iterable[SplitFunctionSemanticPageItemClassParam], PropertyInfo(alias="itemClasses")]


class UpsertJoinFunction(TypedDict, total=False):
    type: Required[Literal["join"]]

    description: str
    """Description of join function."""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    join_type: Annotated[Literal["standard"], PropertyInfo(alias="joinType")]
    """The type of join to perform."""

    output_schema: Annotated[object, PropertyInfo(alias="outputSchema")]
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: Annotated[str, PropertyInfo(alias="outputSchemaName")]
    """Name of output schema object."""

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class UpsertPayloadShapingFunction(TypedDict, total=False):
    type: Required[Literal["payload_shaping"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Name of function. Must be UNIQUE on a per-environment basis."""

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


class UpsertEnrichFunction(TypedDict, total=False):
    type: Required[Literal["enrich"]]

    config: EnrichConfigParam
    """Configuration for an enrich function.

    **How Enrich Functions Work:**

    Enrich functions augment JSON input with data from external sources. They take
    JSON input (typically from a previous function), extract specified fields, fetch
    or search for matching data, and inject the results back into the JSON.

    **Data Sources:**

    - **Collections** (`source: "collection"`): Vector/keyword search against a BEM
      collection. Best for semantic matching against pre-indexed documents.
    - **Endpoints** (`source: "endpoint"`): HTTP call to any user-provided REST API.
      Best for looking up live data from CRMs, ERPs, or other external systems.
      Optionally uses LLM agent reasoning to rank candidates returned by the
      endpoint.

    **Input Requirements:**

    - Must receive JSON input (typically from a previous function's output)

    **Example Use Cases:**

    - Match product descriptions to SKU codes from a product catalog collection
    - Enrich customer data with account details from a CRM endpoint
    - Use LLM agent reasoning to fuzzy-match line item descriptions to catalog
      products

    **Configuration:**

    - Define named endpoints (for endpoint-source steps)
    - Define one or more enrichment steps; steps are executed sequentially
    """


class UpsertParseFunction(TypedDict, total=False):
    type: Required[Literal["parse"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    extra_config: Annotated[UpsertParseFunctionExtraConfig, PropertyInfo(alias="extraConfig")]
    """Cross-cutting toggles for Parse functions.

    Mirrors the `extraConfig` surface on Extract / Join — separated from
    `parseConfig` so the per-call Parse output shape stays distinct from
    operator-level execution flags.
    """

    function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    parse_config: Annotated[ParseConfigParam, PropertyInfo(alias="parseConfig")]
    """Per-version configuration for a Parse function.

    Parse renders document pages (PDF, image) via vision LLM and emits structured
    JSON. The two toggles below independently control entity extraction (a per-call
    output concern) and cross-document memory linking (an environment-wide concern).
    """

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class UpsertParseFunctionExtraConfig(TypedDict, total=False):
    """Cross-cutting toggles for Parse functions.

    Mirrors the `extraConfig`
    surface on Extract / Join — separated from `parseConfig` so the per-call
    Parse output shape stays distinct from operator-level execution flags.
    """

    enable_bounding_boxes: Annotated[bool, PropertyInfo(alias="enableBoundingBoxes")]
    """
    When true, return per-section and per-entity-mention coordinates in the parse
    event's `fieldBoundingBoxes` map (same shape as Extract: JSON Pointer key →
    array of `{page, left, top, width, height}` with coordinates normalized to [0,
    1]). Keys are `/sections/{N}` and `/entities/{N}/occurrences/{M}` into the parse
    output. Only applies to the open-ended discovery path (no `schema`) and to
    vision input types. Bedrock-backed parse functions silently return an empty map
    (no native bbox support). Defaults to false.
    """


FunctionUpdateParams: TypeAlias = Union[
    UpsertExtractFunction,
    UpsertClassifyFunction,
    UpsertSendFunction,
    UpsertSplitFunction,
    UpsertJoinFunction,
    UpsertPayloadShapingFunction,
    UpsertEnrichFunction,
    UpsertParseFunction,
]
