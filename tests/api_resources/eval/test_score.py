# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from tests.utils import assert_matches_type
from bem.types.eval import EvalScoreRun, ScoreCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScore:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Bem) -> None:
        score = client.eval.score.create(
            function_name="functionName",
            pairs=[
                {
                    "expected": {},
                    "input": {
                        "input_content": "inputContent",
                        "input_type": "csv",
                    },
                }
            ],
        )
        assert_matches_type(ScoreCreateResponse, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Bem) -> None:
        score = client.eval.score.create(
            function_name="functionName",
            pairs=[
                {
                    "expected": {},
                    "input": {
                        "input_content": "inputContent",
                        "input_type": "csv",
                    },
                }
            ],
            function_version_num=0,
            match_config={
                "array_match": "by-index",
                "fuzzy_threshold": 0,
                "ignore_paths": ["string"],
                "numeric_tolerance": 0,
                "string_match": "exact",
            },
        )
        assert_matches_type(ScoreCreateResponse, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Bem) -> None:
        response = client.eval.score.with_raw_response.create(
            function_name="functionName",
            pairs=[
                {
                    "expected": {},
                    "input": {
                        "input_content": "inputContent",
                        "input_type": "csv",
                    },
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert_matches_type(ScoreCreateResponse, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Bem) -> None:
        with client.eval.score.with_streaming_response.create(
            function_name="functionName",
            pairs=[
                {
                    "expected": {},
                    "input": {
                        "input_content": "inputContent",
                        "input_type": "csv",
                    },
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert_matches_type(ScoreCreateResponse, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bem) -> None:
        score = client.eval.score.retrieve(
            "scoreRunID",
        )
        assert_matches_type(EvalScoreRun, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bem) -> None:
        response = client.eval.score.with_raw_response.retrieve(
            "scoreRunID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert_matches_type(EvalScoreRun, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bem) -> None:
        with client.eval.score.with_streaming_response.retrieve(
            "scoreRunID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert_matches_type(EvalScoreRun, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `score_run_id` but received ''"):
            client.eval.score.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Bem) -> None:
        score = client.eval.score.cancel(
            "scoreRunID",
        )
        assert_matches_type(EvalScoreRun, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Bem) -> None:
        response = client.eval.score.with_raw_response.cancel(
            "scoreRunID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = response.parse()
        assert_matches_type(EvalScoreRun, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Bem) -> None:
        with client.eval.score.with_streaming_response.cancel(
            "scoreRunID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = response.parse()
            assert_matches_type(EvalScoreRun, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `score_run_id` but received ''"):
            client.eval.score.with_raw_response.cancel(
                "",
            )


class TestAsyncScore:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBem) -> None:
        score = await async_client.eval.score.create(
            function_name="functionName",
            pairs=[
                {
                    "expected": {},
                    "input": {
                        "input_content": "inputContent",
                        "input_type": "csv",
                    },
                }
            ],
        )
        assert_matches_type(ScoreCreateResponse, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBem) -> None:
        score = await async_client.eval.score.create(
            function_name="functionName",
            pairs=[
                {
                    "expected": {},
                    "input": {
                        "input_content": "inputContent",
                        "input_type": "csv",
                    },
                }
            ],
            function_version_num=0,
            match_config={
                "array_match": "by-index",
                "fuzzy_threshold": 0,
                "ignore_paths": ["string"],
                "numeric_tolerance": 0,
                "string_match": "exact",
            },
        )
        assert_matches_type(ScoreCreateResponse, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBem) -> None:
        response = await async_client.eval.score.with_raw_response.create(
            function_name="functionName",
            pairs=[
                {
                    "expected": {},
                    "input": {
                        "input_content": "inputContent",
                        "input_type": "csv",
                    },
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert_matches_type(ScoreCreateResponse, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBem) -> None:
        async with async_client.eval.score.with_streaming_response.create(
            function_name="functionName",
            pairs=[
                {
                    "expected": {},
                    "input": {
                        "input_content": "inputContent",
                        "input_type": "csv",
                    },
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert_matches_type(ScoreCreateResponse, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBem) -> None:
        score = await async_client.eval.score.retrieve(
            "scoreRunID",
        )
        assert_matches_type(EvalScoreRun, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBem) -> None:
        response = await async_client.eval.score.with_raw_response.retrieve(
            "scoreRunID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert_matches_type(EvalScoreRun, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBem) -> None:
        async with async_client.eval.score.with_streaming_response.retrieve(
            "scoreRunID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert_matches_type(EvalScoreRun, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `score_run_id` but received ''"):
            await async_client.eval.score.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncBem) -> None:
        score = await async_client.eval.score.cancel(
            "scoreRunID",
        )
        assert_matches_type(EvalScoreRun, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncBem) -> None:
        response = await async_client.eval.score.with_raw_response.cancel(
            "scoreRunID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        score = await response.parse()
        assert_matches_type(EvalScoreRun, score, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncBem) -> None:
        async with async_client.eval.score.with_streaming_response.cancel(
            "scoreRunID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            score = await response.parse()
            assert_matches_type(EvalScoreRun, score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `score_run_id` but received ''"):
            await async_client.eval.score.with_raw_response.cancel(
                "",
            )
