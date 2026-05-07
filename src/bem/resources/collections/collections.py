# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ...types import (
    collection_list_params,
    collection_create_params,
    collection_delete_params,
    collection_count_tokens_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.collection_list_response import CollectionListResponse
from ...types.collection_count_tokens_response import CollectionCountTokensResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
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
    def items(self) -> ItemsResource:
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
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Collection:
        """
        Create a Collection

        Args:
          collection_name: Unique name/path for the collection. Supports dot notation for hierarchical
              paths.

              - Only letters (a-z, A-Z), digits (0-9), underscores (\\__), and dots (.) are
                allowed
              - Each segment (between dots) must start with a letter or underscore (not a
                digit)
              - Segments cannot consist only of digits
              - Each segment must be 1-256 characters
              - No leading, trailing, or consecutive dots
              - Invalid names are rejected with a 400 Bad Request error

              **Valid Examples:**

              - 'product_catalog'
              - 'orders.line_items.sku'
              - 'customer_data'
              - 'price_v2'

              **Invalid Examples:**

              - 'product-catalog' (contains hyphen)
              - '123items' (starts with digit)
              - 'items..data' (consecutive dots)
              - 'order#123' (contains invalid character #)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/collections",
            body=maybe_transform({"collection_name": collection_name}, collection_create_params.CollectionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
        )

    def list(
        self,
        *,
        collection_name_search: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        parent_collection_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionListResponse:
        """
        List Collections

        Args:
          collection_name_search: Optional substring search filter for collection names (case-insensitive). For
              example, "premium" will match "customers.premium", "products.premium", etc.

          limit: Number of collections per page

          page: Page number for pagination

          parent_collection_name: Optional filter to list only collections under a specific parent collection
              path. For example, "customers" will return "customers", "customers.premium",
              "customers.premium.vip", etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_name_search": collection_name_search,
                        "limit": limit,
                        "page": page,
                        "parent_collection_name": parent_collection_name,
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            cast_to=CollectionListResponse,
        )

    def delete(
        self,
        *,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Collection

        Args:
          collection_name: The name/path of the collection to delete. Must use only letters, digits,
              underscores, and dots. Each segment must start with a letter or underscore.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/v3/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"collection_name": collection_name}, collection_delete_params.CollectionDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    def count_tokens(
        self,
        *,
        texts: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionCountTokensResponse:
        """
        Count the number of tokens in the provided texts using the BGE M3 tokenizer.
        This is useful for checking if texts will fit within the embedding model's token
        limit (8,192 tokens per text) before sending them for embedding.

        Args:
          texts: One or more texts to tokenize.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/collections/token-count",
            body=maybe_transform({"texts": texts}, collection_count_tokens_params.CollectionCountTokensParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionCountTokensResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
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
    def items(self) -> AsyncItemsResource:
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
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Collection:
        """
        Create a Collection

        Args:
          collection_name: Unique name/path for the collection. Supports dot notation for hierarchical
              paths.

              - Only letters (a-z, A-Z), digits (0-9), underscores (\\__), and dots (.) are
                allowed
              - Each segment (between dots) must start with a letter or underscore (not a
                digit)
              - Segments cannot consist only of digits
              - Each segment must be 1-256 characters
              - No leading, trailing, or consecutive dots
              - Invalid names are rejected with a 400 Bad Request error

              **Valid Examples:**

              - 'product_catalog'
              - 'orders.line_items.sku'
              - 'customer_data'
              - 'price_v2'

              **Invalid Examples:**

              - 'product-catalog' (contains hyphen)
              - '123items' (starts with digit)
              - 'items..data' (consecutive dots)
              - 'order#123' (contains invalid character #)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/collections",
            body=await async_maybe_transform(
                {"collection_name": collection_name}, collection_create_params.CollectionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
        )

    async def list(
        self,
        *,
        collection_name_search: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        parent_collection_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionListResponse:
        """
        List Collections

        Args:
          collection_name_search: Optional substring search filter for collection names (case-insensitive). For
              example, "premium" will match "customers.premium", "products.premium", etc.

          limit: Number of collections per page

          page: Page number for pagination

          parent_collection_name: Optional filter to list only collections under a specific parent collection
              path. For example, "customers" will return "customers", "customers.premium",
              "customers.premium.vip", etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "collection_name_search": collection_name_search,
                        "limit": limit,
                        "page": page,
                        "parent_collection_name": parent_collection_name,
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            cast_to=CollectionListResponse,
        )

    async def delete(
        self,
        *,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Collection

        Args:
          collection_name: The name/path of the collection to delete. Must use only letters, digits,
              underscores, and dots. Each segment must start with a letter or underscore.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/v3/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"collection_name": collection_name}, collection_delete_params.CollectionDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def count_tokens(
        self,
        *,
        texts: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionCountTokensResponse:
        """
        Count the number of tokens in the provided texts using the BGE M3 tokenizer.
        This is useful for checking if texts will fit within the embedding model's token
        limit (8,192 tokens per text) before sending them for embedding.

        Args:
          texts: One or more texts to tokenize.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/collections/token-count",
            body=await async_maybe_transform(
                {"texts": texts}, collection_count_tokens_params.CollectionCountTokensParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionCountTokensResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_raw_response_wrapper(
            collections.create,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.delete = to_raw_response_wrapper(
            collections.delete,
        )
        self.count_tokens = to_raw_response_wrapper(
            collections.count_tokens,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
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
        return ItemsResourceWithRawResponse(self._collections.items)


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_raw_response_wrapper(
            collections.create,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            collections.delete,
        )
        self.count_tokens = async_to_raw_response_wrapper(
            collections.count_tokens,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
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
        return AsyncItemsResourceWithRawResponse(self._collections.items)


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_streamed_response_wrapper(
            collections.create,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = to_streamed_response_wrapper(
            collections.delete,
        )
        self.count_tokens = to_streamed_response_wrapper(
            collections.count_tokens,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
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
        return ItemsResourceWithStreamingResponse(self._collections.items)


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_streamed_response_wrapper(
            collections.create,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            collections.delete,
        )
        self.count_tokens = async_to_streamed_response_wrapper(
            collections.count_tokens,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
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
        return AsyncItemsResourceWithStreamingResponse(self._collections.items)
