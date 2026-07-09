# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import knowledge_graph_retrieve_params
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
from ..types.knowledge_graph_retrieve_response import KnowledgeGraphRetrieveResponse

__all__ = ["KnowledgeGraphResource", "AsyncKnowledgeGraphResource"]


class KnowledgeGraphResource(SyncAPIResource):
    """
    Read the cross-document knowledge graph — the canonical entities and the
    directed relations between them that the Parse pipeline populates when
    `linkAcrossDocuments` is enabled.

    - **`GET /v3/entities/{id}/relations`** returns the inbound and outbound
      edges incident to one entity, split by direction. Supports
      `direction`, an exact `relationType` filter, and cursor pagination over
      edges. A merged-away entity id transparently resolves to its surviving
      canonical entity.
    - **`GET /v3/knowledge-graph`** returns the graph as `{ nodes, edges }`,
      paginating over edges. The `nodes` for a page are the distinct endpoint
      entities of that page's edges (both endpoints of every edge are
      included). Filter with `type[]`, `since`, and `search`; an edge is
      returned only when both of its endpoints survive the entity filters.

    Both endpoints take an optional `bucket` (`bkt_...`) to scope the read to
    a single bucket; omit it for the unscoped account+environment view.
    """

    @cached_property
    def with_raw_response(self) -> KnowledgeGraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return KnowledgeGraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeGraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return KnowledgeGraphResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        bucket: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        max_depth: int | Omit = omit,
        node_id: str | Omit = omit,
        search: str | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        type: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeGraphRetrieveResponse:
        """
        Retrieve the Knowledge Graph

        Args:
          bucket: Optional bucket public ID (`bkt_...`) to scope the read to one bucket. Omit for
              the unscoped (all account+environment) view.

          cursor: Cursor: return edges whose KSUID sorts after this value.

          limit: Maximum number of edges per page (default 50, max 200).

          max_depth: Maximum hops from the center node. Only meaningful with `nodeID`. Defaults to 2
              and is clamped down to a system maximum (5).

          node_id: Center the graph on this entity (`ent_...`) and only return the subgraph within
              `maxDepth` hops of it; every node then carries its `depth` (hops from the
              center, center = 0). Omit for the uncentered whole-graph view. `rootNodeID` and
              `focusNodeID` are accepted as aliases.

          search: Case-insensitive substring match on canonical names. Both endpoints of an edge
              must match for the edge (and its nodes) to be returned.

          since: Only edges created at/after this RFC 3339 timestamp.

          type: Restrict to entities of these types. An edge is returned only when BOTH of its
              endpoints survive the type filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/knowledge-graph",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bucket": bucket,
                        "cursor": cursor,
                        "limit": limit,
                        "max_depth": max_depth,
                        "node_id": node_id,
                        "search": search,
                        "since": since,
                        "type": type,
                    },
                    knowledge_graph_retrieve_params.KnowledgeGraphRetrieveParams,
                ),
            ),
            cast_to=KnowledgeGraphRetrieveResponse,
        )


class AsyncKnowledgeGraphResource(AsyncAPIResource):
    """
    Read the cross-document knowledge graph — the canonical entities and the
    directed relations between them that the Parse pipeline populates when
    `linkAcrossDocuments` is enabled.

    - **`GET /v3/entities/{id}/relations`** returns the inbound and outbound
      edges incident to one entity, split by direction. Supports
      `direction`, an exact `relationType` filter, and cursor pagination over
      edges. A merged-away entity id transparently resolves to its surviving
      canonical entity.
    - **`GET /v3/knowledge-graph`** returns the graph as `{ nodes, edges }`,
      paginating over edges. The `nodes` for a page are the distinct endpoint
      entities of that page's edges (both endpoints of every edge are
      included). Filter with `type[]`, `since`, and `search`; an edge is
      returned only when both of its endpoints survive the entity filters.

    Both endpoints take an optional `bucket` (`bkt_...`) to scope the read to
    a single bucket; omit it for the unscoped account+environment view.
    """

    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeGraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeGraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeGraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncKnowledgeGraphResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        bucket: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        max_depth: int | Omit = omit,
        node_id: str | Omit = omit,
        search: str | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        type: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeGraphRetrieveResponse:
        """
        Retrieve the Knowledge Graph

        Args:
          bucket: Optional bucket public ID (`bkt_...`) to scope the read to one bucket. Omit for
              the unscoped (all account+environment) view.

          cursor: Cursor: return edges whose KSUID sorts after this value.

          limit: Maximum number of edges per page (default 50, max 200).

          max_depth: Maximum hops from the center node. Only meaningful with `nodeID`. Defaults to 2
              and is clamped down to a system maximum (5).

          node_id: Center the graph on this entity (`ent_...`) and only return the subgraph within
              `maxDepth` hops of it; every node then carries its `depth` (hops from the
              center, center = 0). Omit for the uncentered whole-graph view. `rootNodeID` and
              `focusNodeID` are accepted as aliases.

          search: Case-insensitive substring match on canonical names. Both endpoints of an edge
              must match for the edge (and its nodes) to be returned.

          since: Only edges created at/after this RFC 3339 timestamp.

          type: Restrict to entities of these types. An edge is returned only when BOTH of its
              endpoints survive the type filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/knowledge-graph",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bucket": bucket,
                        "cursor": cursor,
                        "limit": limit,
                        "max_depth": max_depth,
                        "node_id": node_id,
                        "search": search,
                        "since": since,
                        "type": type,
                    },
                    knowledge_graph_retrieve_params.KnowledgeGraphRetrieveParams,
                ),
            ),
            cast_to=KnowledgeGraphRetrieveResponse,
        )


class KnowledgeGraphResourceWithRawResponse:
    def __init__(self, knowledge_graph: KnowledgeGraphResource) -> None:
        self._knowledge_graph = knowledge_graph

        self.retrieve = to_raw_response_wrapper(
            knowledge_graph.retrieve,
        )


class AsyncKnowledgeGraphResourceWithRawResponse:
    def __init__(self, knowledge_graph: AsyncKnowledgeGraphResource) -> None:
        self._knowledge_graph = knowledge_graph

        self.retrieve = async_to_raw_response_wrapper(
            knowledge_graph.retrieve,
        )


class KnowledgeGraphResourceWithStreamingResponse:
    def __init__(self, knowledge_graph: KnowledgeGraphResource) -> None:
        self._knowledge_graph = knowledge_graph

        self.retrieve = to_streamed_response_wrapper(
            knowledge_graph.retrieve,
        )


class AsyncKnowledgeGraphResourceWithStreamingResponse:
    def __init__(self, knowledge_graph: AsyncKnowledgeGraphResource) -> None:
        self._knowledge_graph = knowledge_graph

        self.retrieve = async_to_streamed_response_wrapper(
            knowledge_graph.retrieve,
        )
