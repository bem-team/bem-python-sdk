# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.entity_types import reviewer_assign_params
from ...types.entity_types.reviewer_list_response import ReviewerListResponse
from ...types.entity_types.reviewer_assign_response import ReviewerAssignResponse

__all__ = ["ReviewersResource", "AsyncReviewersResource"]


class ReviewersResource(SyncAPIResource):
    """
    Reviewer assignments link users to the entity types they are responsible
    for reviewing, scoped to an account+environment. These are dashboard-only
    endpoints: an assignment needs a user identity, which only the dashboard
    (JWT) surface carries.

    - **`POST /v3/entity-types/{typeID}/reviewers`** assigns a user as a
      reviewer of the type. The assignment is idempotent: re-assigning an
      existing reviewer returns the existing assignment. Requires the `admin`
      role.
    - **`GET /v3/entity-types/{typeID}/reviewers`** lists the users assigned
      to review the type, with each user's email and role. Requires the
      `operator` role.
    - **`DELETE /v3/entity-types/{typeID}/reviewers/{userID}`** removes an
      assignment. Requires the `admin` role.
    - **`GET /v3/users/{userID}/reviewer-assignments`** is the reverse lookup:
      the entity types a user reviews. A user may read their own assignments;
      reading another user's assignments requires the `admin` role.
    """

    @cached_property
    def with_raw_response(self) -> ReviewersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReviewersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReviewersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return ReviewersResourceWithStreamingResponse(self)

    def list(
        self,
        type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReviewerListResponse:
        """
        List Reviewers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        return self._get(
            path_template("/v3/entity-types/{type_id}/reviewers", type_id=type_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReviewerListResponse,
        )

    def assign(
        self,
        type_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReviewerAssignResponse:
        """Assign a Reviewer

        Args:
          user_id: Public ID (`usr_...`) of the user to assign.

        Must belong to the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        return self._post(
            path_template("/v3/entity-types/{type_id}/reviewers", type_id=type_id),
            body=maybe_transform({"user_id": user_id}, reviewer_assign_params.ReviewerAssignParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReviewerAssignResponse,
        )

    def remove(
        self,
        user_id: str,
        *,
        type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a Reviewer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/entity-types/{type_id}/reviewers/{user_id}", type_id=type_id, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncReviewersResource(AsyncAPIResource):
    """
    Reviewer assignments link users to the entity types they are responsible
    for reviewing, scoped to an account+environment. These are dashboard-only
    endpoints: an assignment needs a user identity, which only the dashboard
    (JWT) surface carries.

    - **`POST /v3/entity-types/{typeID}/reviewers`** assigns a user as a
      reviewer of the type. The assignment is idempotent: re-assigning an
      existing reviewer returns the existing assignment. Requires the `admin`
      role.
    - **`GET /v3/entity-types/{typeID}/reviewers`** lists the users assigned
      to review the type, with each user's email and role. Requires the
      `operator` role.
    - **`DELETE /v3/entity-types/{typeID}/reviewers/{userID}`** removes an
      assignment. Requires the `admin` role.
    - **`GET /v3/users/{userID}/reviewer-assignments`** is the reverse lookup:
      the entity types a user reviews. A user may read their own assignments;
      reading another user's assignments requires the `admin` role.
    """

    @cached_property
    def with_raw_response(self) -> AsyncReviewersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReviewersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReviewersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncReviewersResourceWithStreamingResponse(self)

    async def list(
        self,
        type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReviewerListResponse:
        """
        List Reviewers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        return await self._get(
            path_template("/v3/entity-types/{type_id}/reviewers", type_id=type_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReviewerListResponse,
        )

    async def assign(
        self,
        type_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReviewerAssignResponse:
        """Assign a Reviewer

        Args:
          user_id: Public ID (`usr_...`) of the user to assign.

        Must belong to the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        return await self._post(
            path_template("/v3/entity-types/{type_id}/reviewers", type_id=type_id),
            body=await async_maybe_transform({"user_id": user_id}, reviewer_assign_params.ReviewerAssignParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReviewerAssignResponse,
        )

    async def remove(
        self,
        user_id: str,
        *,
        type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a Reviewer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/entity-types/{type_id}/reviewers/{user_id}", type_id=type_id, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ReviewersResourceWithRawResponse:
    def __init__(self, reviewers: ReviewersResource) -> None:
        self._reviewers = reviewers

        self.list = to_raw_response_wrapper(
            reviewers.list,
        )
        self.assign = to_raw_response_wrapper(
            reviewers.assign,
        )
        self.remove = to_raw_response_wrapper(
            reviewers.remove,
        )


class AsyncReviewersResourceWithRawResponse:
    def __init__(self, reviewers: AsyncReviewersResource) -> None:
        self._reviewers = reviewers

        self.list = async_to_raw_response_wrapper(
            reviewers.list,
        )
        self.assign = async_to_raw_response_wrapper(
            reviewers.assign,
        )
        self.remove = async_to_raw_response_wrapper(
            reviewers.remove,
        )


class ReviewersResourceWithStreamingResponse:
    def __init__(self, reviewers: ReviewersResource) -> None:
        self._reviewers = reviewers

        self.list = to_streamed_response_wrapper(
            reviewers.list,
        )
        self.assign = to_streamed_response_wrapper(
            reviewers.assign,
        )
        self.remove = to_streamed_response_wrapper(
            reviewers.remove,
        )


class AsyncReviewersResourceWithStreamingResponse:
    def __init__(self, reviewers: AsyncReviewersResource) -> None:
        self._reviewers = reviewers

        self.list = async_to_streamed_response_wrapper(
            reviewers.list,
        )
        self.assign = async_to_streamed_response_wrapper(
            reviewers.assign,
        )
        self.remove = async_to_streamed_response_wrapper(
            reviewers.remove,
        )
