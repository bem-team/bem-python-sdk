# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import event_submit_feedback_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.event_submit_feedback_response import EventSubmitFeedbackResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    """Submit training corrections for `extract`, `classify`, and `join` events.

    Feedback is event-centric — each correction is attached to an event by its `eventID`,
    and the server resolves the correct underlying storage (extract/join transformations
    or classify route events) from the event's function type.

    Split and enrich function types do not support feedback.
    """

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def submit_feedback(
        self,
        event_id: str,
        *,
        correction: object,
        order_matching: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventSubmitFeedbackResponse:
        """
        **Submit a correction for an event.**

        Accepts training corrections for `extract`, `classify`, and `join` events. For
        extract/join events, `correction` is a JSON object matching the function's
        output schema. For classify events, `correction` is a JSON string matching one
        of the function version's declared classifications.

        Submitting feedback again for the same event overwrites the previous correction.

        Unsupported function types (split, enrich) return `400`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._post(
            path_template("/v3/events/{event_id}/feedback", event_id=event_id),
            body=maybe_transform(
                {
                    "correction": correction,
                    "order_matching": order_matching,
                },
                event_submit_feedback_params.EventSubmitFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubmitFeedbackResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    """Submit training corrections for `extract`, `classify`, and `join` events.

    Feedback is event-centric — each correction is attached to an event by its `eventID`,
    and the server resolves the correct underlying storage (extract/join transformations
    or classify route events) from the event's function type.

    Split and enrich function types do not support feedback.
    """

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def submit_feedback(
        self,
        event_id: str,
        *,
        correction: object,
        order_matching: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventSubmitFeedbackResponse:
        """
        **Submit a correction for an event.**

        Accepts training corrections for `extract`, `classify`, and `join` events. For
        extract/join events, `correction` is a JSON object matching the function's
        output schema. For classify events, `correction` is a JSON string matching one
        of the function version's declared classifications.

        Submitting feedback again for the same event overwrites the previous correction.

        Unsupported function types (split, enrich) return `400`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._post(
            path_template("/v3/events/{event_id}/feedback", event_id=event_id),
            body=await async_maybe_transform(
                {
                    "correction": correction,
                    "order_matching": order_matching,
                },
                event_submit_feedback_params.EventSubmitFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubmitFeedbackResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.submit_feedback = to_raw_response_wrapper(
            events.submit_feedback,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.submit_feedback = async_to_raw_response_wrapper(
            events.submit_feedback,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.submit_feedback = to_streamed_response_wrapper(
            events.submit_feedback,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.submit_feedback = async_to_streamed_response_wrapper(
            events.submit_feedback,
        )
