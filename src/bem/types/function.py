# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .parse_config import ParseConfig
from .enrich_config import EnrichConfig
from .function_audit import FunctionAudit
from .workflow_usage_info import WorkflowUsageInfo
from .send_destination_type import SendDestinationType
from .classification_list_item import ClassificationListItem
from .split_function_semantic_page_item_class import SplitFunctionSemanticPageItemClass

__all__ = [
    "Function",
    "TransformFunction",
    "ExtractFunction",
    "AnalyzeFunction",
    "ClassifyFunction",
    "SendFunction",
    "SplitFunction",
    "SplitFunctionPrintPageSplitConfig",
    "SplitFunctionSemanticPageSplitConfig",
    "JoinFunction",
    "PayloadShapingFunction",
    "EnrichFunction",
    "ParseFunction",
    "ParseFunctionExtraConfig",
    "RenderFunction",
    "RenderFunctionRenderConfig",
    "RenderFunctionRenderConfigTemplate",
    "RenderFunctionRenderConfigTemplatePlaceholders",
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

    enable_bounding_boxes: bool = FieldInfo(alias="enableBoundingBoxes")
    """Whether bounding box extraction is enabled.

    Applies to vision input types (pdf, png, jpeg, heic, heif, webp) that dispatch
    through the analyze path. When true, the function returns the document regions
    (page, coordinates) from which each field was extracted.
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


class ClassifyFunction(BaseModel):
    classifications: List[ClassificationListItem]
    """List of classifications a classify function can produce.

    Shares the underlying route list shape.
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

    destination_type: SendDestinationType = FieldInfo(alias="destinationType")
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


class ParseFunctionExtraConfig(BaseModel):
    """Cross-cutting toggles for Parse functions.

    Mirrors the `extraConfig`
    surface on Extract / Join — separated from `parseConfig` so the per-call
    Parse output shape stays distinct from operator-level execution flags.
    """

    enable_bounding_boxes: Optional[bool] = FieldInfo(alias="enableBoundingBoxes", default=None)
    """
    When true, return per-section and per-entity-mention coordinates in the parse
    event's `fieldBoundingBoxes` map (same shape as Extract: JSON Pointer key →
    array of `{page, left, top, width, height}` with coordinates normalized to [0,
    1]). Keys are `/sections/{N}` and `/entities/{N}/occurrences/{M}` into the parse
    output. Only applies to the open-ended discovery path (no `schema`) and to
    vision input types. Bedrock-backed parse functions silently return an empty map
    (no native bbox support). Defaults to false.
    """


class ParseFunction(BaseModel):
    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Literal["parse"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    extra_config: Optional[ParseFunctionExtraConfig] = FieldInfo(alias="extraConfig", default=None)
    """Cross-cutting toggles for Parse functions.

    Mirrors the `extraConfig` surface on Extract / Join — separated from
    `parseConfig` so the per-call Parse output shape stays distinct from
    operator-level execution flags.
    """

    parse_config: Optional[ParseConfig] = FieldInfo(alias="parseConfig", default=None)
    """Per-version configuration for a Parse function.

    Parse renders document pages (PDF, image) via vision LLM and emits structured
    JSON. The two toggles below independently control entity extraction (a per-call
    output concern) and cross-document memory linking (an environment-wide concern).
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class RenderFunctionRenderConfigTemplatePlaceholders(BaseModel):
    """
    The placeholder contract a Render template declares, grouped by how each
    placeholder is filled. Derived from the template at create/update time by
    scanning its `docxtpl` tags; not user-supplied.

    - `stringKeys`: bare string placeholders (`{{ key }}`) filled with a single
    value.
    - `blockKeys`: wrapped-primitive placeholders (`{{p key }}`) — bind one core
    primitive (paragraph, table, image, or list). The placeholder's own
    paragraph dissolves and is replaced by the rendered subdocument's blocks,
    rather than substituting text inline.
    """

    block_keys: List[str] = FieldInfo(alias="blockKeys")

    string_keys: List[str] = FieldInfo(alias="stringKeys")


class RenderFunctionRenderConfigTemplate(BaseModel):
    """
    The uploaded template: its filename, a short-lived presigned download URL,
    and the placeholder/style contract derived from it. Absent on configs
    created before template capture existed.
    """

    download_url: Optional[str] = FieldInfo(alias="downloadURL", default=None)
    """Short-lived presigned URL to download the stored `.docx`.

    The private storage location is never exposed.
    """

    list_kinds: Optional[List[Literal["decimal", "bullet"]]] = FieldInfo(alias="listKinds", default=None)
    """
    Supported list kinds (`decimal`, `bullet`) the template's `numbering.xml`
    defines an `abstractNum` for. Empty means the template can hold no list, so any
    list primitive will fail at render.
    """

    name: Optional[str] = None
    """Original filename of the uploaded template (e.g.

    `contract.docx`), echoed back for display. Absent on templates uploaded before
    the filename was captured.
    """

    placeholders: Optional[RenderFunctionRenderConfigTemplatePlaceholders] = None
    """
    The placeholder contract a Render template declares, grouped by how each
    placeholder is filled. Derived from the template at create/update time by
    scanning its `docxtpl` tags; not user-supplied.

    - `stringKeys`: bare string placeholders (`{{ key }}`) filled with a single
      value.
    - `blockKeys`: wrapped-primitive placeholders (`{{p key }}`) — bind one core
      primitive (paragraph, table, image, or list). The placeholder's own paragraph
      dissolves and is replaced by the rendered subdocument's blocks, rather than
      substituting text inline.
    """

    style_ids: Optional[List[str]] = FieldInfo(alias="styleIds", default=None)
    """
    Paragraph/character style IDs the uploaded template defines and the rendered
    output can reference. Derived from the template's `styles.xml` at create/update
    time.
    """

    table_style_ids: Optional[List[str]] = FieldInfo(alias="tableStyleIds", default=None)
    """
    Style IDs whose type is table — the styles a `table` primitive's required
    `styleId` can name. Empty means the template defines no table style, so any
    table primitive will fail at render.
    """


class RenderFunctionRenderConfig(BaseModel):
    """Per-version configuration for a Render function.

    Render emits a `.docx` from schema-typed JSON by composing the JSON into a
    `.docx` template. The template document is stored server-side; this response
    exposes only the contract derived from it. Schema validation runs internally
    in the ML service against the bundled core schema; no customer-supplied
    schema rides this surface.
    """

    template: Optional[RenderFunctionRenderConfigTemplate] = None
    """
    The uploaded template: its filename, a short-lived presigned download URL, and
    the placeholder/style contract derived from it. Absent on configs created before
    template capture existed.
    """


class RenderFunction(BaseModel):
    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    type: Literal["render"]

    version_num: int = FieldInfo(alias="versionNum")
    """Version number of function."""

    audit: Optional[FunctionAudit] = None
    """Audit trail information for the function."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    render_config: Optional[RenderFunctionRenderConfig] = FieldInfo(alias="renderConfig", default=None)
    """Per-version configuration for a Render function.

    Render emits a `.docx` from schema-typed JSON by composing the JSON into a
    `.docx` template. The template document is stored server-side; this response
    exposes only the contract derived from it. Schema validation runs internally in
    the ML service against the bundled core schema; no customer-supplied schema
    rides this surface.
    """

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


Function: TypeAlias = Annotated[
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
        ParseFunction,
        RenderFunction,
    ],
    PropertyInfo(discriminator="type"),
]
