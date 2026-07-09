# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from tests.utils import assert_matches_type
from bem.types.entity_types import Reviewer, ReviewerListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReviewers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bem) -> None:
        reviewer = client.entity_types.reviewers.list(
            "typeID",
        )
        assert_matches_type(ReviewerListResponse, reviewer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bem) -> None:
        response = client.entity_types.reviewers.with_raw_response.list(
            "typeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reviewer = response.parse()
        assert_matches_type(ReviewerListResponse, reviewer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bem) -> None:
        with client.entity_types.reviewers.with_streaming_response.list(
            "typeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reviewer = response.parse()
            assert_matches_type(ReviewerListResponse, reviewer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            client.entity_types.reviewers.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_assign(self, client: Bem) -> None:
        reviewer = client.entity_types.reviewers.assign(
            type_id="typeID",
            user_id="usr_2xyz...",
        )
        assert_matches_type(Reviewer, reviewer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_assign(self, client: Bem) -> None:
        response = client.entity_types.reviewers.with_raw_response.assign(
            type_id="typeID",
            user_id="usr_2xyz...",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reviewer = response.parse()
        assert_matches_type(Reviewer, reviewer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_assign(self, client: Bem) -> None:
        with client.entity_types.reviewers.with_streaming_response.assign(
            type_id="typeID",
            user_id="usr_2xyz...",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reviewer = response.parse()
            assert_matches_type(Reviewer, reviewer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_assign(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            client.entity_types.reviewers.with_raw_response.assign(
                type_id="",
                user_id="usr_2xyz...",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Bem) -> None:
        reviewer = client.entity_types.reviewers.remove(
            user_id="userID",
            type_id="typeID",
        )
        assert reviewer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Bem) -> None:
        response = client.entity_types.reviewers.with_raw_response.remove(
            user_id="userID",
            type_id="typeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reviewer = response.parse()
        assert reviewer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Bem) -> None:
        with client.entity_types.reviewers.with_streaming_response.remove(
            user_id="userID",
            type_id="typeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reviewer = response.parse()
            assert reviewer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            client.entity_types.reviewers.with_raw_response.remove(
                user_id="userID",
                type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.entity_types.reviewers.with_raw_response.remove(
                user_id="",
                type_id="typeID",
            )


class TestAsyncReviewers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBem) -> None:
        reviewer = await async_client.entity_types.reviewers.list(
            "typeID",
        )
        assert_matches_type(ReviewerListResponse, reviewer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBem) -> None:
        response = await async_client.entity_types.reviewers.with_raw_response.list(
            "typeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reviewer = await response.parse()
        assert_matches_type(ReviewerListResponse, reviewer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBem) -> None:
        async with async_client.entity_types.reviewers.with_streaming_response.list(
            "typeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reviewer = await response.parse()
            assert_matches_type(ReviewerListResponse, reviewer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            await async_client.entity_types.reviewers.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_assign(self, async_client: AsyncBem) -> None:
        reviewer = await async_client.entity_types.reviewers.assign(
            type_id="typeID",
            user_id="usr_2xyz...",
        )
        assert_matches_type(Reviewer, reviewer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_assign(self, async_client: AsyncBem) -> None:
        response = await async_client.entity_types.reviewers.with_raw_response.assign(
            type_id="typeID",
            user_id="usr_2xyz...",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reviewer = await response.parse()
        assert_matches_type(Reviewer, reviewer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_assign(self, async_client: AsyncBem) -> None:
        async with async_client.entity_types.reviewers.with_streaming_response.assign(
            type_id="typeID",
            user_id="usr_2xyz...",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reviewer = await response.parse()
            assert_matches_type(Reviewer, reviewer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_assign(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            await async_client.entity_types.reviewers.with_raw_response.assign(
                type_id="",
                user_id="usr_2xyz...",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncBem) -> None:
        reviewer = await async_client.entity_types.reviewers.remove(
            user_id="userID",
            type_id="typeID",
        )
        assert reviewer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncBem) -> None:
        response = await async_client.entity_types.reviewers.with_raw_response.remove(
            user_id="userID",
            type_id="typeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reviewer = await response.parse()
        assert reviewer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncBem) -> None:
        async with async_client.entity_types.reviewers.with_streaming_response.remove(
            user_id="userID",
            type_id="typeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reviewer = await response.parse()
            assert reviewer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            await async_client.entity_types.reviewers.with_raw_response.remove(
                user_id="userID",
                type_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.entity_types.reviewers.with_raw_response.remove(
                user_id="",
                type_id="typeID",
            )
