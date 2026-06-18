# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from tests.utils import assert_matches_type
from bem.types.entities import SynonymAddResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSynonyms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Bem) -> None:
        synonym = client.entities.synonyms.add(
            id="id",
            text="ACME Corporation",
        )
        assert_matches_type(SynonymAddResponse, synonym, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Bem) -> None:
        synonym = client.entities.synonyms.add(
            id="id",
            text="ACME Corporation",
            bucket="bucket",
            locale="en-US",
        )
        assert_matches_type(SynonymAddResponse, synonym, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Bem) -> None:
        response = client.entities.synonyms.with_raw_response.add(
            id="id",
            text="ACME Corporation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        synonym = response.parse()
        assert_matches_type(SynonymAddResponse, synonym, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Bem) -> None:
        with client.entities.synonyms.with_streaming_response.add(
            id="id",
            text="ACME Corporation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            synonym = response.parse()
            assert_matches_type(SynonymAddResponse, synonym, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.synonyms.with_raw_response.add(
                id="",
                text="ACME Corporation",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Bem) -> None:
        synonym = client.entities.synonyms.remove(
            synonym_id="synonymID",
            id="id",
        )
        assert synonym is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_with_all_params(self, client: Bem) -> None:
        synonym = client.entities.synonyms.remove(
            synonym_id="synonymID",
            id="id",
            bucket="bucket",
        )
        assert synonym is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Bem) -> None:
        response = client.entities.synonyms.with_raw_response.remove(
            synonym_id="synonymID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        synonym = response.parse()
        assert synonym is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Bem) -> None:
        with client.entities.synonyms.with_streaming_response.remove(
            synonym_id="synonymID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            synonym = response.parse()
            assert synonym is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.synonyms.with_raw_response.remove(
                synonym_id="synonymID",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `synonym_id` but received ''"):
            client.entities.synonyms.with_raw_response.remove(
                synonym_id="",
                id="id",
            )


class TestAsyncSynonyms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncBem) -> None:
        synonym = await async_client.entities.synonyms.add(
            id="id",
            text="ACME Corporation",
        )
        assert_matches_type(SynonymAddResponse, synonym, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncBem) -> None:
        synonym = await async_client.entities.synonyms.add(
            id="id",
            text="ACME Corporation",
            bucket="bucket",
            locale="en-US",
        )
        assert_matches_type(SynonymAddResponse, synonym, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncBem) -> None:
        response = await async_client.entities.synonyms.with_raw_response.add(
            id="id",
            text="ACME Corporation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        synonym = await response.parse()
        assert_matches_type(SynonymAddResponse, synonym, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncBem) -> None:
        async with async_client.entities.synonyms.with_streaming_response.add(
            id="id",
            text="ACME Corporation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            synonym = await response.parse()
            assert_matches_type(SynonymAddResponse, synonym, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.synonyms.with_raw_response.add(
                id="",
                text="ACME Corporation",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncBem) -> None:
        synonym = await async_client.entities.synonyms.remove(
            synonym_id="synonymID",
            id="id",
        )
        assert synonym is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncBem) -> None:
        synonym = await async_client.entities.synonyms.remove(
            synonym_id="synonymID",
            id="id",
            bucket="bucket",
        )
        assert synonym is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncBem) -> None:
        response = await async_client.entities.synonyms.with_raw_response.remove(
            synonym_id="synonymID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        synonym = await response.parse()
        assert synonym is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncBem) -> None:
        async with async_client.entities.synonyms.with_streaming_response.remove(
            synonym_id="synonymID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            synonym = await response.parse()
            assert synonym is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.synonyms.with_raw_response.remove(
                synonym_id="synonymID",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `synonym_id` but received ''"):
            await async_client.entities.synonyms.with_raw_response.remove(
                synonym_id="",
                id="id",
            )
