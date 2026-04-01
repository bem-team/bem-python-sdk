# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .enrich_config_param import EnrichConfigParam
from .route_list_item_param import RouteListItemParam
from .split_function_semantic_page_item_class_param import SplitFunctionSemanticPageItemClassParam

__all__ = [
    "FunctionUpdateParams",
    "UpsertTransformFunction",
    "UpsertAnalyzeFunction",
    "UpsertRouteFunction",
    "UpsertSplitFunction",
    "UpsertSplitFunctionPrintPageSplitConfig",
    "UpsertSplitFunctionSemanticPageSplitConfig",
    "UpsertJoinFunction",
    "UpsertPayloadShapingFunction",
    "UpsertEnrichFunction",
]


class UpsertTransformFunction(TypedDict, total=False):
    type: Required[Literal["transform"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    body_function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    output_schema: Annotated[object, PropertyInfo(alias="outputSchema")]
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: Annotated[str, PropertyInfo(alias="outputSchemaName")]
    """Name of output schema object."""

    tabular_chunking_enabled: Annotated[bool, PropertyInfo(alias="tabularChunkingEnabled")]
    """Whether tabular chunking is enabled on the pipeline.

    This processes tables in CSV/Excel in row batches, rather than all rows at once.
    """

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class UpsertAnalyzeFunction(TypedDict, total=False):
    type: Required[Literal["analyze"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    body_function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    output_schema: Annotated[object, PropertyInfo(alias="outputSchema")]
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: Annotated[str, PropertyInfo(alias="outputSchemaName")]
    """Name of output schema object."""

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class UpsertRouteFunction(TypedDict, total=False):
    type: Required[Literal["route"]]

    description: str
    """Description of router.

    Can be used to provide additional context on router's purpose and expected
    inputs.
    """

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    body_function_name: Annotated[str, PropertyInfo(alias="functionName")]
    """Name of function. Must be UNIQUE on a per-environment basis."""

    routes: Iterable[RouteListItemParam]
    """List of routes."""

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize functions."""


class UpsertSplitFunction(TypedDict, total=False):
    type: Required[Literal["split"]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of function.

    Human-readable name to help you identify the function.
    """

    body_function_name: Annotated[str, PropertyInfo(alias="functionName")]
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

    body_function_name: Annotated[str, PropertyInfo(alias="functionName")]
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

    body_function_name: Annotated[str, PropertyInfo(alias="functionName")]
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


FunctionUpdateParams: TypeAlias = Union[
    UpsertTransformFunction,
    UpsertAnalyzeFunction,
    UpsertRouteFunction,
    UpsertSplitFunction,
    UpsertJoinFunction,
    UpsertPayloadShapingFunction,
    UpsertEnrichFunction,
]
