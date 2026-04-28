# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import EvalTriggerEvaluationResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEval:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_evaluation(self, client: Bem) -> None:
        eval = client.eval.trigger_evaluation(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        )
        assert_matches_type(EvalTriggerEvaluationResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_evaluation_with_all_params(self, client: Bem) -> None:
        eval = client.eval.trigger_evaluation(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
            evaluation_version="0.1.0-gemini",
        )
        assert_matches_type(EvalTriggerEvaluationResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_trigger_evaluation(self, client: Bem) -> None:
        response = client.eval.with_raw_response.trigger_evaluation(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(EvalTriggerEvaluationResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_trigger_evaluation(self, client: Bem) -> None:
        with client.eval.with_streaming_response.trigger_evaluation(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(EvalTriggerEvaluationResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEval:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_evaluation(self, async_client: AsyncBem) -> None:
        eval = await async_client.eval.trigger_evaluation(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        )
        assert_matches_type(EvalTriggerEvaluationResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_evaluation_with_all_params(self, async_client: AsyncBem) -> None:
        eval = await async_client.eval.trigger_evaluation(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
            evaluation_version="0.1.0-gemini",
        )
        assert_matches_type(EvalTriggerEvaluationResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_trigger_evaluation(self, async_client: AsyncBem) -> None:
        response = await async_client.eval.with_raw_response.trigger_evaluation(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(EvalTriggerEvaluationResponse, eval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_evaluation(self, async_client: AsyncBem) -> None:
        async with async_client.eval.with_streaming_response.trigger_evaluation(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(EvalTriggerEvaluationResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True
