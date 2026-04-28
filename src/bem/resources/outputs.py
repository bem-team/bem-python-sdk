# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, cast
from typing_extensions import Literal

import httpx

from ..types import output_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOutputsPage, AsyncOutputsPage
from ..types.event import Event
from .._base_client import AsyncPaginator, make_request_options
from ..types.output_retrieve_response import OutputRetrieveResponse

__all__ = ["OutputsResource", "AsyncOutputsResource"]


class OutputsResource(SyncAPIResource):
    """Retrieve terminal non-error output events from workflow calls.

    Outputs are events produced by successful terminal function steps — steps that completed
    without errors and did not spawn further downstream function calls. A single workflow call
    may produce multiple outputs (e.g. from a split-then-transform pipeline).

    Outputs and errors from the same call are not mutually exclusive: a partially-completed
    workflow may have both.

    Use `GET /v3/outputs` to list outputs across calls, or `GET /v3/outputs/{eventID}` to
    retrieve a specific output. To get outputs scoped to a single call, filter by `callIDs`.
    """

    @cached_property
    def with_raw_response(self) -> OutputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OutputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return OutputsResourceWithStreamingResponse(self)

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
    ) -> OutputRetrieveResponse:
        """
        **Retrieve a single output event by ID.**

        Fetches any non-error event by its `eventID`. Returns `404` if the event does
        not exist or if it is an error event (use `GET /v3/errors/{eventID}` for those).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template("/v3/outputs/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutputRetrieveResponse,
        )

    def list(
        self,
        *,
        call_ids: SequenceNotStr[str] | Omit = omit,
        ending_before: str | Omit = omit,
        event_ids: SequenceNotStr[str] | Omit = omit,
        function_ids: SequenceNotStr[str] | Omit = omit,
        function_names: SequenceNotStr[str] | Omit = omit,
        function_version_nums: Iterable[int] | Omit = omit,
        include_intermediate: bool | Omit = omit,
        is_labelled: bool | Omit = omit,
        is_regression: bool | Omit = omit,
        limit: int | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        reference_id_substring: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        transformation_ids: SequenceNotStr[str] | Omit = omit,
        workflow_ids: SequenceNotStr[str] | Omit = omit,
        workflow_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOutputsPage[Event]:
        """
        **List terminal non-error output events.**

        Returns events that represent successful terminal outputs — primary events
        (non-split-collection) that did not trigger any downstream function calls. Error
        events are excluded; use `GET /v3/errors` to retrieve those.

        ## Intermediate Events

        By default, intermediate events (those that spawned a downstream function call
        in a multi-step workflow) are excluded. Pass `includeIntermediate=true` to
        include them.

        ## Filtering

        Filter by call, workflow, function, or reference ID. Multiple filters are ANDed
        together.

        Args:
          call_ids: Filter to outputs from specific calls.

          event_ids: Filter to specific output events by their event IDs (KSUIDs).

          function_version_nums: Filter to specific function version numbers.

          include_intermediate: When `true`, includes intermediate events (those that spawned a downstream
              function call). Default: `false`.

          is_labelled: If `true`, only outputs with a corrected (labelled) payload. If `false`, only
              outputs that are not labelled. If omitted, no filter is applied.

          is_regression: If `true`, only regression-marked outputs. If `false`, only non-regression
              outputs. If omitted, no filter is applied.

              Note: clients migrating from `/v1-beta/transformations` should pass
              `isRegression=false` explicitly to preserve the legacy default (regressions
              hidden unless explicitly requested).

          reference_id_substring: Case-insensitive substring match against `referenceID`.

          transformation_ids: Filter by legacy transformation IDs. Provided for backwards compatibility with
              clients migrating from `/v1-beta/transformations`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/outputs",
            page=SyncOutputsPage[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "call_ids": call_ids,
                        "ending_before": ending_before,
                        "event_ids": event_ids,
                        "function_ids": function_ids,
                        "function_names": function_names,
                        "function_version_nums": function_version_nums,
                        "include_intermediate": include_intermediate,
                        "is_labelled": is_labelled,
                        "is_regression": is_regression,
                        "limit": limit,
                        "reference_ids": reference_ids,
                        "reference_id_substring": reference_id_substring,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                        "transformation_ids": transformation_ids,
                        "workflow_ids": workflow_ids,
                        "workflow_names": workflow_names,
                    },
                    output_list_params.OutputListParams,
                ),
            ),
            model=cast(Any, Event),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncOutputsResource(AsyncAPIResource):
    """Retrieve terminal non-error output events from workflow calls.

    Outputs are events produced by successful terminal function steps — steps that completed
    without errors and did not spawn further downstream function calls. A single workflow call
    may produce multiple outputs (e.g. from a split-then-transform pipeline).

    Outputs and errors from the same call are not mutually exclusive: a partially-completed
    workflow may have both.

    Use `GET /v3/outputs` to list outputs across calls, or `GET /v3/outputs/{eventID}` to
    retrieve a specific output. To get outputs scoped to a single call, filter by `callIDs`.
    """

    @cached_property
    def with_raw_response(self) -> AsyncOutputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOutputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncOutputsResourceWithStreamingResponse(self)

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
    ) -> OutputRetrieveResponse:
        """
        **Retrieve a single output event by ID.**

        Fetches any non-error event by its `eventID`. Returns `404` if the event does
        not exist or if it is an error event (use `GET /v3/errors/{eventID}` for those).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template("/v3/outputs/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutputRetrieveResponse,
        )

    def list(
        self,
        *,
        call_ids: SequenceNotStr[str] | Omit = omit,
        ending_before: str | Omit = omit,
        event_ids: SequenceNotStr[str] | Omit = omit,
        function_ids: SequenceNotStr[str] | Omit = omit,
        function_names: SequenceNotStr[str] | Omit = omit,
        function_version_nums: Iterable[int] | Omit = omit,
        include_intermediate: bool | Omit = omit,
        is_labelled: bool | Omit = omit,
        is_regression: bool | Omit = omit,
        limit: int | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        reference_id_substring: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        transformation_ids: SequenceNotStr[str] | Omit = omit,
        workflow_ids: SequenceNotStr[str] | Omit = omit,
        workflow_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Event, AsyncOutputsPage[Event]]:
        """
        **List terminal non-error output events.**

        Returns events that represent successful terminal outputs — primary events
        (non-split-collection) that did not trigger any downstream function calls. Error
        events are excluded; use `GET /v3/errors` to retrieve those.

        ## Intermediate Events

        By default, intermediate events (those that spawned a downstream function call
        in a multi-step workflow) are excluded. Pass `includeIntermediate=true` to
        include them.

        ## Filtering

        Filter by call, workflow, function, or reference ID. Multiple filters are ANDed
        together.

        Args:
          call_ids: Filter to outputs from specific calls.

          event_ids: Filter to specific output events by their event IDs (KSUIDs).

          function_version_nums: Filter to specific function version numbers.

          include_intermediate: When `true`, includes intermediate events (those that spawned a downstream
              function call). Default: `false`.

          is_labelled: If `true`, only outputs with a corrected (labelled) payload. If `false`, only
              outputs that are not labelled. If omitted, no filter is applied.

          is_regression: If `true`, only regression-marked outputs. If `false`, only non-regression
              outputs. If omitted, no filter is applied.

              Note: clients migrating from `/v1-beta/transformations` should pass
              `isRegression=false` explicitly to preserve the legacy default (regressions
              hidden unless explicitly requested).

          reference_id_substring: Case-insensitive substring match against `referenceID`.

          transformation_ids: Filter by legacy transformation IDs. Provided for backwards compatibility with
              clients migrating from `/v1-beta/transformations`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/outputs",
            page=AsyncOutputsPage[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "call_ids": call_ids,
                        "ending_before": ending_before,
                        "event_ids": event_ids,
                        "function_ids": function_ids,
                        "function_names": function_names,
                        "function_version_nums": function_version_nums,
                        "include_intermediate": include_intermediate,
                        "is_labelled": is_labelled,
                        "is_regression": is_regression,
                        "limit": limit,
                        "reference_ids": reference_ids,
                        "reference_id_substring": reference_id_substring,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                        "transformation_ids": transformation_ids,
                        "workflow_ids": workflow_ids,
                        "workflow_names": workflow_names,
                    },
                    output_list_params.OutputListParams,
                ),
            ),
            model=cast(Any, Event),  # Union types cannot be passed in as arguments in the type system
        )


class OutputsResourceWithRawResponse:
    def __init__(self, outputs: OutputsResource) -> None:
        self._outputs = outputs

        self.retrieve = to_raw_response_wrapper(
            outputs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            outputs.list,
        )


class AsyncOutputsResourceWithRawResponse:
    def __init__(self, outputs: AsyncOutputsResource) -> None:
        self._outputs = outputs

        self.retrieve = async_to_raw_response_wrapper(
            outputs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            outputs.list,
        )


class OutputsResourceWithStreamingResponse:
    def __init__(self, outputs: OutputsResource) -> None:
        self._outputs = outputs

        self.retrieve = to_streamed_response_wrapper(
            outputs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            outputs.list,
        )


class AsyncOutputsResourceWithStreamingResponse:
    def __init__(self, outputs: AsyncOutputsResource) -> None:
        self._outputs = outputs

        self.retrieve = async_to_streamed_response_wrapper(
            outputs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            outputs.list,
        )
