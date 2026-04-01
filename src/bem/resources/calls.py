# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import call_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.call_list_response import CallListResponse
from ..types.call_get_response_v3 import CallGetResponseV3

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    """
    The Calls API provides a unified interface for invoking both **Workflows** and **Functions**.

    Use this API when you want to:
    - Execute a complete workflow that chains multiple functions together
    - Call a single function directly without defining a workflow
    - Submit batch requests with multiple inputs in a single API call
    - Track execution status using call reference IDs

    **Key Difference**: Calls vs Function Calls
    - **Calls API** (`/v2/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
    - **Function Calls API** (`/v2/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
    """

    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bem-python#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bem-python#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetResponseV3:
        """
        **Retrieve a workflow call by ID.**

        Returns the full call object including status, workflow details, terminal
        outputs, and terminal errors. `outputs` and `errors` are both populated once the
        call finishes — they are not mutually exclusive (a partially-completed workflow
        may have both).

        ## Status

        | Status      | Description                                                 |
        | ----------- | ----------------------------------------------------------- |
        | `pending`   | Queued, not yet started                                     |
        | `running`   | Currently executing                                         |
        | `completed` | All enclosed function calls finished without errors         |
        | `failed`    | One or more enclosed function calls produced an error event |

        Poll this endpoint or configure a webhook subscription to detect completion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return self._get(
            path_template("/v3/calls/{call_id}", call_id=call_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallGetResponseV3,
        )

    def list(
        self,
        *,
        call_ids: SequenceNotStr[str] | Omit = omit,
        ending_before: str | Omit = omit,
        limit: int | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        reference_id_substring: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        statuses: List[Literal["pending", "running", "completed", "failed"]] | Omit = omit,
        workflow_ids: SequenceNotStr[str] | Omit = omit,
        workflow_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListResponse:
        """
        **List workflow calls with filtering and pagination.**

        Returns calls created via `POST /v3/workflows/{workflowName}/call`.

        ## Filtering

        - `callIDs`: Specific call identifiers
        - `referenceIDs`: Your custom reference IDs
        - `workflowIDs` / `workflowNames`: Filter by workflow

        ## Pagination

        Use `startingAfter` and `endingBefore` cursors with a default limit of 50.

        Args:
          reference_id_substring: Case-insensitive substring match against `callReferenceID`.

          statuses: Filter by one or more statuses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "call_ids": call_ids,
                        "ending_before": ending_before,
                        "limit": limit,
                        "reference_ids": reference_ids,
                        "reference_id_substring": reference_id_substring,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                        "statuses": statuses,
                        "workflow_ids": workflow_ids,
                        "workflow_names": workflow_names,
                    },
                    call_list_params.CallListParams,
                ),
            ),
            cast_to=CallListResponse,
        )


class AsyncCallsResource(AsyncAPIResource):
    """
    The Calls API provides a unified interface for invoking both **Workflows** and **Functions**.

    Use this API when you want to:
    - Execute a complete workflow that chains multiple functions together
    - Call a single function directly without defining a workflow
    - Submit batch requests with multiple inputs in a single API call
    - Track execution status using call reference IDs

    **Key Difference**: Calls vs Function Calls
    - **Calls API** (`/v2/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
    - **Function Calls API** (`/v2/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bem-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bem-python#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetResponseV3:
        """
        **Retrieve a workflow call by ID.**

        Returns the full call object including status, workflow details, terminal
        outputs, and terminal errors. `outputs` and `errors` are both populated once the
        call finishes — they are not mutually exclusive (a partially-completed workflow
        may have both).

        ## Status

        | Status      | Description                                                 |
        | ----------- | ----------------------------------------------------------- |
        | `pending`   | Queued, not yet started                                     |
        | `running`   | Currently executing                                         |
        | `completed` | All enclosed function calls finished without errors         |
        | `failed`    | One or more enclosed function calls produced an error event |

        Poll this endpoint or configure a webhook subscription to detect completion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return await self._get(
            path_template("/v3/calls/{call_id}", call_id=call_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallGetResponseV3,
        )

    async def list(
        self,
        *,
        call_ids: SequenceNotStr[str] | Omit = omit,
        ending_before: str | Omit = omit,
        limit: int | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        reference_id_substring: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        statuses: List[Literal["pending", "running", "completed", "failed"]] | Omit = omit,
        workflow_ids: SequenceNotStr[str] | Omit = omit,
        workflow_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListResponse:
        """
        **List workflow calls with filtering and pagination.**

        Returns calls created via `POST /v3/workflows/{workflowName}/call`.

        ## Filtering

        - `callIDs`: Specific call identifiers
        - `referenceIDs`: Your custom reference IDs
        - `workflowIDs` / `workflowNames`: Filter by workflow

        ## Pagination

        Use `startingAfter` and `endingBefore` cursors with a default limit of 50.

        Args:
          reference_id_substring: Case-insensitive substring match against `callReferenceID`.

          statuses: Filter by one or more statuses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "call_ids": call_ids,
                        "ending_before": ending_before,
                        "limit": limit,
                        "reference_ids": reference_ids,
                        "reference_id_substring": reference_id_substring,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                        "statuses": statuses,
                        "workflow_ids": workflow_ids,
                        "workflow_names": workflow_names,
                    },
                    call_list_params.CallListParams,
                ),
            ),
            cast_to=CallListResponse,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.retrieve = to_raw_response_wrapper(
            calls.retrieve,
        )
        self.list = to_raw_response_wrapper(
            calls.list,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.retrieve = async_to_raw_response_wrapper(
            calls.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            calls.list,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.retrieve = to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            calls.list,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.retrieve = async_to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            calls.list,
        )
