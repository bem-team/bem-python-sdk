# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from tests.utils import assert_matches_type
from bem.types.functions import (
    RegressionRunResponse,
    RegressionApplyCorrectionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegression:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_apply_corrections(self, client: Bem) -> None:
        regression = client.functions.regression.apply_corrections(
            baseline_version_num=3,
            comparison_version_num=4,
            function_name="invoice-extractor",
        )
        assert_matches_type(RegressionApplyCorrectionsResponse, regression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_apply_corrections(self, client: Bem) -> None:
        response = client.functions.regression.with_raw_response.apply_corrections(
            baseline_version_num=3,
            comparison_version_num=4,
            function_name="invoice-extractor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regression = response.parse()
        assert_matches_type(RegressionApplyCorrectionsResponse, regression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_apply_corrections(self, client: Bem) -> None:
        with client.functions.regression.with_streaming_response.apply_corrections(
            baseline_version_num=3,
            comparison_version_num=4,
            function_name="invoice-extractor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regression = response.parse()
            assert_matches_type(RegressionApplyCorrectionsResponse, regression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Bem) -> None:
        regression = client.functions.regression.run(
            function_name="invoice-extractor",
        )
        assert_matches_type(RegressionRunResponse, regression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Bem) -> None:
        regression = client.functions.regression.run(
            function_name="invoice-extractor",
            baseline_version_num=3,
            comparison_version_num=5,
            only_corrected_data=True,
            sample_size=100,
        )
        assert_matches_type(RegressionRunResponse, regression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Bem) -> None:
        response = client.functions.regression.with_raw_response.run(
            function_name="invoice-extractor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regression = response.parse()
        assert_matches_type(RegressionRunResponse, regression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Bem) -> None:
        with client.functions.regression.with_streaming_response.run(
            function_name="invoice-extractor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regression = response.parse()
            assert_matches_type(RegressionRunResponse, regression, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRegression:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_apply_corrections(self, async_client: AsyncBem) -> None:
        regression = await async_client.functions.regression.apply_corrections(
            baseline_version_num=3,
            comparison_version_num=4,
            function_name="invoice-extractor",
        )
        assert_matches_type(RegressionApplyCorrectionsResponse, regression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_apply_corrections(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.regression.with_raw_response.apply_corrections(
            baseline_version_num=3,
            comparison_version_num=4,
            function_name="invoice-extractor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regression = await response.parse()
        assert_matches_type(RegressionApplyCorrectionsResponse, regression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_apply_corrections(self, async_client: AsyncBem) -> None:
        async with async_client.functions.regression.with_streaming_response.apply_corrections(
            baseline_version_num=3,
            comparison_version_num=4,
            function_name="invoice-extractor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regression = await response.parse()
            assert_matches_type(RegressionApplyCorrectionsResponse, regression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncBem) -> None:
        regression = await async_client.functions.regression.run(
            function_name="invoice-extractor",
        )
        assert_matches_type(RegressionRunResponse, regression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncBem) -> None:
        regression = await async_client.functions.regression.run(
            function_name="invoice-extractor",
            baseline_version_num=3,
            comparison_version_num=5,
            only_corrected_data=True,
            sample_size=100,
        )
        assert_matches_type(RegressionRunResponse, regression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.regression.with_raw_response.run(
            function_name="invoice-extractor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regression = await response.parse()
        assert_matches_type(RegressionRunResponse, regression, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncBem) -> None:
        async with async_client.functions.regression.with_streaming_response.run(
            function_name="invoice-extractor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regression = await response.parse()
            assert_matches_type(RegressionRunResponse, regression, path=["response"])

        assert cast(Any, response.is_closed) is True
