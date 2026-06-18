# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import bucket_list_params, bucket_create_params, bucket_delete_params, bucket_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.bucket_list_response import BucketListResponse
from ..types.bucket_create_response import BucketCreateResponse
from ..types.bucket_update_response import BucketUpdateResponse
from ..types.bucket_retrieve_response import BucketRetrieveResponse

__all__ = ["BucketsResource", "AsyncBucketsResource"]


class BucketsResource(SyncAPIResource):
    """
    Buckets are named partitions of the knowledge graph within an
    account+environment. Entities, mentions, and relations are scoped to a
    bucket so a single account+environment can host multiple isolated graphs
    — for example one per data source or workspace.

    Every account+environment has exactly one **default** bucket, used by
    unscoped flows. The default bucket can be renamed but never deleted.

    Use these endpoints to create, list, fetch, rename, and delete buckets:

    - **`POST /v3/buckets`** creates a non-default bucket.
    - **`GET /v3/buckets`** lists buckets with cursor pagination
      (`startingAfter` / `endingBefore` over `bucketID`).
    - **`PATCH /v3/buckets/{bucketID}`** updates `name` and/or `description`.
    - **`DELETE /v3/buckets/{bucketID}`** soft-deletes a bucket. A non-empty
      bucket is rejected with `409 Conflict` unless `?cascade=true` is
      passed; the default bucket can never be deleted.
    """

    @cached_property
    def with_raw_response(self) -> BucketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BucketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BucketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return BucketsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BucketCreateResponse:
        """Create a Bucket

        Args:
          name: Bucket name.

        Required and unique within the account+environment.

          description: Optional description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/buckets",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                bucket_create_params.BucketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BucketCreateResponse,
        )

    def retrieve(
        self,
        bucket_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BucketRetrieveResponse:
        """
        Get a Bucket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_id:
            raise ValueError(f"Expected a non-empty value for `bucket_id` but received {bucket_id!r}")
        return self._get(
            path_template("/v3/buckets/{bucket_id}", bucket_id=bucket_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BucketRetrieveResponse,
        )

    def update(
        self,
        bucket_id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BucketUpdateResponse:
        """
        Update a Bucket

        Args:
          description: New description.

          name: New name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_id:
            raise ValueError(f"Expected a non-empty value for `bucket_id` but received {bucket_id!r}")
        return self._patch(
            path_template("/v3/buckets/{bucket_id}", bucket_id=bucket_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                bucket_update_params.BucketUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BucketUpdateResponse,
        )

    def list(
        self,
        *,
        ending_before: str | Omit = omit,
        limit: int | Omit = omit,
        name_substring: str | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BucketListResponse:
        """
        List Buckets

        Args:
          ending_before: Cursor: return buckets whose `bucketID` sorts before this value.

          limit: Maximum number of buckets to return (default 50, max 200).

          name_substring: Case-insensitive substring match on the bucket name.

          starting_after: Cursor: return buckets whose `bucketID` sorts after this value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/buckets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "limit": limit,
                        "name_substring": name_substring,
                        "starting_after": starting_after,
                    },
                    bucket_list_params.BucketListParams,
                ),
            ),
            cast_to=BucketListResponse,
        )

    def delete(
        self,
        bucket_id: str,
        *,
        cascade: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Bucket

        Args:
          cascade: When `true`, delete the bucket even if it still contains entities (the entities
              are removed along with it). When omitted or `false`, the request is rejected
              with `409 Conflict` if the bucket is non-empty.

              The default bucket can never be deleted regardless of this flag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_id:
            raise ValueError(f"Expected a non-empty value for `bucket_id` but received {bucket_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/buckets/{bucket_id}", bucket_id=bucket_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cascade": cascade}, bucket_delete_params.BucketDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncBucketsResource(AsyncAPIResource):
    """
    Buckets are named partitions of the knowledge graph within an
    account+environment. Entities, mentions, and relations are scoped to a
    bucket so a single account+environment can host multiple isolated graphs
    — for example one per data source or workspace.

    Every account+environment has exactly one **default** bucket, used by
    unscoped flows. The default bucket can be renamed but never deleted.

    Use these endpoints to create, list, fetch, rename, and delete buckets:

    - **`POST /v3/buckets`** creates a non-default bucket.
    - **`GET /v3/buckets`** lists buckets with cursor pagination
      (`startingAfter` / `endingBefore` over `bucketID`).
    - **`PATCH /v3/buckets/{bucketID}`** updates `name` and/or `description`.
    - **`DELETE /v3/buckets/{bucketID}`** soft-deletes a bucket. A non-empty
      bucket is rejected with `409 Conflict` unless `?cascade=true` is
      passed; the default bucket can never be deleted.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBucketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBucketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBucketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncBucketsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BucketCreateResponse:
        """Create a Bucket

        Args:
          name: Bucket name.

        Required and unique within the account+environment.

          description: Optional description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/buckets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                bucket_create_params.BucketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BucketCreateResponse,
        )

    async def retrieve(
        self,
        bucket_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BucketRetrieveResponse:
        """
        Get a Bucket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_id:
            raise ValueError(f"Expected a non-empty value for `bucket_id` but received {bucket_id!r}")
        return await self._get(
            path_template("/v3/buckets/{bucket_id}", bucket_id=bucket_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BucketRetrieveResponse,
        )

    async def update(
        self,
        bucket_id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BucketUpdateResponse:
        """
        Update a Bucket

        Args:
          description: New description.

          name: New name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_id:
            raise ValueError(f"Expected a non-empty value for `bucket_id` but received {bucket_id!r}")
        return await self._patch(
            path_template("/v3/buckets/{bucket_id}", bucket_id=bucket_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                bucket_update_params.BucketUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BucketUpdateResponse,
        )

    async def list(
        self,
        *,
        ending_before: str | Omit = omit,
        limit: int | Omit = omit,
        name_substring: str | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BucketListResponse:
        """
        List Buckets

        Args:
          ending_before: Cursor: return buckets whose `bucketID` sorts before this value.

          limit: Maximum number of buckets to return (default 50, max 200).

          name_substring: Case-insensitive substring match on the bucket name.

          starting_after: Cursor: return buckets whose `bucketID` sorts after this value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/buckets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ending_before": ending_before,
                        "limit": limit,
                        "name_substring": name_substring,
                        "starting_after": starting_after,
                    },
                    bucket_list_params.BucketListParams,
                ),
            ),
            cast_to=BucketListResponse,
        )

    async def delete(
        self,
        bucket_id: str,
        *,
        cascade: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Bucket

        Args:
          cascade: When `true`, delete the bucket even if it still contains entities (the entities
              are removed along with it). When omitted or `false`, the request is rejected
              with `409 Conflict` if the bucket is non-empty.

              The default bucket can never be deleted regardless of this flag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_id:
            raise ValueError(f"Expected a non-empty value for `bucket_id` but received {bucket_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/buckets/{bucket_id}", bucket_id=bucket_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cascade": cascade}, bucket_delete_params.BucketDeleteParams),
            ),
            cast_to=NoneType,
        )


class BucketsResourceWithRawResponse:
    def __init__(self, buckets: BucketsResource) -> None:
        self._buckets = buckets

        self.create = to_raw_response_wrapper(
            buckets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            buckets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            buckets.update,
        )
        self.list = to_raw_response_wrapper(
            buckets.list,
        )
        self.delete = to_raw_response_wrapper(
            buckets.delete,
        )


class AsyncBucketsResourceWithRawResponse:
    def __init__(self, buckets: AsyncBucketsResource) -> None:
        self._buckets = buckets

        self.create = async_to_raw_response_wrapper(
            buckets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            buckets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            buckets.update,
        )
        self.list = async_to_raw_response_wrapper(
            buckets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            buckets.delete,
        )


class BucketsResourceWithStreamingResponse:
    def __init__(self, buckets: BucketsResource) -> None:
        self._buckets = buckets

        self.create = to_streamed_response_wrapper(
            buckets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            buckets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            buckets.update,
        )
        self.list = to_streamed_response_wrapper(
            buckets.list,
        )
        self.delete = to_streamed_response_wrapper(
            buckets.delete,
        )


class AsyncBucketsResourceWithStreamingResponse:
    def __init__(self, buckets: AsyncBucketsResource) -> None:
        self._buckets = buckets

        self.create = async_to_streamed_response_wrapper(
            buckets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            buckets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            buckets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            buckets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            buckets.delete,
        )
