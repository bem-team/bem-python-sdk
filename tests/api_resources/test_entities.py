# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import (
    EntityUpdateResponse,
    EntityBulkCreateResponse,
    EntityBulkValidateResponse,
    EntityRetrieveRelationsResponse,
    EntityRetrieveSeedStatusResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Bem) -> None:
        entity = client.entities.update(
            id="id",
        )
        assert_matches_type(EntityUpdateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Bem) -> None:
        entity = client.entities.update(
            id="id",
            add_synonyms=["string"],
            assigned_type_id="assignedTypeID",
            canonical="canonical",
            locale="locale",
            remove_synonym_ids=["string"],
            status="approved",
        )
        assert_matches_type(EntityUpdateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Bem) -> None:
        response = client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityUpdateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Bem) -> None:
        with client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityUpdateResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_create(self, client: Bem) -> None:
        entity = client.entities.bulk_create(
            entities=[
                {
                    "canonical": "Acme Corporation",
                    "type": "organization",
                }
            ],
        )
        assert_matches_type(EntityBulkCreateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_create_with_all_params(self, client: Bem) -> None:
        entity = client.entities.bulk_create(
            entities=[
                {
                    "canonical": "Acme Corporation",
                    "type": "organization",
                    "attributes": {"headquarters": "Springfield"},
                    "description": "Industrial conglomerate",
                    "synonyms": ["ACME", "Acme Corp"],
                }
            ],
            bucket="bucket",
            on_conflict="merge",
        )
        assert_matches_type(EntityBulkCreateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_create(self, client: Bem) -> None:
        response = client.entities.with_raw_response.bulk_create(
            entities=[
                {
                    "canonical": "Acme Corporation",
                    "type": "organization",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityBulkCreateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_create(self, client: Bem) -> None:
        with client.entities.with_streaming_response.bulk_create(
            entities=[
                {
                    "canonical": "Acme Corporation",
                    "type": "organization",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityBulkCreateResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_validate(self, client: Bem) -> None:
        entity = client.entities.bulk_validate(
            entity_ids=["ent_2abc", "ent_2def"],
            status="approved",
        )
        assert_matches_type(EntityBulkValidateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_validate(self, client: Bem) -> None:
        response = client.entities.with_raw_response.bulk_validate(
            entity_ids=["ent_2abc", "ent_2def"],
            status="approved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityBulkValidateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_validate(self, client: Bem) -> None:
        with client.entities.with_streaming_response.bulk_validate(
            entity_ids=["ent_2abc", "ent_2def"],
            status="approved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityBulkValidateResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_relations(self, client: Bem) -> None:
        entity = client.entities.retrieve_relations(
            id="id",
        )
        assert_matches_type(EntityRetrieveRelationsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_relations_with_all_params(self, client: Bem) -> None:
        entity = client.entities.retrieve_relations(
            id="id",
            bucket="bucket",
            cursor="cursor",
            direction="inbound",
            limit=0,
            relation_type="relationType",
        )
        assert_matches_type(EntityRetrieveRelationsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_relations(self, client: Bem) -> None:
        response = client.entities.with_raw_response.retrieve_relations(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityRetrieveRelationsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_relations(self, client: Bem) -> None:
        with client.entities.with_streaming_response.retrieve_relations(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityRetrieveRelationsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_relations(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.retrieve_relations(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_seed_status(self, client: Bem) -> None:
        entity = client.entities.retrieve_seed_status(
            "id",
        )
        assert_matches_type(EntityRetrieveSeedStatusResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_seed_status(self, client: Bem) -> None:
        response = client.entities.with_raw_response.retrieve_seed_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityRetrieveSeedStatusResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_seed_status(self, client: Bem) -> None:
        with client.entities.with_streaming_response.retrieve_seed_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityRetrieveSeedStatusResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_seed_status(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.entities.with_raw_response.retrieve_seed_status(
                "",
            )


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBem) -> None:
        entity = await async_client.entities.update(
            id="id",
        )
        assert_matches_type(EntityUpdateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBem) -> None:
        entity = await async_client.entities.update(
            id="id",
            add_synonyms=["string"],
            assigned_type_id="assignedTypeID",
            canonical="canonical",
            locale="locale",
            remove_synonym_ids=["string"],
            status="approved",
        )
        assert_matches_type(EntityUpdateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBem) -> None:
        response = await async_client.entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityUpdateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBem) -> None:
        async with async_client.entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityUpdateResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncBem) -> None:
        entity = await async_client.entities.bulk_create(
            entities=[
                {
                    "canonical": "Acme Corporation",
                    "type": "organization",
                }
            ],
        )
        assert_matches_type(EntityBulkCreateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_create_with_all_params(self, async_client: AsyncBem) -> None:
        entity = await async_client.entities.bulk_create(
            entities=[
                {
                    "canonical": "Acme Corporation",
                    "type": "organization",
                    "attributes": {"headquarters": "Springfield"},
                    "description": "Industrial conglomerate",
                    "synonyms": ["ACME", "Acme Corp"],
                }
            ],
            bucket="bucket",
            on_conflict="merge",
        )
        assert_matches_type(EntityBulkCreateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncBem) -> None:
        response = await async_client.entities.with_raw_response.bulk_create(
            entities=[
                {
                    "canonical": "Acme Corporation",
                    "type": "organization",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityBulkCreateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncBem) -> None:
        async with async_client.entities.with_streaming_response.bulk_create(
            entities=[
                {
                    "canonical": "Acme Corporation",
                    "type": "organization",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityBulkCreateResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_validate(self, async_client: AsyncBem) -> None:
        entity = await async_client.entities.bulk_validate(
            entity_ids=["ent_2abc", "ent_2def"],
            status="approved",
        )
        assert_matches_type(EntityBulkValidateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_validate(self, async_client: AsyncBem) -> None:
        response = await async_client.entities.with_raw_response.bulk_validate(
            entity_ids=["ent_2abc", "ent_2def"],
            status="approved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityBulkValidateResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_validate(self, async_client: AsyncBem) -> None:
        async with async_client.entities.with_streaming_response.bulk_validate(
            entity_ids=["ent_2abc", "ent_2def"],
            status="approved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityBulkValidateResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_relations(self, async_client: AsyncBem) -> None:
        entity = await async_client.entities.retrieve_relations(
            id="id",
        )
        assert_matches_type(EntityRetrieveRelationsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_relations_with_all_params(self, async_client: AsyncBem) -> None:
        entity = await async_client.entities.retrieve_relations(
            id="id",
            bucket="bucket",
            cursor="cursor",
            direction="inbound",
            limit=0,
            relation_type="relationType",
        )
        assert_matches_type(EntityRetrieveRelationsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_relations(self, async_client: AsyncBem) -> None:
        response = await async_client.entities.with_raw_response.retrieve_relations(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityRetrieveRelationsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_relations(self, async_client: AsyncBem) -> None:
        async with async_client.entities.with_streaming_response.retrieve_relations(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityRetrieveRelationsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_relations(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.retrieve_relations(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_seed_status(self, async_client: AsyncBem) -> None:
        entity = await async_client.entities.retrieve_seed_status(
            "id",
        )
        assert_matches_type(EntityRetrieveSeedStatusResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_seed_status(self, async_client: AsyncBem) -> None:
        response = await async_client.entities.with_raw_response.retrieve_seed_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityRetrieveSeedStatusResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_seed_status(self, async_client: AsyncBem) -> None:
        async with async_client.entities.with_streaming_response.retrieve_seed_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityRetrieveSeedStatusResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_seed_status(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.entities.with_raw_response.retrieve_seed_status(
                "",
            )
