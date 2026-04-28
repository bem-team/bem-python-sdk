# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import FNavigateResponse
from bem._utils import parse_datetime
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_navigate(self, client: Bem) -> None:
        f = client.fs.navigate(
            op="ls",
        )
        assert_matches_type(FNavigateResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_navigate_with_all_params(self, client: Bem) -> None:
        f = client.fs.navigate(
            op="ls",
            count_only=True,
            cursor="cursor",
            filter={
                "function_name": "functionName",
                "search": "search",
                "since": parse_datetime("2019-12-27T18:11:19.117Z"),
                "type": "type",
            },
            ignore_case=True,
            limit=0,
            n=0,
            path="path",
            pattern="pattern",
            range={
                "page": 0,
                "page_range": [0, 0],
                "section_types": ["string"],
            },
            regex=True,
            scope="scope",
            select=["string"],
        )
        assert_matches_type(FNavigateResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_navigate(self, client: Bem) -> None:
        response = client.fs.with_raw_response.navigate(
            op="ls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = response.parse()
        assert_matches_type(FNavigateResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_navigate(self, client: Bem) -> None:
        with client.fs.with_streaming_response.navigate(
            op="ls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = response.parse()
            assert_matches_type(FNavigateResponse, f, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_navigate(self, async_client: AsyncBem) -> None:
        f = await async_client.fs.navigate(
            op="ls",
        )
        assert_matches_type(FNavigateResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_navigate_with_all_params(self, async_client: AsyncBem) -> None:
        f = await async_client.fs.navigate(
            op="ls",
            count_only=True,
            cursor="cursor",
            filter={
                "function_name": "functionName",
                "search": "search",
                "since": parse_datetime("2019-12-27T18:11:19.117Z"),
                "type": "type",
            },
            ignore_case=True,
            limit=0,
            n=0,
            path="path",
            pattern="pattern",
            range={
                "page": 0,
                "page_range": [0, 0],
                "section_types": ["string"],
            },
            regex=True,
            scope="scope",
            select=["string"],
        )
        assert_matches_type(FNavigateResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_navigate(self, async_client: AsyncBem) -> None:
        response = await async_client.fs.with_raw_response.navigate(
            op="ls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        f = await response.parse()
        assert_matches_type(FNavigateResponse, f, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_navigate(self, async_client: AsyncBem) -> None:
        async with async_client.fs.with_streaming_response.navigate(
            op="ls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            f = await response.parse()
            assert_matches_type(FNavigateResponse, f, path=["response"])

        assert cast(Any, response.is_closed) is True
