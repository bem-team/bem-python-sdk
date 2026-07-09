# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import entity_type_list_params, entity_type_create_params, entity_type_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .reviewers import (
    ReviewersResource,
    AsyncReviewersResource,
    ReviewersResourceWithRawResponse,
    AsyncReviewersResourceWithRawResponse,
    ReviewersResourceWithStreamingResponse,
    AsyncReviewersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.entity_type import EntityType
from ...types.entity_type_list_response import EntityTypeListResponse

__all__ = ["EntityTypesResource", "AsyncEntityTypesResource"]


class EntityTypesResource(SyncAPIResource):
    """
    Entity Types are the customer-defined taxonomy for the knowledge graph,
    scoped to an account+environment. Each type has a unique, immutable name
    and can be organised into hierarchies via `parentTypeID`. A type may
    carry per-type structured attribute metadata in `attributeSchema` (for
    example `{"unit": "mg", "range": [0, 100]}`).

    Use these endpoints to create, list, fetch, update, and delete entity
    types:

    - **`POST /v3/entity-types`** creates a type, optionally under a parent.
    - **`GET /v3/entity-types`** lists types with cursor pagination
      (`startingAfter` / `endingBefore` over `typeID`) and an optional
      `parentTypeId` filter for direct children.
    - **`PATCH /v3/entity-types/{typeID}`** updates `description`,
      `parentTypeID`, and/or `attributeSchema`. The `name` is immutable.
    - **`DELETE /v3/entity-types/{typeID}`** soft-deletes a type. The request
      is rejected with `409 Conflict` while any live entity is assigned to
      the type or any live child type points at it.
    """

    @cached_property
    def reviewers(self) -> ReviewersResource:
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
        return ReviewersResource(self._client)

    @cached_property
    def with_raw_response(self) -> EntityTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EntityTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntityTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return EntityTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        attribute_schema: object | Omit = omit,
        description: str | Omit = omit,
        parent_type_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityType:
        """Create an Entity Type

        Args:
          name: Type name.

        Required and unique within the account+environment.

          attribute_schema: Optional per-type structured attribute metadata.

          description: Optional description.

          parent_type_id: Optional public ID (`ety_...`) of the parent type. Must belong to the same
              account+environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/entity-types",
            body=maybe_transform(
                {
                    "name": name,
                    "attribute_schema": attribute_schema,
                    "description": description,
                    "parent_type_id": parent_type_id,
                },
                entity_type_create_params.EntityTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityType,
        )

    def retrieve(
        self,
        type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityType:
        """
        Get an Entity Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        return self._get(
            path_template("/v3/entity-types/{type_id}", type_id=type_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityType,
        )

    def update(
        self,
        type_id: str,
        *,
        attribute_schema: object | Omit = omit,
        description: str | Omit = omit,
        parent_type_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityType:
        """
        Update an Entity Type

        Args:
          attribute_schema: New per-type structured attribute metadata.

          description: New description.

          parent_type_id: New parent type public ID (`ety_...`), or an empty string to clear the parent
              (promote to top-level). Must belong to the same account+environment and may not
              be the type itself.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        return self._patch(
            path_template("/v3/entity-types/{type_id}", type_id=type_id),
            body=maybe_transform(
                {
                    "attribute_schema": attribute_schema,
                    "description": description,
                    "parent_type_id": parent_type_id,
                },
                entity_type_update_params.EntityTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityType,
        )

    def list(
        self,
        *,
        ending_before: str | Omit = omit,
        limit: int | Omit = omit,
        parent_type_id: str | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityTypeListResponse:
        """
        List Entity Types

        Args:
          ending_before: Cursor: return types whose `typeID` sorts before this value.

          limit: Maximum number of entity types to return (default 50, max 200).

          parent_type_id: Filter to the direct children of this parent type (`ety_...`).

          starting_after: Cursor: return types whose `typeID` sorts after this value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/entity-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "limit": limit,
                        "parent_type_id": parent_type_id,
                        "starting_after": starting_after,
                    },
                    entity_type_list_params.EntityTypeListParams,
                ),
            ),
            cast_to=EntityTypeListResponse,
        )

    def delete(
        self,
        type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an Entity Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/entity-types/{type_id}", type_id=type_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEntityTypesResource(AsyncAPIResource):
    """
    Entity Types are the customer-defined taxonomy for the knowledge graph,
    scoped to an account+environment. Each type has a unique, immutable name
    and can be organised into hierarchies via `parentTypeID`. A type may
    carry per-type structured attribute metadata in `attributeSchema` (for
    example `{"unit": "mg", "range": [0, 100]}`).

    Use these endpoints to create, list, fetch, update, and delete entity
    types:

    - **`POST /v3/entity-types`** creates a type, optionally under a parent.
    - **`GET /v3/entity-types`** lists types with cursor pagination
      (`startingAfter` / `endingBefore` over `typeID`) and an optional
      `parentTypeId` filter for direct children.
    - **`PATCH /v3/entity-types/{typeID}`** updates `description`,
      `parentTypeID`, and/or `attributeSchema`. The `name` is immutable.
    - **`DELETE /v3/entity-types/{typeID}`** soft-deletes a type. The request
      is rejected with `409 Conflict` while any live entity is assigned to
      the type or any live child type points at it.
    """

    @cached_property
    def reviewers(self) -> AsyncReviewersResource:
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
        return AsyncReviewersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEntityTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEntityTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntityTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncEntityTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        attribute_schema: object | Omit = omit,
        description: str | Omit = omit,
        parent_type_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityType:
        """Create an Entity Type

        Args:
          name: Type name.

        Required and unique within the account+environment.

          attribute_schema: Optional per-type structured attribute metadata.

          description: Optional description.

          parent_type_id: Optional public ID (`ety_...`) of the parent type. Must belong to the same
              account+environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/entity-types",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "attribute_schema": attribute_schema,
                    "description": description,
                    "parent_type_id": parent_type_id,
                },
                entity_type_create_params.EntityTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityType,
        )

    async def retrieve(
        self,
        type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityType:
        """
        Get an Entity Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        return await self._get(
            path_template("/v3/entity-types/{type_id}", type_id=type_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityType,
        )

    async def update(
        self,
        type_id: str,
        *,
        attribute_schema: object | Omit = omit,
        description: str | Omit = omit,
        parent_type_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityType:
        """
        Update an Entity Type

        Args:
          attribute_schema: New per-type structured attribute metadata.

          description: New description.

          parent_type_id: New parent type public ID (`ety_...`), or an empty string to clear the parent
              (promote to top-level). Must belong to the same account+environment and may not
              be the type itself.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        return await self._patch(
            path_template("/v3/entity-types/{type_id}", type_id=type_id),
            body=await async_maybe_transform(
                {
                    "attribute_schema": attribute_schema,
                    "description": description,
                    "parent_type_id": parent_type_id,
                },
                entity_type_update_params.EntityTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityType,
        )

    async def list(
        self,
        *,
        ending_before: str | Omit = omit,
        limit: int | Omit = omit,
        parent_type_id: str | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityTypeListResponse:
        """
        List Entity Types

        Args:
          ending_before: Cursor: return types whose `typeID` sorts before this value.

          limit: Maximum number of entity types to return (default 50, max 200).

          parent_type_id: Filter to the direct children of this parent type (`ety_...`).

          starting_after: Cursor: return types whose `typeID` sorts after this value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/entity-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ending_before": ending_before,
                        "limit": limit,
                        "parent_type_id": parent_type_id,
                        "starting_after": starting_after,
                    },
                    entity_type_list_params.EntityTypeListParams,
                ),
            ),
            cast_to=EntityTypeListResponse,
        )

    async def delete(
        self,
        type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an Entity Type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_id:
            raise ValueError(f"Expected a non-empty value for `type_id` but received {type_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/entity-types/{type_id}", type_id=type_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EntityTypesResourceWithRawResponse:
    def __init__(self, entity_types: EntityTypesResource) -> None:
        self._entity_types = entity_types

        self.create = to_raw_response_wrapper(
            entity_types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            entity_types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            entity_types.update,
        )
        self.list = to_raw_response_wrapper(
            entity_types.list,
        )
        self.delete = to_raw_response_wrapper(
            entity_types.delete,
        )

    @cached_property
    def reviewers(self) -> ReviewersResourceWithRawResponse:
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
        return ReviewersResourceWithRawResponse(self._entity_types.reviewers)


class AsyncEntityTypesResourceWithRawResponse:
    def __init__(self, entity_types: AsyncEntityTypesResource) -> None:
        self._entity_types = entity_types

        self.create = async_to_raw_response_wrapper(
            entity_types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            entity_types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            entity_types.update,
        )
        self.list = async_to_raw_response_wrapper(
            entity_types.list,
        )
        self.delete = async_to_raw_response_wrapper(
            entity_types.delete,
        )

    @cached_property
    def reviewers(self) -> AsyncReviewersResourceWithRawResponse:
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
        return AsyncReviewersResourceWithRawResponse(self._entity_types.reviewers)


class EntityTypesResourceWithStreamingResponse:
    def __init__(self, entity_types: EntityTypesResource) -> None:
        self._entity_types = entity_types

        self.create = to_streamed_response_wrapper(
            entity_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            entity_types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            entity_types.update,
        )
        self.list = to_streamed_response_wrapper(
            entity_types.list,
        )
        self.delete = to_streamed_response_wrapper(
            entity_types.delete,
        )

    @cached_property
    def reviewers(self) -> ReviewersResourceWithStreamingResponse:
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
        return ReviewersResourceWithStreamingResponse(self._entity_types.reviewers)


class AsyncEntityTypesResourceWithStreamingResponse:
    def __init__(self, entity_types: AsyncEntityTypesResource) -> None:
        self._entity_types = entity_types

        self.create = async_to_streamed_response_wrapper(
            entity_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            entity_types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            entity_types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            entity_types.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            entity_types.delete,
        )

    @cached_property
    def reviewers(self) -> AsyncReviewersResourceWithStreamingResponse:
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
        return AsyncReviewersResourceWithStreamingResponse(self._entity_types.reviewers)
