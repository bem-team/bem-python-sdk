# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Iterable, cast
from typing_extensions import Literal, overload

import httpx

from .copy import (
    CopyResource,
    AsyncCopyResource,
    CopyResourceWithRawResponse,
    AsyncCopyResourceWithRawResponse,
    CopyResourceWithStreamingResponse,
    AsyncCopyResourceWithStreamingResponse,
)
from ...types import function_list_params, function_create_params, function_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncFunctionsPage, AsyncFunctionsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.function import Function
from ...types.function_type import FunctionType
from ...types.function_response import FunctionResponse
from ...types.enrich_config_param import EnrichConfigParam
from ...types.classification_list_item_param import ClassificationListItemParam

__all__ = ["FunctionsResource", "AsyncFunctionsResource"]


class FunctionsResource(SyncAPIResource):
    """Functions are the core building blocks of data transformation in Bem.

    Each function type serves a specific purpose:

    - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
    - **Route**: Direct data to different processing paths based on conditions
    - **Split**: Break multi-page documents into individual pages for parallel processing
    - **Join**: Combine outputs from multiple function calls into a single result
    - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
    - **Payload Shaping**: Transform and restructure data using JMESPath expressions
    - **Enrich**: Enhance data with semantic search against collections
    - **Send**: Deliver workflow outputs to downstream destinations

    Use these endpoints to create, update, list, and manage your functions.
    """

    @cached_property
    def copy(self) -> CopyResource:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return CopyResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return FunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return FunctionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        function_name: str,
        type: Literal["extract"],
        display_name: str | Omit = omit,
        enable_bounding_boxes: bool | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        pre_count: bool | Omit = omit,
        tabular_chunking_enabled: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          display_name: Display name of function. Human-readable name to help you identify the function.

          enable_bounding_boxes: Whether bounding box extraction is enabled. Applies to vision input types (pdf,
              png, jpeg, heic, heif, webp) that dispatch through the analyze path. When true,
              the function returns the document regions (page, coordinates) from which each
              field was extracted. Enabling this automatically configures the function to use
              the bounding box model. Disabling resets to the default.

          output_schema: Desired output structure defined in standard JSON Schema convention.

          output_schema_name: Name of output schema object.

          pre_count:
              Reducing the risk of the model stopping early on long documents. Trade-off:
              Increases total latency. Compatible with `enableBoundingBoxes`.

          tabular_chunking_enabled: Whether tabular chunking is enabled. When true, tables in CSV/Excel files are
              processed in row batches rather than all at once.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        function_name: str,
        type: Literal["classify"],
        classifications: Iterable[ClassificationListItemParam] | Omit = omit,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          classifications: List of classifications a classify function can produce. Shares the underlying
              route list shape.

          description: Description of classifier. Can be used to provide additional context on
              classifier's purpose and expected inputs.

          display_name: Display name of function. Human-readable name to help you identify the function.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        function_name: str,
        type: Literal["send"],
        destination_type: Literal["webhook", "s3", "google_drive"] | Omit = omit,
        display_name: str | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_prefix: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_signing_enabled: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          destination_type: Destination type for a Send function.

          display_name: Display name of function. Human-readable name to help you identify the function.

          google_drive_folder_id: Google Drive folder ID. Required when destinationType is google_drive. Managed
              via Paragon OAuth.

          s3_bucket: S3 bucket to upload the payload to. Required when destinationType is s3.

          s3_prefix: Optional S3 key prefix (folder path).

          tags: Array of tags to categorize and organize functions.

          webhook_signing_enabled: Whether to sign webhook deliveries with an HMAC-SHA256 `bem-signature` header.
              Defaults to `true` when omitted — signing is on by default for new send
              functions. Set explicitly to `false` to disable.

          webhook_url: Webhook URL to POST the payload to. Required when destinationType is webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        function_name: str,
        type: Literal["split"],
        display_name: str | Omit = omit,
        print_page_split_config: function_create_params.CreateSplitFunctionPrintPageSplitConfig | Omit = omit,
        semantic_page_split_config: function_create_params.CreateSplitFunctionSemanticPageSplitConfig | Omit = omit,
        split_type: Literal["print_page", "semantic_page"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          display_name: Display name of function. Human-readable name to help you identify the function.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        function_name: str,
        type: Literal["join"],
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        join_type: Literal["standard"] | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          description: Description of join function.

          display_name: Display name of function. Human-readable name to help you identify the function.

          join_type: The type of join to perform.

          output_schema: Desired output structure defined in standard JSON Schema convention.

          output_schema_name: Name of output schema object.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        function_name: str,
        type: Literal["payload_shaping"],
        display_name: str | Omit = omit,
        shaping_schema: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          display_name: Display name of function. Human-readable name to help you identify the function.

          shaping_schema: JMESPath expression that defines how to transform and customize the input
              payload structure. Payload shaping allows you to extract, reshape, and
              reorganize data from complex input payloads into a simplified, standardized
              output format. Use JMESPath syntax to select specific fields, perform
              calculations, and create new data structures tailored to your needs.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        function_name: str,
        type: Literal["enrich"],
        config: EnrichConfigParam | Omit = omit,
        display_name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          config: Configuration for enrich function with semantic search steps.

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

          display_name: Display name of function. Human-readable name to help you identify the function.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        function_name: str,
        type: Literal["parse"],
        display_name: str | Omit = omit,
        parse_config: function_create_params.CreateParseFunctionParseConfig | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          display_name: Display name of function. Human-readable name to help you identify the function.

          parse_config: Per-version configuration for a Parse function.

              Parse renders document pages (PDF, image) via vision LLM and emits structured
              JSON. The two toggles below independently control entity extraction (a per-call
              output concern) and cross-document memory linking (an environment-wide concern).

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["function_name", "type"])
    def create(
        self,
        *,
        function_name: str,
        type: Literal["extract"]
        | Literal["classify"]
        | Literal["send"]
        | Literal["split"]
        | Literal["join"]
        | Literal["payload_shaping"]
        | Literal["enrich"]
        | Literal["parse"],
        display_name: str | Omit = omit,
        enable_bounding_boxes: bool | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        pre_count: bool | Omit = omit,
        tabular_chunking_enabled: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        classifications: Iterable[ClassificationListItemParam] | Omit = omit,
        description: str | Omit = omit,
        destination_type: Literal["webhook", "s3", "google_drive"] | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_prefix: str | Omit = omit,
        webhook_signing_enabled: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        print_page_split_config: function_create_params.CreateSplitFunctionPrintPageSplitConfig | Omit = omit,
        semantic_page_split_config: function_create_params.CreateSplitFunctionSemanticPageSplitConfig | Omit = omit,
        split_type: Literal["print_page", "semantic_page"] | Omit = omit,
        join_type: Literal["standard"] | Omit = omit,
        shaping_schema: str | Omit = omit,
        config: EnrichConfigParam | Omit = omit,
        parse_config: function_create_params.CreateParseFunctionParseConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        return self._post(
            "/v3/functions",
            body=maybe_transform(
                {
                    "function_name": function_name,
                    "type": type,
                    "display_name": display_name,
                    "enable_bounding_boxes": enable_bounding_boxes,
                    "output_schema": output_schema,
                    "output_schema_name": output_schema_name,
                    "pre_count": pre_count,
                    "tabular_chunking_enabled": tabular_chunking_enabled,
                    "tags": tags,
                    "classifications": classifications,
                    "description": description,
                    "destination_type": destination_type,
                    "google_drive_folder_id": google_drive_folder_id,
                    "s3_bucket": s3_bucket,
                    "s3_prefix": s3_prefix,
                    "webhook_signing_enabled": webhook_signing_enabled,
                    "webhook_url": webhook_url,
                    "print_page_split_config": print_page_split_config,
                    "semantic_page_split_config": semantic_page_split_config,
                    "split_type": split_type,
                    "join_type": join_type,
                    "shaping_schema": shaping_schema,
                    "config": config,
                    "parse_config": parse_config,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionResponse,
        )

    def retrieve(
        self,
        function_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Retrieve a function's current version by name.**

        Returns the function record with its `currentVersionNum` and the configuration
        of that version. To inspect a historical version, use
        `GET /v3/functions/{functionName}/versions/{versionNum}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_name:
            raise ValueError(f"Expected a non-empty value for `function_name` but received {function_name!r}")
        return self._get(
            path_template("/v3/functions/{function_name}", function_name=function_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionResponse,
        )

    @overload
    def update(
        self,
        path_function_name: str,
        *,
        type: Literal["extract"],
        display_name: str | Omit = omit,
        enable_bounding_boxes: bool | Omit = omit,
        function_name: str | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        pre_count: bool | Omit = omit,
        tabular_chunking_enabled: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          display_name: Display name of function. Human-readable name to help you identify the function.

          enable_bounding_boxes: Whether bounding box extraction is enabled. Applies to vision input types (pdf,
              png, jpeg, heic, heif, webp) that dispatch through the analyze path. When true,
              the function returns the document regions (page, coordinates) from which each
              field was extracted. Enabling this automatically configures the function to use
              the bounding box model. Disabling resets to the default.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          output_schema: Desired output structure defined in standard JSON Schema convention.

          output_schema_name: Name of output schema object.

          pre_count:
              Reducing the risk of the model stopping early on long documents. Trade-off:
              Increases total latency. Compatible with `enableBoundingBoxes`.

          tabular_chunking_enabled: Whether tabular chunking is enabled. When true, tables in CSV/Excel files are
              processed in row batches rather than all at once.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        path_function_name: str,
        *,
        type: Literal["classify"],
        classifications: Iterable[ClassificationListItemParam] | Omit = omit,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          classifications: List of classifications a classify function can produce. Shares the underlying
              route list shape.

          description: Description of classifier. Can be used to provide additional context on
              classifier's purpose and expected inputs.

          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        path_function_name: str,
        *,
        type: Literal["send"],
        destination_type: Literal["webhook", "s3", "google_drive"] | Omit = omit,
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_prefix: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_signing_enabled: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          destination_type: Destination type for a Send function.

          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          google_drive_folder_id: Google Drive folder ID. Required when destinationType is google_drive. Managed
              via Paragon OAuth.

          s3_bucket: S3 bucket to upload the payload to. Required when destinationType is s3.

          s3_prefix: Optional S3 key prefix (folder path).

          tags: Array of tags to categorize and organize functions.

          webhook_signing_enabled: Whether to sign webhook deliveries with an HMAC-SHA256 `bem-signature` header.
              Defaults to `true` when omitted — signing is on by default for new send
              functions. Set explicitly to `false` to disable.

          webhook_url: Webhook URL to POST the payload to. Required when destinationType is webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        path_function_name: str,
        *,
        type: Literal["split"],
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        print_page_split_config: function_update_params.UpsertSplitFunctionPrintPageSplitConfig | Omit = omit,
        semantic_page_split_config: function_update_params.UpsertSplitFunctionSemanticPageSplitConfig | Omit = omit,
        split_type: Literal["print_page", "semantic_page"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        path_function_name: str,
        *,
        type: Literal["join"],
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        join_type: Literal["standard"] | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          description: Description of join function.

          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          join_type: The type of join to perform.

          output_schema: Desired output structure defined in standard JSON Schema convention.

          output_schema_name: Name of output schema object.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        path_function_name: str,
        *,
        type: Literal["payload_shaping"],
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        shaping_schema: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          shaping_schema: JMESPath expression that defines how to transform and customize the input
              payload structure. Payload shaping allows you to extract, reshape, and
              reorganize data from complex input payloads into a simplified, standardized
              output format. Use JMESPath syntax to select specific fields, perform
              calculations, and create new data structures tailored to your needs.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        path_function_name: str,
        *,
        type: Literal["enrich"],
        config: EnrichConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          config: Configuration for enrich function with semantic search steps.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        path_function_name: str,
        *,
        type: Literal["parse"],
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        parse_config: function_update_params.UpsertParseFunctionParseConfig | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          parse_config: Per-version configuration for a Parse function.

              Parse renders document pages (PDF, image) via vision LLM and emits structured
              JSON. The two toggles below independently control entity extraction (a per-call
              output concern) and cross-document memory linking (an environment-wide concern).

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"])
    def update(
        self,
        path_function_name: str,
        *,
        type: Literal["extract"]
        | Literal["classify"]
        | Literal["send"]
        | Literal["split"]
        | Literal["join"]
        | Literal["payload_shaping"]
        | Literal["enrich"]
        | Literal["parse"],
        display_name: str | Omit = omit,
        enable_bounding_boxes: bool | Omit = omit,
        function_name: str | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        pre_count: bool | Omit = omit,
        tabular_chunking_enabled: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        classifications: Iterable[ClassificationListItemParam] | Omit = omit,
        description: str | Omit = omit,
        destination_type: Literal["webhook", "s3", "google_drive"] | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_prefix: str | Omit = omit,
        webhook_signing_enabled: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        print_page_split_config: function_update_params.UpsertSplitFunctionPrintPageSplitConfig | Omit = omit,
        semantic_page_split_config: function_update_params.UpsertSplitFunctionSemanticPageSplitConfig | Omit = omit,
        split_type: Literal["print_page", "semantic_page"] | Omit = omit,
        join_type: Literal["standard"] | Omit = omit,
        shaping_schema: str | Omit = omit,
        config: EnrichConfigParam | Omit = omit,
        parse_config: function_update_params.UpsertParseFunctionParseConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        if not path_function_name:
            raise ValueError(f"Expected a non-empty value for `path_function_name` but received {path_function_name!r}")
        return self._patch(
            path_template("/v3/functions/{path_function_name}", path_function_name=path_function_name),
            body=maybe_transform(
                {
                    "type": type,
                    "display_name": display_name,
                    "enable_bounding_boxes": enable_bounding_boxes,
                    "function_name": function_name,
                    "output_schema": output_schema,
                    "output_schema_name": output_schema_name,
                    "pre_count": pre_count,
                    "tabular_chunking_enabled": tabular_chunking_enabled,
                    "tags": tags,
                    "classifications": classifications,
                    "description": description,
                    "destination_type": destination_type,
                    "google_drive_folder_id": google_drive_folder_id,
                    "s3_bucket": s3_bucket,
                    "s3_prefix": s3_prefix,
                    "webhook_signing_enabled": webhook_signing_enabled,
                    "webhook_url": webhook_url,
                    "print_page_split_config": print_page_split_config,
                    "semantic_page_split_config": semantic_page_split_config,
                    "split_type": split_type,
                    "join_type": join_type,
                    "shaping_schema": shaping_schema,
                    "config": config,
                    "parse_config": parse_config,
                },
                function_update_params.FunctionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionResponse,
        )

    def list(
        self,
        *,
        display_name: str | Omit = omit,
        ending_before: str | Omit = omit,
        function_ids: SequenceNotStr[str] | Omit = omit,
        function_names: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        types: List[FunctionType] | Omit = omit,
        workflow_ids: SequenceNotStr[str] | Omit = omit,
        workflow_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncFunctionsPage[Function]:
        """
        **List functions in the current environment.**

        Returns each function's current version. Combine filters freely — they AND
        together.

        ## Filtering

        - `functionIDs` / `functionNames`: exact-match identity filters.
        - `displayName`: case-insensitive substring match.
        - `types`: one or more of `extract`, `classify`, `split`, `join`, `enrich`,
          `payload_shaping`. Legacy `transform`, `analyze`, `route`, and `send` types
          remain readable via this filter.
        - `tags`: returns functions tagged with any of the supplied tags.
        - `workflowIDs` / `workflowNames`: returns only functions referenced by the
          named workflows. Useful for "what functions does this workflow depend on?"
          lookups.

        ## Pagination

        Cursor-based with `startingAfter` and `endingBefore` (functionIDs). Default
        limit 50, maximum 100.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/functions",
            page=SyncFunctionsPage[Function],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "display_name": display_name,
                        "ending_before": ending_before,
                        "function_ids": function_ids,
                        "function_names": function_names,
                        "limit": limit,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                        "tags": tags,
                        "types": types,
                        "workflow_ids": workflow_ids,
                        "workflow_names": workflow_names,
                    },
                    function_list_params.FunctionListParams,
                ),
            ),
            model=cast(Any, Function),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        function_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """**Delete a function and every one of its versions.**

        Permanent.

        Running and queued calls that reference this function continue to
        completion against the version they captured at call time, but no new calls can
        target it.

        ## Before deleting

        Workflow nodes that reference this function will fail at call time after
        deletion. List workflows that reference it first:

        ```
        GET /v3/workflows?functionNames=my-function
        ```

        Update or remove those workflows, or create a replacement function and re-point
        the workflow nodes, before deleting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_name:
            raise ValueError(f"Expected a non-empty value for `function_name` but received {function_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/functions/{function_name}", function_name=function_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFunctionsResource(AsyncAPIResource):
    """Functions are the core building blocks of data transformation in Bem.

    Each function type serves a specific purpose:

    - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
    - **Route**: Direct data to different processing paths based on conditions
    - **Split**: Break multi-page documents into individual pages for parallel processing
    - **Join**: Combine outputs from multiple function calls into a single result
    - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
    - **Payload Shaping**: Transform and restructure data using JMESPath expressions
    - **Enrich**: Enhance data with semantic search against collections
    - **Send**: Deliver workflow outputs to downstream destinations

    Use these endpoints to create, update, list, and manage your functions.
    """

    @cached_property
    def copy(self) -> AsyncCopyResource:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return AsyncCopyResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncFunctionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        function_name: str,
        type: Literal["extract"],
        display_name: str | Omit = omit,
        enable_bounding_boxes: bool | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        pre_count: bool | Omit = omit,
        tabular_chunking_enabled: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          display_name: Display name of function. Human-readable name to help you identify the function.

          enable_bounding_boxes: Whether bounding box extraction is enabled. Applies to vision input types (pdf,
              png, jpeg, heic, heif, webp) that dispatch through the analyze path. When true,
              the function returns the document regions (page, coordinates) from which each
              field was extracted. Enabling this automatically configures the function to use
              the bounding box model. Disabling resets to the default.

          output_schema: Desired output structure defined in standard JSON Schema convention.

          output_schema_name: Name of output schema object.

          pre_count:
              Reducing the risk of the model stopping early on long documents. Trade-off:
              Increases total latency. Compatible with `enableBoundingBoxes`.

          tabular_chunking_enabled: Whether tabular chunking is enabled. When true, tables in CSV/Excel files are
              processed in row batches rather than all at once.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        function_name: str,
        type: Literal["classify"],
        classifications: Iterable[ClassificationListItemParam] | Omit = omit,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          classifications: List of classifications a classify function can produce. Shares the underlying
              route list shape.

          description: Description of classifier. Can be used to provide additional context on
              classifier's purpose and expected inputs.

          display_name: Display name of function. Human-readable name to help you identify the function.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        function_name: str,
        type: Literal["send"],
        destination_type: Literal["webhook", "s3", "google_drive"] | Omit = omit,
        display_name: str | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_prefix: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_signing_enabled: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          destination_type: Destination type for a Send function.

          display_name: Display name of function. Human-readable name to help you identify the function.

          google_drive_folder_id: Google Drive folder ID. Required when destinationType is google_drive. Managed
              via Paragon OAuth.

          s3_bucket: S3 bucket to upload the payload to. Required when destinationType is s3.

          s3_prefix: Optional S3 key prefix (folder path).

          tags: Array of tags to categorize and organize functions.

          webhook_signing_enabled: Whether to sign webhook deliveries with an HMAC-SHA256 `bem-signature` header.
              Defaults to `true` when omitted — signing is on by default for new send
              functions. Set explicitly to `false` to disable.

          webhook_url: Webhook URL to POST the payload to. Required when destinationType is webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        function_name: str,
        type: Literal["split"],
        display_name: str | Omit = omit,
        print_page_split_config: function_create_params.CreateSplitFunctionPrintPageSplitConfig | Omit = omit,
        semantic_page_split_config: function_create_params.CreateSplitFunctionSemanticPageSplitConfig | Omit = omit,
        split_type: Literal["print_page", "semantic_page"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          display_name: Display name of function. Human-readable name to help you identify the function.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        function_name: str,
        type: Literal["join"],
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        join_type: Literal["standard"] | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          description: Description of join function.

          display_name: Display name of function. Human-readable name to help you identify the function.

          join_type: The type of join to perform.

          output_schema: Desired output structure defined in standard JSON Schema convention.

          output_schema_name: Name of output schema object.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        function_name: str,
        type: Literal["payload_shaping"],
        display_name: str | Omit = omit,
        shaping_schema: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          display_name: Display name of function. Human-readable name to help you identify the function.

          shaping_schema: JMESPath expression that defines how to transform and customize the input
              payload structure. Payload shaping allows you to extract, reshape, and
              reorganize data from complex input payloads into a simplified, standardized
              output format. Use JMESPath syntax to select specific fields, perform
              calculations, and create new data structures tailored to your needs.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        function_name: str,
        type: Literal["enrich"],
        config: EnrichConfigParam | Omit = omit,
        display_name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          config: Configuration for enrich function with semantic search steps.

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

          display_name: Display name of function. Human-readable name to help you identify the function.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        function_name: str,
        type: Literal["parse"],
        display_name: str | Omit = omit,
        parse_config: function_create_params.CreateParseFunctionParseConfig | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Create a function.**

        The function type (`extract`, `classify`, `split`, `join`, `enrich`, or
        `payload_shaping`) determines which configuration fields are required — see
        [Function types overview](/guide/function-types/overview) for the per-type
        contract.

        The response contains both `functionID` and `functionName`. Either is a stable
        handle you can use elsewhere; most workflows reference functions by
        `functionName` because it's human-readable.

        ## Naming rules

        - `functionName` must be unique per environment.
        - Allowed characters: letters, digits, hyphens, and underscores.
        - Names cannot be reused after deletion within the same environment for at least
          the retention window of the previous record.

        The new function is created at `versionNum: 1`. Subsequent
        `PATCH /v3/functions/{functionName}` calls produce new versions — the version-1
        configuration remains immutable and addressable.

        Args:
          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          display_name: Display name of function. Human-readable name to help you identify the function.

          parse_config: Per-version configuration for a Parse function.

              Parse renders document pages (PDF, image) via vision LLM and emits structured
              JSON. The two toggles below independently control entity extraction (a per-call
              output concern) and cross-document memory linking (an environment-wide concern).

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["function_name", "type"])
    async def create(
        self,
        *,
        function_name: str,
        type: Literal["extract"]
        | Literal["classify"]
        | Literal["send"]
        | Literal["split"]
        | Literal["join"]
        | Literal["payload_shaping"]
        | Literal["enrich"]
        | Literal["parse"],
        display_name: str | Omit = omit,
        enable_bounding_boxes: bool | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        pre_count: bool | Omit = omit,
        tabular_chunking_enabled: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        classifications: Iterable[ClassificationListItemParam] | Omit = omit,
        description: str | Omit = omit,
        destination_type: Literal["webhook", "s3", "google_drive"] | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_prefix: str | Omit = omit,
        webhook_signing_enabled: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        print_page_split_config: function_create_params.CreateSplitFunctionPrintPageSplitConfig | Omit = omit,
        semantic_page_split_config: function_create_params.CreateSplitFunctionSemanticPageSplitConfig | Omit = omit,
        split_type: Literal["print_page", "semantic_page"] | Omit = omit,
        join_type: Literal["standard"] | Omit = omit,
        shaping_schema: str | Omit = omit,
        config: EnrichConfigParam | Omit = omit,
        parse_config: function_create_params.CreateParseFunctionParseConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        return await self._post(
            "/v3/functions",
            body=await async_maybe_transform(
                {
                    "function_name": function_name,
                    "type": type,
                    "display_name": display_name,
                    "enable_bounding_boxes": enable_bounding_boxes,
                    "output_schema": output_schema,
                    "output_schema_name": output_schema_name,
                    "pre_count": pre_count,
                    "tabular_chunking_enabled": tabular_chunking_enabled,
                    "tags": tags,
                    "classifications": classifications,
                    "description": description,
                    "destination_type": destination_type,
                    "google_drive_folder_id": google_drive_folder_id,
                    "s3_bucket": s3_bucket,
                    "s3_prefix": s3_prefix,
                    "webhook_signing_enabled": webhook_signing_enabled,
                    "webhook_url": webhook_url,
                    "print_page_split_config": print_page_split_config,
                    "semantic_page_split_config": semantic_page_split_config,
                    "split_type": split_type,
                    "join_type": join_type,
                    "shaping_schema": shaping_schema,
                    "config": config,
                    "parse_config": parse_config,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionResponse,
        )

    async def retrieve(
        self,
        function_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """
        **Retrieve a function's current version by name.**

        Returns the function record with its `currentVersionNum` and the configuration
        of that version. To inspect a historical version, use
        `GET /v3/functions/{functionName}/versions/{versionNum}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_name:
            raise ValueError(f"Expected a non-empty value for `function_name` but received {function_name!r}")
        return await self._get(
            path_template("/v3/functions/{function_name}", function_name=function_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionResponse,
        )

    @overload
    async def update(
        self,
        path_function_name: str,
        *,
        type: Literal["extract"],
        display_name: str | Omit = omit,
        enable_bounding_boxes: bool | Omit = omit,
        function_name: str | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        pre_count: bool | Omit = omit,
        tabular_chunking_enabled: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          display_name: Display name of function. Human-readable name to help you identify the function.

          enable_bounding_boxes: Whether bounding box extraction is enabled. Applies to vision input types (pdf,
              png, jpeg, heic, heif, webp) that dispatch through the analyze path. When true,
              the function returns the document regions (page, coordinates) from which each
              field was extracted. Enabling this automatically configures the function to use
              the bounding box model. Disabling resets to the default.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          output_schema: Desired output structure defined in standard JSON Schema convention.

          output_schema_name: Name of output schema object.

          pre_count:
              Reducing the risk of the model stopping early on long documents. Trade-off:
              Increases total latency. Compatible with `enableBoundingBoxes`.

          tabular_chunking_enabled: Whether tabular chunking is enabled. When true, tables in CSV/Excel files are
              processed in row batches rather than all at once.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        path_function_name: str,
        *,
        type: Literal["classify"],
        classifications: Iterable[ClassificationListItemParam] | Omit = omit,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          classifications: List of classifications a classify function can produce. Shares the underlying
              route list shape.

          description: Description of classifier. Can be used to provide additional context on
              classifier's purpose and expected inputs.

          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        path_function_name: str,
        *,
        type: Literal["send"],
        destination_type: Literal["webhook", "s3", "google_drive"] | Omit = omit,
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_prefix: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_signing_enabled: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          destination_type: Destination type for a Send function.

          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          google_drive_folder_id: Google Drive folder ID. Required when destinationType is google_drive. Managed
              via Paragon OAuth.

          s3_bucket: S3 bucket to upload the payload to. Required when destinationType is s3.

          s3_prefix: Optional S3 key prefix (folder path).

          tags: Array of tags to categorize and organize functions.

          webhook_signing_enabled: Whether to sign webhook deliveries with an HMAC-SHA256 `bem-signature` header.
              Defaults to `true` when omitted — signing is on by default for new send
              functions. Set explicitly to `false` to disable.

          webhook_url: Webhook URL to POST the payload to. Required when destinationType is webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        path_function_name: str,
        *,
        type: Literal["split"],
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        print_page_split_config: function_update_params.UpsertSplitFunctionPrintPageSplitConfig | Omit = omit,
        semantic_page_split_config: function_update_params.UpsertSplitFunctionSemanticPageSplitConfig | Omit = omit,
        split_type: Literal["print_page", "semantic_page"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        path_function_name: str,
        *,
        type: Literal["join"],
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        join_type: Literal["standard"] | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          description: Description of join function.

          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          join_type: The type of join to perform.

          output_schema: Desired output structure defined in standard JSON Schema convention.

          output_schema_name: Name of output schema object.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        path_function_name: str,
        *,
        type: Literal["payload_shaping"],
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        shaping_schema: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          shaping_schema: JMESPath expression that defines how to transform and customize the input
              payload structure. Payload shaping allows you to extract, reshape, and
              reorganize data from complex input payloads into a simplified, standardized
              output format. Use JMESPath syntax to select specific fields, perform
              calculations, and create new data structures tailored to your needs.

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        path_function_name: str,
        *,
        type: Literal["enrich"],
        config: EnrichConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          config: Configuration for enrich function with semantic search steps.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        path_function_name: str,
        *,
        type: Literal["parse"],
        display_name: str | Omit = omit,
        function_name: str | Omit = omit,
        parse_config: function_update_params.UpsertParseFunctionParseConfig | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """**Update a function.

        Updates create a new version.**

        The previous version remains addressable and immutable. Workflow nodes that
        pinned the function with a `versionNum` continue to use the pinned version;
        nodes that reference the function by name with no version automatically pick up
        the new version on their next call.

        ## What you can change

        Any field allowed by the function's type. Most commonly: `outputSchema` (for
        `extract`/`join`), `classifications` (for `classify`), `displayName`, and
        `tags`.

        ## Versioning behaviour

        - Each successful update increments `currentVersionNum` by 1.
        - `displayName`, `tags`, and `functionName` updates also create a new version,
          so the version history is a complete record of every change.
        - To revert, fetch the previous version and re-submit its configuration as a new
          update — versions themselves are immutable.

        Args:
          display_name: Display name of function. Human-readable name to help you identify the function.

          function_name: Name of function. Must be UNIQUE on a per-environment basis.

          parse_config: Per-version configuration for a Parse function.

              Parse renders document pages (PDF, image) via vision LLM and emits structured
              JSON. The two toggles below independently control entity extraction (a per-call
              output concern) and cross-document memory linking (an environment-wide concern).

          tags: Array of tags to categorize and organize functions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"])
    async def update(
        self,
        path_function_name: str,
        *,
        type: Literal["extract"]
        | Literal["classify"]
        | Literal["send"]
        | Literal["split"]
        | Literal["join"]
        | Literal["payload_shaping"]
        | Literal["enrich"]
        | Literal["parse"],
        display_name: str | Omit = omit,
        enable_bounding_boxes: bool | Omit = omit,
        function_name: str | Omit = omit,
        output_schema: object | Omit = omit,
        output_schema_name: str | Omit = omit,
        pre_count: bool | Omit = omit,
        tabular_chunking_enabled: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        classifications: Iterable[ClassificationListItemParam] | Omit = omit,
        description: str | Omit = omit,
        destination_type: Literal["webhook", "s3", "google_drive"] | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_prefix: str | Omit = omit,
        webhook_signing_enabled: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        print_page_split_config: function_update_params.UpsertSplitFunctionPrintPageSplitConfig | Omit = omit,
        semantic_page_split_config: function_update_params.UpsertSplitFunctionSemanticPageSplitConfig | Omit = omit,
        split_type: Literal["print_page", "semantic_page"] | Omit = omit,
        join_type: Literal["standard"] | Omit = omit,
        shaping_schema: str | Omit = omit,
        config: EnrichConfigParam | Omit = omit,
        parse_config: function_update_params.UpsertParseFunctionParseConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        if not path_function_name:
            raise ValueError(f"Expected a non-empty value for `path_function_name` but received {path_function_name!r}")
        return await self._patch(
            path_template("/v3/functions/{path_function_name}", path_function_name=path_function_name),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "display_name": display_name,
                    "enable_bounding_boxes": enable_bounding_boxes,
                    "function_name": function_name,
                    "output_schema": output_schema,
                    "output_schema_name": output_schema_name,
                    "pre_count": pre_count,
                    "tabular_chunking_enabled": tabular_chunking_enabled,
                    "tags": tags,
                    "classifications": classifications,
                    "description": description,
                    "destination_type": destination_type,
                    "google_drive_folder_id": google_drive_folder_id,
                    "s3_bucket": s3_bucket,
                    "s3_prefix": s3_prefix,
                    "webhook_signing_enabled": webhook_signing_enabled,
                    "webhook_url": webhook_url,
                    "print_page_split_config": print_page_split_config,
                    "semantic_page_split_config": semantic_page_split_config,
                    "split_type": split_type,
                    "join_type": join_type,
                    "shaping_schema": shaping_schema,
                    "config": config,
                    "parse_config": parse_config,
                },
                function_update_params.FunctionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionResponse,
        )

    def list(
        self,
        *,
        display_name: str | Omit = omit,
        ending_before: str | Omit = omit,
        function_ids: SequenceNotStr[str] | Omit = omit,
        function_names: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        types: List[FunctionType] | Omit = omit,
        workflow_ids: SequenceNotStr[str] | Omit = omit,
        workflow_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Function, AsyncFunctionsPage[Function]]:
        """
        **List functions in the current environment.**

        Returns each function's current version. Combine filters freely — they AND
        together.

        ## Filtering

        - `functionIDs` / `functionNames`: exact-match identity filters.
        - `displayName`: case-insensitive substring match.
        - `types`: one or more of `extract`, `classify`, `split`, `join`, `enrich`,
          `payload_shaping`. Legacy `transform`, `analyze`, `route`, and `send` types
          remain readable via this filter.
        - `tags`: returns functions tagged with any of the supplied tags.
        - `workflowIDs` / `workflowNames`: returns only functions referenced by the
          named workflows. Useful for "what functions does this workflow depend on?"
          lookups.

        ## Pagination

        Cursor-based with `startingAfter` and `endingBefore` (functionIDs). Default
        limit 50, maximum 100.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/functions",
            page=AsyncFunctionsPage[Function],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "display_name": display_name,
                        "ending_before": ending_before,
                        "function_ids": function_ids,
                        "function_names": function_names,
                        "limit": limit,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                        "tags": tags,
                        "types": types,
                        "workflow_ids": workflow_ids,
                        "workflow_names": workflow_names,
                    },
                    function_list_params.FunctionListParams,
                ),
            ),
            model=cast(Any, Function),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        function_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """**Delete a function and every one of its versions.**

        Permanent.

        Running and queued calls that reference this function continue to
        completion against the version they captured at call time, but no new calls can
        target it.

        ## Before deleting

        Workflow nodes that reference this function will fail at call time after
        deletion. List workflows that reference it first:

        ```
        GET /v3/workflows?functionNames=my-function
        ```

        Update or remove those workflows, or create a replacement function and re-point
        the workflow nodes, before deleting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_name:
            raise ValueError(f"Expected a non-empty value for `function_name` but received {function_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/functions/{function_name}", function_name=function_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_raw_response_wrapper(
            functions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            functions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            functions.update,
        )
        self.list = to_raw_response_wrapper(
            functions.list,
        )
        self.delete = to_raw_response_wrapper(
            functions.delete,
        )

    @cached_property
    def copy(self) -> CopyResourceWithRawResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return CopyResourceWithRawResponse(self._functions.copy)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return VersionsResourceWithRawResponse(self._functions.versions)


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_raw_response_wrapper(
            functions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            functions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            functions.update,
        )
        self.list = async_to_raw_response_wrapper(
            functions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            functions.delete,
        )

    @cached_property
    def copy(self) -> AsyncCopyResourceWithRawResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return AsyncCopyResourceWithRawResponse(self._functions.copy)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return AsyncVersionsResourceWithRawResponse(self._functions.versions)


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_streamed_response_wrapper(
            functions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            functions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            functions.update,
        )
        self.list = to_streamed_response_wrapper(
            functions.list,
        )
        self.delete = to_streamed_response_wrapper(
            functions.delete,
        )

    @cached_property
    def copy(self) -> CopyResourceWithStreamingResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return CopyResourceWithStreamingResponse(self._functions.copy)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return VersionsResourceWithStreamingResponse(self._functions.versions)


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_streamed_response_wrapper(
            functions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            functions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            functions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            functions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            functions.delete,
        )

    @cached_property
    def copy(self) -> AsyncCopyResourceWithStreamingResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return AsyncCopyResourceWithStreamingResponse(self._functions.copy)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        return AsyncVersionsResourceWithStreamingResponse(self._functions.versions)
