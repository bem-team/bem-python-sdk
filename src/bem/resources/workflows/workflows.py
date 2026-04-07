# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
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
from ...pagination import SyncWorkflowsPage, AsyncWorkflowsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.call_get_response import CallGetResponse
from ...types.workflow_copy_response import WorkflowCopyResponse
from ...types.workflow_list_response import WorkflowListResponse
from ...types.workflow_create_response import WorkflowCreateResponse
from ...types.workflow_update_response import WorkflowUpdateResponse
from ...types.workflow_retrieve_response import WorkflowRetrieveResponse

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]


class WorkflowsResource(SyncAPIResource):
    """Workflow operations"""

    @cached_property
    def versions(self) -> VersionsResource:
        """Workflow operations"""
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
        display_name: str | Omit = omit,
        edges: Iterable[workflow_create_params.Edge] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowCreateResponse:
        """Create a Workflow

        Args:
          main_node_name: Name of the entry-point node.

        Must not be a destination of any edge.

          name: Unique name for the workflow. Must match `^[a-zA-Z0-9_-]{1,128}$`.

          nodes: Call-site nodes in the DAG. At least one is required.

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
                    "display_name": display_name,
                    "edges": edges,
                    "tags": tags,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowCreateResponse,
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
        Get a Workflow

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
        """
        Update a Workflow

        Args:
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
    ) -> SyncWorkflowsPage[WorkflowListResponse]:
        """
        List Workflows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/workflows",
            page=SyncWorkflowsPage[WorkflowListResponse],
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
            model=WorkflowListResponse,
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
        """
        Delete a Workflow

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
        call_reference_id: str | Omit = omit,
        file: object | Omit = omit,
        files: Iterable[object] | Omit = omit,
        wait: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetResponse:
        """
        **Invoke a workflow by submitting a multipart form request.**

        Workflows can only be called via multipart form in V3. Submit the input file
        along with an optional reference ID for tracking.

        ## Synchronous vs Asynchronous

        By default the call is created asynchronously and this endpoint returns
        `202 Accepted` immediately with a `pending` call object. Set the `wait` field to
        `true` to block until the call completes (up to 30 seconds):

        - On success: returns `200 OK` with the completed call, `outputs` populated
        - On failure: returns `500 Internal Server Error` with the call and an `error`
          message
        - On timeout: returns `202 Accepted` with the still-running call

        ## Tracking

        Poll `GET /v3/calls/{callID}` to check status, or configure a webhook
        subscription to receive events when the call finishes.

        Args:
          call_reference_id: Your reference ID for tracking this call.

          file: Single input file (for transform, analyze, route, and split functions).

          files: Multiple input files (for join functions).

          wait: When `true`, the endpoint blocks until the call completes (up to 30 seconds) and
              returns the finished call object. Default: `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_name:
            raise ValueError(f"Expected a non-empty value for `workflow_name` but received {workflow_name!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/v3/workflows/{workflow_name}/call", workflow_name=workflow_name),
            body=maybe_transform(
                {
                    "call_reference_id": call_reference_id,
                    "file": file,
                    "files": files,
                    "wait": wait,
                },
                workflow_call_params.WorkflowCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        Copy a Workflow

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
    """Workflow operations"""

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        """Workflow operations"""
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
        display_name: str | Omit = omit,
        edges: Iterable[workflow_create_params.Edge] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowCreateResponse:
        """Create a Workflow

        Args:
          main_node_name: Name of the entry-point node.

        Must not be a destination of any edge.

          name: Unique name for the workflow. Must match `^[a-zA-Z0-9_-]{1,128}$`.

          nodes: Call-site nodes in the DAG. At least one is required.

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
                    "display_name": display_name,
                    "edges": edges,
                    "tags": tags,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowCreateResponse,
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
        Get a Workflow

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
        """
        Update a Workflow

        Args:
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
    ) -> AsyncPaginator[WorkflowListResponse, AsyncWorkflowsPage[WorkflowListResponse]]:
        """
        List Workflows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/workflows",
            page=AsyncWorkflowsPage[WorkflowListResponse],
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
            model=WorkflowListResponse,
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
        """
        Delete a Workflow

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
        call_reference_id: str | Omit = omit,
        file: object | Omit = omit,
        files: Iterable[object] | Omit = omit,
        wait: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetResponse:
        """
        **Invoke a workflow by submitting a multipart form request.**

        Workflows can only be called via multipart form in V3. Submit the input file
        along with an optional reference ID for tracking.

        ## Synchronous vs Asynchronous

        By default the call is created asynchronously and this endpoint returns
        `202 Accepted` immediately with a `pending` call object. Set the `wait` field to
        `true` to block until the call completes (up to 30 seconds):

        - On success: returns `200 OK` with the completed call, `outputs` populated
        - On failure: returns `500 Internal Server Error` with the call and an `error`
          message
        - On timeout: returns `202 Accepted` with the still-running call

        ## Tracking

        Poll `GET /v3/calls/{callID}` to check status, or configure a webhook
        subscription to receive events when the call finishes.

        Args:
          call_reference_id: Your reference ID for tracking this call.

          file: Single input file (for transform, analyze, route, and split functions).

          files: Multiple input files (for join functions).

          wait: When `true`, the endpoint blocks until the call completes (up to 30 seconds) and
              returns the finished call object. Default: `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_name:
            raise ValueError(f"Expected a non-empty value for `workflow_name` but received {workflow_name!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/v3/workflows/{workflow_name}/call", workflow_name=workflow_name),
            body=await async_maybe_transform(
                {
                    "call_reference_id": call_reference_id,
                    "file": file,
                    "files": files,
                    "wait": wait,
                },
                workflow_call_params.WorkflowCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        Copy a Workflow

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
        """Workflow operations"""
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
        """Workflow operations"""
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
        """Workflow operations"""
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
        """Workflow operations"""
        return AsyncVersionsResourceWithStreamingResponse(self._workflows.versions)
