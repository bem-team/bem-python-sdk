# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.user_list_reviewer_assignments_response import UserListReviewerAssignmentsResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
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
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def list_reviewer_assignments(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListReviewerAssignmentsResponse:
        """
        List a User's Reviewer Assignments

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v3/users/{user_id}/reviewer-assignments", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListReviewerAssignmentsResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def list_reviewer_assignments(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListReviewerAssignmentsResponse:
        """
        List a User's Reviewer Assignments

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v3/users/{user_id}/reviewer-assignments", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListReviewerAssignmentsResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list_reviewer_assignments = to_raw_response_wrapper(
            users.list_reviewer_assignments,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list_reviewer_assignments = async_to_raw_response_wrapper(
            users.list_reviewer_assignments,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list_reviewer_assignments = to_streamed_response_wrapper(
            users.list_reviewer_assignments,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list_reviewer_assignments = async_to_streamed_response_wrapper(
            users.list_reviewer_assignments,
        )
