# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import error_list_params
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
from ..types.error_list_response import ErrorListResponse
from ..types.error_retrieve_response import ErrorRetrieveResponse

__all__ = ["ErrorsResource", "AsyncErrorsResource"]


class ErrorsResource(SyncAPIResource):
    """Retrieve terminal error events from workflow calls.

    Errors are events produced by function steps that failed during processing. A single workflow
    call may produce multiple error events if several steps fail independently.

    Errors and outputs from the same call are not mutually exclusive: a partially-completed
    workflow may have both.

    Use `GET /v3/errors` to list errors across calls, or `GET /v3/errors/{eventID}` to retrieve
    a specific error. To get errors scoped to a single call, filter by `callIDs`.
    """

    @cached_property
    def with_raw_response(self) -> ErrorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ErrorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ErrorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return ErrorsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ErrorRetrieveResponse:
        """
        **Retrieve a single error event by ID.**

        Returns `404` if the event does not exist or if it is not an error event (use
        `GET /v3/outputs/{eventID}` for non-error events).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template("/v3/errors/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ErrorRetrieveResponse,
        )

    def list(
        self,
        *,
        call_ids: SequenceNotStr[str] | Omit = omit,
        ending_before: str | Omit = omit,
        function_ids: SequenceNotStr[str] | Omit = omit,
        function_names: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        reference_id_substring: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        workflow_ids: SequenceNotStr[str] | Omit = omit,
        workflow_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ErrorListResponse:
        """
        **List terminal error events.**

        Returns error events produced by failed function calls within workflow
        executions. Non-error output events are excluded; use `GET /v3/outputs` to
        retrieve those.

        ## Filtering

        Filter by call, workflow, function, or reference ID. Multiple filters are ANDed
        together.

        Args:
          call_ids: Filter to errors from specific calls.

          reference_id_substring: Case-insensitive substring match against `referenceID`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/errors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "call_ids": call_ids,
                        "ending_before": ending_before,
                        "function_ids": function_ids,
                        "function_names": function_names,
                        "limit": limit,
                        "reference_ids": reference_ids,
                        "reference_id_substring": reference_id_substring,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                        "workflow_ids": workflow_ids,
                        "workflow_names": workflow_names,
                    },
                    error_list_params.ErrorListParams,
                ),
            ),
            cast_to=ErrorListResponse,
        )


class AsyncErrorsResource(AsyncAPIResource):
    """Retrieve terminal error events from workflow calls.

    Errors are events produced by function steps that failed during processing. A single workflow
    call may produce multiple error events if several steps fail independently.

    Errors and outputs from the same call are not mutually exclusive: a partially-completed
    workflow may have both.

    Use `GET /v3/errors` to list errors across calls, or `GET /v3/errors/{eventID}` to retrieve
    a specific error. To get errors scoped to a single call, filter by `callIDs`.
    """

    @cached_property
    def with_raw_response(self) -> AsyncErrorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncErrorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncErrorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncErrorsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ErrorRetrieveResponse:
        """
        **Retrieve a single error event by ID.**

        Returns `404` if the event does not exist or if it is not an error event (use
        `GET /v3/outputs/{eventID}` for non-error events).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template("/v3/errors/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ErrorRetrieveResponse,
        )

    async def list(
        self,
        *,
        call_ids: SequenceNotStr[str] | Omit = omit,
        ending_before: str | Omit = omit,
        function_ids: SequenceNotStr[str] | Omit = omit,
        function_names: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        reference_id_substring: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        workflow_ids: SequenceNotStr[str] | Omit = omit,
        workflow_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ErrorListResponse:
        """
        **List terminal error events.**

        Returns error events produced by failed function calls within workflow
        executions. Non-error output events are excluded; use `GET /v3/outputs` to
        retrieve those.

        ## Filtering

        Filter by call, workflow, function, or reference ID. Multiple filters are ANDed
        together.

        Args:
          call_ids: Filter to errors from specific calls.

          reference_id_substring: Case-insensitive substring match against `referenceID`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/errors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "call_ids": call_ids,
                        "ending_before": ending_before,
                        "function_ids": function_ids,
                        "function_names": function_names,
                        "limit": limit,
                        "reference_ids": reference_ids,
                        "reference_id_substring": reference_id_substring,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                        "workflow_ids": workflow_ids,
                        "workflow_names": workflow_names,
                    },
                    error_list_params.ErrorListParams,
                ),
            ),
            cast_to=ErrorListResponse,
        )


class ErrorsResourceWithRawResponse:
    def __init__(self, errors: ErrorsResource) -> None:
        self._errors = errors

        self.retrieve = to_raw_response_wrapper(
            errors.retrieve,
        )
        self.list = to_raw_response_wrapper(
            errors.list,
        )


class AsyncErrorsResourceWithRawResponse:
    def __init__(self, errors: AsyncErrorsResource) -> None:
        self._errors = errors

        self.retrieve = async_to_raw_response_wrapper(
            errors.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            errors.list,
        )


class ErrorsResourceWithStreamingResponse:
    def __init__(self, errors: ErrorsResource) -> None:
        self._errors = errors

        self.retrieve = to_streamed_response_wrapper(
            errors.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            errors.list,
        )


class AsyncErrorsResourceWithStreamingResponse:
    def __init__(self, errors: AsyncErrorsResource) -> None:
        self._errors = errors

        self.retrieve = async_to_streamed_response_wrapper(
            errors.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            errors.list,
        )
