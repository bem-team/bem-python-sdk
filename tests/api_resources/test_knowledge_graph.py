# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import KnowledgeGraphRetrieveResponse
from bem._utils import parse_datetime
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeGraph:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bem) -> None:
        knowledge_graph = client.knowledge_graph.retrieve()
        assert_matches_type(KnowledgeGraphRetrieveResponse, knowledge_graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Bem) -> None:
        knowledge_graph = client.knowledge_graph.retrieve(
            bucket="bucket",
            cursor="cursor",
            limit=0,
            max_depth=0,
            node_id="nodeID",
            search="search",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            type=["string"],
        )
        assert_matches_type(KnowledgeGraphRetrieveResponse, knowledge_graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bem) -> None:
        response = client.knowledge_graph.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_graph = response.parse()
        assert_matches_type(KnowledgeGraphRetrieveResponse, knowledge_graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bem) -> None:
        with client.knowledge_graph.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_graph = response.parse()
            assert_matches_type(KnowledgeGraphRetrieveResponse, knowledge_graph, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowledgeGraph:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBem) -> None:
        knowledge_graph = await async_client.knowledge_graph.retrieve()
        assert_matches_type(KnowledgeGraphRetrieveResponse, knowledge_graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBem) -> None:
        knowledge_graph = await async_client.knowledge_graph.retrieve(
            bucket="bucket",
            cursor="cursor",
            limit=0,
            max_depth=0,
            node_id="nodeID",
            search="search",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            type=["string"],
        )
        assert_matches_type(KnowledgeGraphRetrieveResponse, knowledge_graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBem) -> None:
        response = await async_client.knowledge_graph.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_graph = await response.parse()
        assert_matches_type(KnowledgeGraphRetrieveResponse, knowledge_graph, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBem) -> None:
        async with async_client.knowledge_graph.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_graph = await response.parse()
            assert_matches_type(KnowledgeGraphRetrieveResponse, knowledge_graph, path=["response"])

        assert cast(Any, response.is_closed) is True
