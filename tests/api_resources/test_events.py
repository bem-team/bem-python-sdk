# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import EventSubmitFeedbackResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_feedback(self, client: Bem) -> None:
        event = client.events.submit_feedback(
            event_id="eventID",
            correction={},
        )
        assert_matches_type(EventSubmitFeedbackResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_feedback_with_all_params(self, client: Bem) -> None:
        event = client.events.submit_feedback(
            event_id="eventID",
            correction={},
            order_matching=True,
        )
        assert_matches_type(EventSubmitFeedbackResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_feedback(self, client: Bem) -> None:
        response = client.events.with_raw_response.submit_feedback(
            event_id="eventID",
            correction={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventSubmitFeedbackResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_feedback(self, client: Bem) -> None:
        with client.events.with_streaming_response.submit_feedback(
            event_id="eventID",
            correction={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventSubmitFeedbackResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_feedback(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.events.with_raw_response.submit_feedback(
                event_id="",
                correction={},
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_feedback(self, async_client: AsyncBem) -> None:
        event = await async_client.events.submit_feedback(
            event_id="eventID",
            correction={},
        )
        assert_matches_type(EventSubmitFeedbackResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_feedback_with_all_params(self, async_client: AsyncBem) -> None:
        event = await async_client.events.submit_feedback(
            event_id="eventID",
            correction={},
            order_matching=True,
        )
        assert_matches_type(EventSubmitFeedbackResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_feedback(self, async_client: AsyncBem) -> None:
        response = await async_client.events.with_raw_response.submit_feedback(
            event_id="eventID",
            correction={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventSubmitFeedbackResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_feedback(self, async_client: AsyncBem) -> None:
        async with async_client.events.with_streaming_response.submit_feedback(
            event_id="eventID",
            correction={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventSubmitFeedbackResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_feedback(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.events.with_raw_response.submit_feedback(
                event_id="",
                correction={},
            )
