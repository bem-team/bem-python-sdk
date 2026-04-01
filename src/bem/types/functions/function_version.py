# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..enrich_config import EnrichConfig
from ..function_audit import FunctionAudit
from ..route_list_item import RouteListItem
from ..workflow_usage_info import WorkflowUsageInfo
from ..split_function_semantic_page_item_class import SplitFunctionSemanticPageItemClass

__all__ = [
    "FunctionVersion",
    "TransformFunctionVersion",
    "AnalyzeFunctionVersion",
    "RouteFunctionVersion",
    "SplitFunctionVersion",
    "SplitFunctionVersionPrintPageSplitConfig",
    "SplitFunctionVersionSemanticPageSplitConfig",
    "JoinFunctionVersion",
    "EnrichFunctionVersion",
    "PayloadShapingFunctionVersion",
]


class TransformFunctionVersion(BaseModel):
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


class AnalyzeFunctionVersion(BaseModel):
    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    output_schema: object = FieldInfo(alias="outputSchema")
    """Desired output structure defined in standard JSON Schema convention."""

    output_schema_name: str = FieldInfo(alias="outputSchemaName")
    """Name of output schema object."""

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


class RouteFunctionVersion(BaseModel):
    description: str
    """Description of router.

    Can be used to provide additional context on router's purpose and expected
    inputs.
    """

    email_address: str = FieldInfo(alias="emailAddress")
    """Email address automatically created by bem.

    You can forward emails with or without attachments, to be routed.
    """

    function_id: str = FieldInfo(alias="functionID")
    """Unique identifier of function."""

    function_name: str = FieldInfo(alias="functionName")
    """Name of function. Must be UNIQUE on a per-environment basis."""

    routes: List[RouteListItem]
    """List of routes."""

    type: Literal["route"]

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


class SplitFunctionVersionPrintPageSplitConfig(BaseModel):
    next_function_id: Optional[str] = FieldInfo(alias="nextFunctionID", default=None)


class SplitFunctionVersionSemanticPageSplitConfig(BaseModel):
    item_classes: Optional[List[SplitFunctionSemanticPageItemClass]] = FieldInfo(alias="itemClasses", default=None)


class SplitFunctionVersion(BaseModel):
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

    print_page_split_config: Optional[SplitFunctionVersionPrintPageSplitConfig] = FieldInfo(
        alias="printPageSplitConfig", default=None
    )

    semantic_page_split_config: Optional[SplitFunctionVersionSemanticPageSplitConfig] = FieldInfo(
        alias="semanticPageSplitConfig", default=None
    )

    tags: Optional[List[str]] = None
    """Array of tags to categorize and organize functions."""

    used_in_workflows: Optional[List[WorkflowUsageInfo]] = FieldInfo(alias="usedInWorkflows", default=None)
    """List of workflows that use this function."""


class JoinFunctionVersion(BaseModel):
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


class EnrichFunctionVersion(BaseModel):
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


class PayloadShapingFunctionVersion(BaseModel):
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


FunctionVersion: TypeAlias = Annotated[
    Union[
        TransformFunctionVersion,
        AnalyzeFunctionVersion,
        RouteFunctionVersion,
        SplitFunctionVersion,
        JoinFunctionVersion,
        EnrichFunctionVersion,
        PayloadShapingFunctionVersion,
    ],
    PropertyInfo(discriminator="type"),
]
