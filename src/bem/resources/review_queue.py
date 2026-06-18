# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import review_queue_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.review_queue_list_response import ReviewQueueListResponse

__all__ = ["ReviewQueueResource", "AsyncReviewQueueResource"]


class ReviewQueueResource(SyncAPIResource):
    """
    The reviewer-facing read surface for entity curation, available on the
    dashboard (JWT) only.

    - **`GET /v3/review-queue`** returns a cursor-paginated set of entities
      awaiting curation, scoped to your account+environment (and optional
      `bucket`). Each row is a full entity plus a small preview (up to 2) of
      its first mentions, so a reviewer can triage without opening every
      entity.

    Filters AND together. `status` (repeatable) defaults to the pre-terminal
    states `extracted` + `proposed` when omitted. `type` (repeatable `ety_…`
    IDs) matches the entity's *effective* type — its assigned type id, or, for
    entities with no assigned type, its bem-inferred type name. `assignedTo`
    (`me` or a `usr_…` ID) restricts to entities whose effective type the user
    reviews. `since` (RFC3339) filters by creation time. Pagination is
    cursor-based on `entityID` ascending; default limit 50, maximum 200.
    """

    @cached_property
    def with_raw_response(self) -> ReviewQueueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReviewQueueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReviewQueueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return ReviewQueueResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        assigned_to: str | Omit = omit,
        bucket: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        since: str | Omit = omit,
        status: SequenceNotStr[str] | Omit = omit,
        type: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReviewQueueListResponse:
        """
        **List entities awaiting curation, for a human reviewer's queue.**

        Returns a cursor-paginated set of entities scoped to your account+environment
        (and optional `bucket`), each carrying a small preview of its first mentions so
        a reviewer can triage without opening every entity. All filters AND together.

        - **`status`** (repeatable) restricts to the given lifecycle states. Omitting it
          defaults to the pre-terminal states `extracted` and `proposed`.
        - **`type`** (repeatable, `ety_...` IDs) matches the entity's _effective_ type:
          an entity matches when its assigned type is one of these IDs, or it has no
          assigned type and its bem-inferred type name matches one of them.
        - **`assignedTo`** (`me` or a `usr_...` ID) restricts to entities whose
          effective type the given user reviews. `me` resolves to the calling user.
        - **`since`** (RFC3339) restricts to entities created at or after the time.

        Pagination is cursor-based on `entityID` ascending; default limit is 50,
        maximum 200.

        Args:
          assigned_to: `me` or a `usr_...` ID — restrict to entities whose effective type that user
              reviews.

          bucket: Optional bucket public ID (`bkt_...`) to scope to. Omit for all buckets.

          cursor: Cursor — an `entityID` defining your place in the list.

          since: RFC3339 timestamp — restrict to entities created at or after this time.

          status: Restrict to these lifecycle states. Defaults to `extracted` + `proposed`.

          type: Restrict to entities whose effective type is one of these `ety_...` IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/review-queue",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assigned_to": assigned_to,
                        "bucket": bucket,
                        "cursor": cursor,
                        "limit": limit,
                        "since": since,
                        "status": status,
                        "type": type,
                    },
                    review_queue_list_params.ReviewQueueListParams,
                ),
            ),
            cast_to=ReviewQueueListResponse,
        )


class AsyncReviewQueueResource(AsyncAPIResource):
    """
    The reviewer-facing read surface for entity curation, available on the
    dashboard (JWT) only.

    - **`GET /v3/review-queue`** returns a cursor-paginated set of entities
      awaiting curation, scoped to your account+environment (and optional
      `bucket`). Each row is a full entity plus a small preview (up to 2) of
      its first mentions, so a reviewer can triage without opening every
      entity.

    Filters AND together. `status` (repeatable) defaults to the pre-terminal
    states `extracted` + `proposed` when omitted. `type` (repeatable `ety_…`
    IDs) matches the entity's *effective* type — its assigned type id, or, for
    entities with no assigned type, its bem-inferred type name. `assignedTo`
    (`me` or a `usr_…` ID) restricts to entities whose effective type the user
    reviews. `since` (RFC3339) filters by creation time. Pagination is
    cursor-based on `entityID` ascending; default limit 50, maximum 200.
    """

    @cached_property
    def with_raw_response(self) -> AsyncReviewQueueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReviewQueueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReviewQueueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncReviewQueueResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        assigned_to: str | Omit = omit,
        bucket: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        since: str | Omit = omit,
        status: SequenceNotStr[str] | Omit = omit,
        type: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReviewQueueListResponse:
        """
        **List entities awaiting curation, for a human reviewer's queue.**

        Returns a cursor-paginated set of entities scoped to your account+environment
        (and optional `bucket`), each carrying a small preview of its first mentions so
        a reviewer can triage without opening every entity. All filters AND together.

        - **`status`** (repeatable) restricts to the given lifecycle states. Omitting it
          defaults to the pre-terminal states `extracted` and `proposed`.
        - **`type`** (repeatable, `ety_...` IDs) matches the entity's _effective_ type:
          an entity matches when its assigned type is one of these IDs, or it has no
          assigned type and its bem-inferred type name matches one of them.
        - **`assignedTo`** (`me` or a `usr_...` ID) restricts to entities whose
          effective type the given user reviews. `me` resolves to the calling user.
        - **`since`** (RFC3339) restricts to entities created at or after the time.

        Pagination is cursor-based on `entityID` ascending; default limit is 50,
        maximum 200.

        Args:
          assigned_to: `me` or a `usr_...` ID — restrict to entities whose effective type that user
              reviews.

          bucket: Optional bucket public ID (`bkt_...`) to scope to. Omit for all buckets.

          cursor: Cursor — an `entityID` defining your place in the list.

          since: RFC3339 timestamp — restrict to entities created at or after this time.

          status: Restrict to these lifecycle states. Defaults to `extracted` + `proposed`.

          type: Restrict to entities whose effective type is one of these `ety_...` IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/review-queue",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "assigned_to": assigned_to,
                        "bucket": bucket,
                        "cursor": cursor,
                        "limit": limit,
                        "since": since,
                        "status": status,
                        "type": type,
                    },
                    review_queue_list_params.ReviewQueueListParams,
                ),
            ),
            cast_to=ReviewQueueListResponse,
        )


class ReviewQueueResourceWithRawResponse:
    def __init__(self, review_queue: ReviewQueueResource) -> None:
        self._review_queue = review_queue

        self.list = to_raw_response_wrapper(
            review_queue.list,
        )


class AsyncReviewQueueResourceWithRawResponse:
    def __init__(self, review_queue: AsyncReviewQueueResource) -> None:
        self._review_queue = review_queue

        self.list = async_to_raw_response_wrapper(
            review_queue.list,
        )


class ReviewQueueResourceWithStreamingResponse:
    def __init__(self, review_queue: ReviewQueueResource) -> None:
        self._review_queue = review_queue

        self.list = to_streamed_response_wrapper(
            review_queue.list,
        )


class AsyncReviewQueueResourceWithStreamingResponse:
    def __init__(self, review_queue: AsyncReviewQueueResource) -> None:
        self._review_queue = review_queue

        self.list = async_to_streamed_response_wrapper(
            review_queue.list,
        )
