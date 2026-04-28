# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...types import (
    workflow_call_params,
    workflow_copy_params,
    workflow_list_params,
    workflow_create_params,
    workflow_update_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ..._wrappers import WorkflowWrapper
from ...pagination import SyncWorkflowsPage, AsyncWorkflowsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.workflow import Workflow
from ...types.call_get_response import CallGetResponse
from ...types.workflow_copy_response import WorkflowCopyResponse
from ...types.workflow_update_response import WorkflowUpdateResponse
from ...types.workflow_retrieve_response import WorkflowRetrieveResponse

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]


class WorkflowsResource(SyncAPIResource):
    """
    Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

    Use these endpoints to create, update, list, and manage workflows, and to invoke them
    with file input via `POST /v3/workflows/{workflowName}/call`.

    The call endpoint accepts files as either multipart form data or JSON with base64-encoded
    content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
    encode files:

    ```
    bem workflows call --workflow-name my-workflow \\
      --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
      --wait
    ```
    """

    @cached_property
    def versions(self) -> VersionsResource:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return WorkflowsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        main_node_name: str,
        name: str,
        nodes: Iterable[workflow_create_params.Node],
        connectors: Iterable[workflow_create_params.Connector] | Omit = omit,
        display_name: str | Omit = omit,
        edges: Iterable[workflow_create_params.Edge] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Workflow]:
        """
        **Create a workflow.**

        A workflow is a directed acyclic graph of nodes (each pointing at a function)
        with one entry point (`mainNodeName`). The graph runs end-to-end on every call.

        ## Required structure

        - `name`: unique within the environment, alphanumeric plus hyphens and
          underscores.
        - `mainNodeName`: must match one of the `nodes[].name` values, and must not be
          the destination of any edge.
        - `nodes`: at least one. Each node has a unique `name` and a `function`
          reference (by `functionName` or `functionID`, optionally pinned to a
          `versionNum`).
        - `edges`: optional for single-node workflows. For branching sources (Classify,
          semantic Split), each edge carries a `destinationName` matching a
          `classifications[].name` or `itemClasses[].name` on the source function.

        The created workflow is at `versionNum: 1`. Subsequent
        `PATCH /v3/workflows/{workflowName}` calls produce new versions.

        ## Common patterns

        - **Single-node**: one extract/classify function, no edges.
        - **Sequential**: extract → enrich → payload_shaping (linear edges).
        - **Branching**: classify → multiple extracts (one edge per classification
          name).
        - **Split-then-process**: split → multiple extracts (one edge per item class).

        See [Workflows explained](/guide/workflows-explained) for end-to-end examples of
        each pattern.

        Args:
          main_node_name: Name of the entry-point node. Must not be a destination of any edge.

          name: Unique name for the workflow. Must match `^[a-zA-Z0-9_-]{1,128}$`.

          nodes: Call-site nodes in the DAG. At least one is required.

          connectors: Connectors to attach to the workflow at creation. If any entry fails to
              provision, the entire workflow creation is rolled back.

          display_name: Human-readable display name.

          edges: Directed edges between nodes. Omit or leave empty for single-node workflows.

          tags: Tags to categorize and organize the workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/workflows",
            body=maybe_transform(
                {
                    "main_node_name": main_node_name,
                    "name": name,
                    "nodes": nodes,
                    "connectors": connectors,
                    "display_name": display_name,
                    "edges": edges,
                    "tags": tags,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=WorkflowWrapper[Optional[Workflow]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Workflow]], WorkflowWrapper[Workflow]),
        )

    def retrieve(
        self,
        workflow_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRetrieveResponse:
        """
        **Retrieve a workflow's current version by name.**

        Returns the full workflow record: `currentVersionNum`, `mainNodeName`, the
        `nodes` array (with each node's function reference and pinned `versionNum` if
        any), and the `edges` array. To inspect a historical version, use
        `GET /v3/workflows/{workflowName}/versions/{versionNum}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_name:
            raise ValueError(f"Expected a non-empty value for `workflow_name` but received {workflow_name!r}")
        return self._get(
            path_template("/v3/workflows/{workflow_name}", workflow_name=workflow_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowRetrieveResponse,
        )

    def update(
        self,
        workflow_name: str,
        *,
        connectors: Iterable[workflow_update_params.Connector] | Omit = omit,
        display_name: str | Omit = omit,
        edges: Iterable[workflow_update_params.Edge] | Omit = omit,
        main_node_name: str | Omit = omit,
        name: str | Omit = omit,
        nodes: Iterable[workflow_update_params.Node] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowUpdateResponse:
        """**Update a workflow.

        Updates create a new version.**

        The previous version remains addressable and immutable. Pending and running
        calls captured at the old version continue against it; new calls run against the
        new version.

        ## Topology updates

        To change the graph you must provide `mainNodeName`, `nodes`, AND `edges`
        together — partial topology updates are rejected. The full graph is replaced
        atomically.

        ## Metadata-only updates

        Omit all three fields to update only `displayName`, `tags`, or `name` while
        keeping the topology of the current version.

        ## Reverting

        To roll back, fetch the desired prior version and resubmit its
        `mainNodeName`/`nodes`/`edges` as a new update. Versions themselves are
        immutable — there is no "pin to version N" operation at the workflow level (use
        `nodes[].function.versionNum` to pin individual functions).

        Args:
          connectors: Declarative, full-desired-state array of connectors. If omitted, existing
              connectors are left unchanged. If provided, it replaces the current set: entries
              with `connectorID` are updates, entries without are creates, and existing
              connectors whose `connectorID` is absent are deleted.

          display_name: Human-readable display name.

          main_node_name: `mainNodeName`, `nodes`, and `edges` must be provided together to update the DAG
              topology. If none are provided the topology is copied unchanged from the current
              version.

          name: New name for the workflow (renames it). Must match `^[a-zA-Z0-9_-]{1,128}$`.

          tags: Tags to categorize and organize the workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_name:
            raise ValueError(f"Expected a non-empty value for `workflow_name` but received {workflow_name!r}")
        return self._patch(
            path_template("/v3/workflows/{workflow_name}", workflow_name=workflow_name),
            body=maybe_transform(
                {
                    "connectors": connectors,
                    "display_name": display_name,
                    "edges": edges,
                    "main_node_name": main_node_name,
                    "name": name,
                    "nodes": nodes,
                    "tags": tags,
                },
                workflow_update_params.WorkflowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowUpdateResponse,
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
        workflow_ids: SequenceNotStr[str] | Omit = omit,
        workflow_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncWorkflowsPage[Workflow]:
        """
        **List workflows in the current environment.**

        Returns each workflow's current version, including its node graph and main node.
        Combine filters freely — they AND together.

        ## Filtering

        - `workflowIDs` / `workflowNames`: exact-match identity filters.
        - `displayName`: case-insensitive substring match.
        - `tags`: returns workflows tagged with any of the supplied tags.
        - `functionIDs` / `functionNames`: returns only workflows that reference the
          named functions in any node. Useful for "which workflows depend on this
          function?" lookups before changing or deleting a function.

        ## Pagination

        Cursor-based with `startingAfter` and `endingBefore` (workflowIDs). Default
        limit 50, maximum 100.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/workflows",
            page=SyncWorkflowsPage[Workflow],
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
                        "workflow_ids": workflow_ids,
                        "workflow_names": workflow_names,
                    },
                    workflow_list_params.WorkflowListParams,
                ),
            ),
            model=Workflow,
        )

    def delete(
        self,
        workflow_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """**Delete a workflow and every one of its versions.**

        Permanent.

        Running and queued calls against this workflow continue to completion
        against the version they captured at call time; subsequent attempts to call the
        workflow return `404 Not Found`.

        Functions referenced by the deleted workflow are not removed — they remain
        available to other workflows or for direct reference.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_name:
            raise ValueError(f"Expected a non-empty value for `workflow_name` but received {workflow_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/workflows/{workflow_name}", workflow_name=workflow_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def call(
        self,
        workflow_name: str,
        *,
        input: workflow_call_params.Input,
        wait: bool | Omit = omit,
        call_reference_id: str | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetResponse:
        """
        **Invoke a workflow.**

        Submit the input file as either a multipart form request or a JSON request with
        base64-encoded file content. The workflow name is derived from the URL path.

        ## Input Formats

        - **Multipart form** (`multipart/form-data`): attach the file directly via the
          `file` or `files` fields. Set `wait` in the form body to control synchronous
          behaviour.
        - **JSON** (`application/json`): base64-encode the file content and set it in
          `input.singleFile.inputContent` or `input.batchFiles.inputs[*].inputContent`.
          Pass `wait=true` as a query parameter to control synchronous behaviour.

        ## Synchronous vs Asynchronous

        By default the call is created asynchronously and this endpoint returns
        `202 Accepted` immediately with a `pending` call object. Set `wait` to `true` to
        block until the call completes (up to 30 seconds):

        - On success: returns `200 OK` with the completed call, `outputs` populated
        - On failure: returns `500 Internal Server Error` with the call and an `error`
          message
        - On timeout: returns `202 Accepted` with the still-running call

        ## Tracking

        Poll `GET /v3/calls/{callID}` to check status, or configure a webhook
        subscription to receive events when the call finishes.

        ## CLI Usage

        Use `@path/to/file` inside JSON string values to embed file contents
        automatically. Binary files (PDF, images, audio) are base64-encoded; text files
        are embedded as strings.

        Single file (synchronous):

        ```bash
        bem workflows call \\
          --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@invoice.pdf", "inputType": "pdf"}' \\
          --wait
        ```

        Single file (asynchronous, returns callID immediately):

        ```bash
        bem workflows call \\
          --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@invoice.pdf", "inputType": "pdf"}'
        ```

        Batch files:

        ```bash
        bem workflows call \\
          --workflow-name my-workflow \\
          --input.batch-files '{"inputs": [{"inputContent": "@a.pdf", "inputType": "pdf"}, {"inputContent": "@b.png", "inputType": "png"}]}'
        ```

        Alternative: pass the full `--input` flag as JSON:

        ```bash
        bem workflows call \\
          --workflow-name my-workflow \\
          --input '{"singleFile": {"inputContent": "@invoice.pdf", "inputType": "pdf"}}' \\
          --wait
        ```

        **Important:** `--wait` is a boolean flag. Use `--wait` or `--wait=true`. Do
        **not** use `--wait true` (with a space) — the `true` will be parsed as an
        unexpected positional argument.

        Supported `inputType` values: csv, docx, email, heic, heif, html, jpeg, json,
        m4a, mp3, pdf, png, text, wav, webp, xls, xlsx, xml.

        Args:
          input: Input file(s) for a call. Provide exactly one of `singleFile` or `batchFiles`.

              In the CLI, use the nested flags `--input.single-file` or `--input.batch-files`
              with `@path/to/file` for automatic file embedding:
              `--input.single-file '{"inputContent": "@invoice.pdf", "inputType": "pdf"}' --wait`

          wait: Block until the call completes (up to 30 seconds) and return the finished call
              object. Default: `false`. This is a boolean flag — use `--wait` or
              `--wait=true`, not `--wait true`.

          call_reference_id: Your reference ID for tracking this call.

          metadata: Arbitrary JSON object attached to this call. Stored on the call record and
              injected into `transformedContent` under the reserved `_metadata` key (alongside
              `referenceID`). Must be a JSON object. Maximum size: 4 KB.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_name:
            raise ValueError(f"Expected a non-empty value for `workflow_name` but received {workflow_name!r}")
        return self._post(
            path_template("/v3/workflows/{workflow_name}/call", workflow_name=workflow_name),
            body=maybe_transform(
                {
                    "input": input,
                    "call_reference_id": call_reference_id,
                    "metadata": metadata,
                },
                workflow_call_params.WorkflowCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"wait": wait}, workflow_call_params.WorkflowCallParams),
            ),
            cast_to=CallGetResponse,
        )

    def copy(
        self,
        *,
        source_workflow_name: str,
        target_workflow_name: str,
        source_workflow_version_num: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        target_display_name: str | Omit = omit,
        target_environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowCopyResponse:
        """
        **Copy a workflow to a new name.**

        Forks the source workflow's current version into a brand-new workflow at
        `versionNum: 1`. The full node graph and edges are carried over, but the
        _functions_ the copied nodes reference are shared, not duplicated — both
        workflows now point at the same functions.

        Useful for forking a production workflow to test a topology change without
        disturbing the live caller.

        Args:
          source_workflow_name: Name of the source workflow to copy from.

          target_workflow_name: Name for the new copied workflow. Must be unique within the target environment.

          source_workflow_version_num: Optional version number of the source workflow to copy. If not provided, copies
              the current version.

          tags: Optional tags for the copied workflow. If not provided, uses the source
              workflow's tags.

          target_display_name: Optional display name for the copied workflow. If not provided, uses the source
              workflow's display name with " (Copy)" appended.

          target_environment: Optional target environment name. If provided, copies the workflow to a
              different environment. When copying to a different environment, all functions
              used in the workflow will also be copied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/workflows/copy",
            body=maybe_transform(
                {
                    "source_workflow_name": source_workflow_name,
                    "target_workflow_name": target_workflow_name,
                    "source_workflow_version_num": source_workflow_version_num,
                    "tags": tags,
                    "target_display_name": target_display_name,
                    "target_environment": target_environment,
                },
                workflow_copy_params.WorkflowCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowCopyResponse,
        )


class AsyncWorkflowsResource(AsyncAPIResource):
    """
    Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

    Use these endpoints to create, update, list, and manage workflows, and to invoke them
    with file input via `POST /v3/workflows/{workflowName}/call`.

    The call endpoint accepts files as either multipart form data or JSON with base64-encoded
    content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
    encode files:

    ```
    bem workflows call --workflow-name my-workflow \\
      --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
      --wait
    ```
    """

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncWorkflowsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        main_node_name: str,
        name: str,
        nodes: Iterable[workflow_create_params.Node],
        connectors: Iterable[workflow_create_params.Connector] | Omit = omit,
        display_name: str | Omit = omit,
        edges: Iterable[workflow_create_params.Edge] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Workflow]:
        """
        **Create a workflow.**

        A workflow is a directed acyclic graph of nodes (each pointing at a function)
        with one entry point (`mainNodeName`). The graph runs end-to-end on every call.

        ## Required structure

        - `name`: unique within the environment, alphanumeric plus hyphens and
          underscores.
        - `mainNodeName`: must match one of the `nodes[].name` values, and must not be
          the destination of any edge.
        - `nodes`: at least one. Each node has a unique `name` and a `function`
          reference (by `functionName` or `functionID`, optionally pinned to a
          `versionNum`).
        - `edges`: optional for single-node workflows. For branching sources (Classify,
          semantic Split), each edge carries a `destinationName` matching a
          `classifications[].name` or `itemClasses[].name` on the source function.

        The created workflow is at `versionNum: 1`. Subsequent
        `PATCH /v3/workflows/{workflowName}` calls produce new versions.

        ## Common patterns

        - **Single-node**: one extract/classify function, no edges.
        - **Sequential**: extract → enrich → payload_shaping (linear edges).
        - **Branching**: classify → multiple extracts (one edge per classification
          name).
        - **Split-then-process**: split → multiple extracts (one edge per item class).

        See [Workflows explained](/guide/workflows-explained) for end-to-end examples of
        each pattern.

        Args:
          main_node_name: Name of the entry-point node. Must not be a destination of any edge.

          name: Unique name for the workflow. Must match `^[a-zA-Z0-9_-]{1,128}$`.

          nodes: Call-site nodes in the DAG. At least one is required.

          connectors: Connectors to attach to the workflow at creation. If any entry fails to
              provision, the entire workflow creation is rolled back.

          display_name: Human-readable display name.

          edges: Directed edges between nodes. Omit or leave empty for single-node workflows.

          tags: Tags to categorize and organize the workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/workflows",
            body=await async_maybe_transform(
                {
                    "main_node_name": main_node_name,
                    "name": name,
                    "nodes": nodes,
                    "connectors": connectors,
                    "display_name": display_name,
                    "edges": edges,
                    "tags": tags,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=WorkflowWrapper[Optional[Workflow]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Workflow]], WorkflowWrapper[Workflow]),
        )

    async def retrieve(
        self,
        workflow_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRetrieveResponse:
        """
        **Retrieve a workflow's current version by name.**

        Returns the full workflow record: `currentVersionNum`, `mainNodeName`, the
        `nodes` array (with each node's function reference and pinned `versionNum` if
        any), and the `edges` array. To inspect a historical version, use
        `GET /v3/workflows/{workflowName}/versions/{versionNum}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_name:
            raise ValueError(f"Expected a non-empty value for `workflow_name` but received {workflow_name!r}")
        return await self._get(
            path_template("/v3/workflows/{workflow_name}", workflow_name=workflow_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowRetrieveResponse,
        )

    async def update(
        self,
        workflow_name: str,
        *,
        connectors: Iterable[workflow_update_params.Connector] | Omit = omit,
        display_name: str | Omit = omit,
        edges: Iterable[workflow_update_params.Edge] | Omit = omit,
        main_node_name: str | Omit = omit,
        name: str | Omit = omit,
        nodes: Iterable[workflow_update_params.Node] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowUpdateResponse:
        """**Update a workflow.

        Updates create a new version.**

        The previous version remains addressable and immutable. Pending and running
        calls captured at the old version continue against it; new calls run against the
        new version.

        ## Topology updates

        To change the graph you must provide `mainNodeName`, `nodes`, AND `edges`
        together — partial topology updates are rejected. The full graph is replaced
        atomically.

        ## Metadata-only updates

        Omit all three fields to update only `displayName`, `tags`, or `name` while
        keeping the topology of the current version.

        ## Reverting

        To roll back, fetch the desired prior version and resubmit its
        `mainNodeName`/`nodes`/`edges` as a new update. Versions themselves are
        immutable — there is no "pin to version N" operation at the workflow level (use
        `nodes[].function.versionNum` to pin individual functions).

        Args:
          connectors: Declarative, full-desired-state array of connectors. If omitted, existing
              connectors are left unchanged. If provided, it replaces the current set: entries
              with `connectorID` are updates, entries without are creates, and existing
              connectors whose `connectorID` is absent are deleted.

          display_name: Human-readable display name.

          main_node_name: `mainNodeName`, `nodes`, and `edges` must be provided together to update the DAG
              topology. If none are provided the topology is copied unchanged from the current
              version.

          name: New name for the workflow (renames it). Must match `^[a-zA-Z0-9_-]{1,128}$`.

          tags: Tags to categorize and organize the workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_name:
            raise ValueError(f"Expected a non-empty value for `workflow_name` but received {workflow_name!r}")
        return await self._patch(
            path_template("/v3/workflows/{workflow_name}", workflow_name=workflow_name),
            body=await async_maybe_transform(
                {
                    "connectors": connectors,
                    "display_name": display_name,
                    "edges": edges,
                    "main_node_name": main_node_name,
                    "name": name,
                    "nodes": nodes,
                    "tags": tags,
                },
                workflow_update_params.WorkflowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowUpdateResponse,
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
        workflow_ids: SequenceNotStr[str] | Omit = omit,
        workflow_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Workflow, AsyncWorkflowsPage[Workflow]]:
        """
        **List workflows in the current environment.**

        Returns each workflow's current version, including its node graph and main node.
        Combine filters freely — they AND together.

        ## Filtering

        - `workflowIDs` / `workflowNames`: exact-match identity filters.
        - `displayName`: case-insensitive substring match.
        - `tags`: returns workflows tagged with any of the supplied tags.
        - `functionIDs` / `functionNames`: returns only workflows that reference the
          named functions in any node. Useful for "which workflows depend on this
          function?" lookups before changing or deleting a function.

        ## Pagination

        Cursor-based with `startingAfter` and `endingBefore` (workflowIDs). Default
        limit 50, maximum 100.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/workflows",
            page=AsyncWorkflowsPage[Workflow],
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
                        "workflow_ids": workflow_ids,
                        "workflow_names": workflow_names,
                    },
                    workflow_list_params.WorkflowListParams,
                ),
            ),
            model=Workflow,
        )

    async def delete(
        self,
        workflow_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """**Delete a workflow and every one of its versions.**

        Permanent.

        Running and queued calls against this workflow continue to completion
        against the version they captured at call time; subsequent attempts to call the
        workflow return `404 Not Found`.

        Functions referenced by the deleted workflow are not removed — they remain
        available to other workflows or for direct reference.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_name:
            raise ValueError(f"Expected a non-empty value for `workflow_name` but received {workflow_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/workflows/{workflow_name}", workflow_name=workflow_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def call(
        self,
        workflow_name: str,
        *,
        input: workflow_call_params.Input,
        wait: bool | Omit = omit,
        call_reference_id: str | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetResponse:
        """
        **Invoke a workflow.**

        Submit the input file as either a multipart form request or a JSON request with
        base64-encoded file content. The workflow name is derived from the URL path.

        ## Input Formats

        - **Multipart form** (`multipart/form-data`): attach the file directly via the
          `file` or `files` fields. Set `wait` in the form body to control synchronous
          behaviour.
        - **JSON** (`application/json`): base64-encode the file content and set it in
          `input.singleFile.inputContent` or `input.batchFiles.inputs[*].inputContent`.
          Pass `wait=true` as a query parameter to control synchronous behaviour.

        ## Synchronous vs Asynchronous

        By default the call is created asynchronously and this endpoint returns
        `202 Accepted` immediately with a `pending` call object. Set `wait` to `true` to
        block until the call completes (up to 30 seconds):

        - On success: returns `200 OK` with the completed call, `outputs` populated
        - On failure: returns `500 Internal Server Error` with the call and an `error`
          message
        - On timeout: returns `202 Accepted` with the still-running call

        ## Tracking

        Poll `GET /v3/calls/{callID}` to check status, or configure a webhook
        subscription to receive events when the call finishes.

        ## CLI Usage

        Use `@path/to/file` inside JSON string values to embed file contents
        automatically. Binary files (PDF, images, audio) are base64-encoded; text files
        are embedded as strings.

        Single file (synchronous):

        ```bash
        bem workflows call \\
          --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@invoice.pdf", "inputType": "pdf"}' \\
          --wait
        ```

        Single file (asynchronous, returns callID immediately):

        ```bash
        bem workflows call \\
          --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@invoice.pdf", "inputType": "pdf"}'
        ```

        Batch files:

        ```bash
        bem workflows call \\
          --workflow-name my-workflow \\
          --input.batch-files '{"inputs": [{"inputContent": "@a.pdf", "inputType": "pdf"}, {"inputContent": "@b.png", "inputType": "png"}]}'
        ```

        Alternative: pass the full `--input` flag as JSON:

        ```bash
        bem workflows call \\
          --workflow-name my-workflow \\
          --input '{"singleFile": {"inputContent": "@invoice.pdf", "inputType": "pdf"}}' \\
          --wait
        ```

        **Important:** `--wait` is a boolean flag. Use `--wait` or `--wait=true`. Do
        **not** use `--wait true` (with a space) — the `true` will be parsed as an
        unexpected positional argument.

        Supported `inputType` values: csv, docx, email, heic, heif, html, jpeg, json,
        m4a, mp3, pdf, png, text, wav, webp, xls, xlsx, xml.

        Args:
          input: Input file(s) for a call. Provide exactly one of `singleFile` or `batchFiles`.

              In the CLI, use the nested flags `--input.single-file` or `--input.batch-files`
              with `@path/to/file` for automatic file embedding:
              `--input.single-file '{"inputContent": "@invoice.pdf", "inputType": "pdf"}' --wait`

          wait: Block until the call completes (up to 30 seconds) and return the finished call
              object. Default: `false`. This is a boolean flag — use `--wait` or
              `--wait=true`, not `--wait true`.

          call_reference_id: Your reference ID for tracking this call.

          metadata: Arbitrary JSON object attached to this call. Stored on the call record and
              injected into `transformedContent` under the reserved `_metadata` key (alongside
              `referenceID`). Must be a JSON object. Maximum size: 4 KB.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_name:
            raise ValueError(f"Expected a non-empty value for `workflow_name` but received {workflow_name!r}")
        return await self._post(
            path_template("/v3/workflows/{workflow_name}/call", workflow_name=workflow_name),
            body=await async_maybe_transform(
                {
                    "input": input,
                    "call_reference_id": call_reference_id,
                    "metadata": metadata,
                },
                workflow_call_params.WorkflowCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"wait": wait}, workflow_call_params.WorkflowCallParams),
            ),
            cast_to=CallGetResponse,
        )

    async def copy(
        self,
        *,
        source_workflow_name: str,
        target_workflow_name: str,
        source_workflow_version_num: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        target_display_name: str | Omit = omit,
        target_environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowCopyResponse:
        """
        **Copy a workflow to a new name.**

        Forks the source workflow's current version into a brand-new workflow at
        `versionNum: 1`. The full node graph and edges are carried over, but the
        _functions_ the copied nodes reference are shared, not duplicated — both
        workflows now point at the same functions.

        Useful for forking a production workflow to test a topology change without
        disturbing the live caller.

        Args:
          source_workflow_name: Name of the source workflow to copy from.

          target_workflow_name: Name for the new copied workflow. Must be unique within the target environment.

          source_workflow_version_num: Optional version number of the source workflow to copy. If not provided, copies
              the current version.

          tags: Optional tags for the copied workflow. If not provided, uses the source
              workflow's tags.

          target_display_name: Optional display name for the copied workflow. If not provided, uses the source
              workflow's display name with " (Copy)" appended.

          target_environment: Optional target environment name. If provided, copies the workflow to a
              different environment. When copying to a different environment, all functions
              used in the workflow will also be copied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/workflows/copy",
            body=await async_maybe_transform(
                {
                    "source_workflow_name": source_workflow_name,
                    "target_workflow_name": target_workflow_name,
                    "source_workflow_version_num": source_workflow_version_num,
                    "tags": tags,
                    "target_display_name": target_display_name,
                    "target_environment": target_environment,
                },
                workflow_copy_params.WorkflowCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowCopyResponse,
        )


class WorkflowsResourceWithRawResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.create = to_raw_response_wrapper(
            workflows.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workflows.update,
        )
        self.list = to_raw_response_wrapper(
            workflows.list,
        )
        self.delete = to_raw_response_wrapper(
            workflows.delete,
        )
        self.call = to_raw_response_wrapper(
            workflows.call,
        )
        self.copy = to_raw_response_wrapper(
            workflows.copy,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        return VersionsResourceWithRawResponse(self._workflows.versions)


class AsyncWorkflowsResourceWithRawResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.create = async_to_raw_response_wrapper(
            workflows.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workflows.update,
        )
        self.list = async_to_raw_response_wrapper(
            workflows.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workflows.delete,
        )
        self.call = async_to_raw_response_wrapper(
            workflows.call,
        )
        self.copy = async_to_raw_response_wrapper(
            workflows.copy,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        return AsyncVersionsResourceWithRawResponse(self._workflows.versions)


class WorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.create = to_streamed_response_wrapper(
            workflows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workflows.update,
        )
        self.list = to_streamed_response_wrapper(
            workflows.list,
        )
        self.delete = to_streamed_response_wrapper(
            workflows.delete,
        )
        self.call = to_streamed_response_wrapper(
            workflows.call,
        )
        self.copy = to_streamed_response_wrapper(
            workflows.copy,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        return VersionsResourceWithStreamingResponse(self._workflows.versions)


class AsyncWorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.create = async_to_streamed_response_wrapper(
            workflows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workflows.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workflows.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workflows.delete,
        )
        self.call = async_to_streamed_response_wrapper(
            workflows.call,
        )
        self.copy = async_to_streamed_response_wrapper(
            workflows.copy,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        return AsyncVersionsResourceWithStreamingResponse(self._workflows.versions)
