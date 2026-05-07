# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.collection import Collection
from ...types.collections import item_add_params, item_delete_params, item_update_params, item_retrieve_params
from ...types.collections.item_add_response import ItemAddResponse
from ...types.collections.item_update_response import ItemUpdateResponse

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
    """
    Collections are named groups of embedded items used by Enrich functions for semantic search.

    Each collection is referenced by a `collectionName`, which supports dot notation for
    hierarchical paths (e.g. `customers.premium.vip`). Names must contain only letters,
    digits, underscores, and dots, and each segment must start with a letter or underscore.

    ## Items

    Items carry either a string or a JSON object in their `data` field. When items are added
    or updated, their `data` is embedded asynchronously — `POST /v3/collections/items` and
    `PUT /v3/collections/items` return immediately with a `pending` status and an `eventID`
    that can be correlated with webhook notifications once processing completes.

    ## Listing and hierarchy

    Use `GET /v3/collections` with `parentCollectionName` to list collections under a path,
    or `collectionNameSearch` for a case-insensitive substring match. `GET /v3/collections/items`
    retrieves a specific collection's items; pass `includeSubcollections=true` to fold in items
    from all descendant collections.

    ## Token counting

    Use `POST /v3/collections/token-count` to check whether texts fit within the embedding
    model's 8,192-token-per-text limit before submitting them for embedding.
    """

    @cached_property
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return ItemsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        collection_name: str,
        include_subcollections: bool | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Collection:
        """Get a Collection

        Args:
          collection_name: The name/path of the collection.

        Must use only letters, digits, underscores, and
              dots. Each segment must start with a letter or underscore.

          include_subcollections: When true, includes items from all subcollections under the specified collection
              path. For example, querying "customers" with this flag will return items from
              "customers", "customers.premium", "customers.premium.vip", etc.

          limit: Number of items per page

          page: Page number for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/collections/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_name": collection_name,
                        "include_subcollections": include_subcollections,
                        "limit": limit,
                        "page": page,
                    },
                    item_retrieve_params.ItemRetrieveParams,
                ),
            ),
            cast_to=Collection,
        )

    def update(
        self,
        *,
        collection_name: str,
        items: Iterable[item_update_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemUpdateResponse:
        """
        Update existing items in a Collection

        Args:
          collection_name: The name/path of the collection. Must use only letters, digits, underscores, and
              dots. Each segment must start with a letter or underscore.

          items: Array of items to update (maximum 100 items per request)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v3/collections/items",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "items": items,
                },
                item_update_params.ItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemUpdateResponse,
        )

    def delete(
        self,
        *,
        collection_item_id: str,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an item from a Collection

        Args:
          collection_item_id: The unique identifier of the item to delete

          collection_name: The name/path of the collection. Must use only letters, digits, underscores, and
              dots. Each segment must start with a letter or underscore.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/v3/collections/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_item_id": collection_item_id,
                        "collection_name": collection_name,
                    },
                    item_delete_params.ItemDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def add(
        self,
        *,
        collection_name: str,
        items: Iterable[item_add_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemAddResponse:
        """
        Add new items to a Collection

        Args:
          collection_name: The name/path of the collection. Must use only letters, digits, underscores, and
              dots. Each segment must start with a letter or underscore.

          items: Array of items to add (maximum 100 items per request)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/collections/items",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "items": items,
                },
                item_add_params.ItemAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemAddResponse,
        )


class AsyncItemsResource(AsyncAPIResource):
    """
    Collections are named groups of embedded items used by Enrich functions for semantic search.

    Each collection is referenced by a `collectionName`, which supports dot notation for
    hierarchical paths (e.g. `customers.premium.vip`). Names must contain only letters,
    digits, underscores, and dots, and each segment must start with a letter or underscore.

    ## Items

    Items carry either a string or a JSON object in their `data` field. When items are added
    or updated, their `data` is embedded asynchronously — `POST /v3/collections/items` and
    `PUT /v3/collections/items` return immediately with a `pending` status and an `eventID`
    that can be correlated with webhook notifications once processing completes.

    ## Listing and hierarchy

    Use `GET /v3/collections` with `parentCollectionName` to list collections under a path,
    or `collectionNameSearch` for a case-insensitive substring match. `GET /v3/collections/items`
    retrieves a specific collection's items; pass `includeSubcollections=true` to fold in items
    from all descendant collections.

    ## Token counting

    Use `POST /v3/collections/token-count` to check whether texts fit within the embedding
    model's 8,192-token-per-text limit before submitting them for embedding.
    """

    @cached_property
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncItemsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        collection_name: str,
        include_subcollections: bool | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Collection:
        """Get a Collection

        Args:
          collection_name: The name/path of the collection.

        Must use only letters, digits, underscores, and
              dots. Each segment must start with a letter or underscore.

          include_subcollections: When true, includes items from all subcollections under the specified collection
              path. For example, querying "customers" with this flag will return items from
              "customers", "customers.premium", "customers.premium.vip", etc.

          limit: Number of items per page

          page: Page number for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/collections/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "collection_name": collection_name,
                        "include_subcollections": include_subcollections,
                        "limit": limit,
                        "page": page,
                    },
                    item_retrieve_params.ItemRetrieveParams,
                ),
            ),
            cast_to=Collection,
        )

    async def update(
        self,
        *,
        collection_name: str,
        items: Iterable[item_update_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemUpdateResponse:
        """
        Update existing items in a Collection

        Args:
          collection_name: The name/path of the collection. Must use only letters, digits, underscores, and
              dots. Each segment must start with a letter or underscore.

          items: Array of items to update (maximum 100 items per request)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v3/collections/items",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "items": items,
                },
                item_update_params.ItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemUpdateResponse,
        )

    async def delete(
        self,
        *,
        collection_item_id: str,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an item from a Collection

        Args:
          collection_item_id: The unique identifier of the item to delete

          collection_name: The name/path of the collection. Must use only letters, digits, underscores, and
              dots. Each segment must start with a letter or underscore.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/v3/collections/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "collection_item_id": collection_item_id,
                        "collection_name": collection_name,
                    },
                    item_delete_params.ItemDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def add(
        self,
        *,
        collection_name: str,
        items: Iterable[item_add_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemAddResponse:
        """
        Add new items to a Collection

        Args:
          collection_name: The name/path of the collection. Must use only letters, digits, underscores, and
              dots. Each segment must start with a letter or underscore.

          items: Array of items to add (maximum 100 items per request)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/collections/items",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "items": items,
                },
                item_add_params.ItemAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemAddResponse,
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.retrieve = to_raw_response_wrapper(
            items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            items.update,
        )
        self.delete = to_raw_response_wrapper(
            items.delete,
        )
        self.add = to_raw_response_wrapper(
            items.add,
        )


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.retrieve = async_to_raw_response_wrapper(
            items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            items.update,
        )
        self.delete = async_to_raw_response_wrapper(
            items.delete,
        )
        self.add = async_to_raw_response_wrapper(
            items.add,
        )


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.retrieve = to_streamed_response_wrapper(
            items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            items.update,
        )
        self.delete = to_streamed_response_wrapper(
            items.delete,
        )
        self.add = to_streamed_response_wrapper(
            items.add,
        )


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.retrieve = async_to_streamed_response_wrapper(
            items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            items.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            items.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            items.add,
        )
