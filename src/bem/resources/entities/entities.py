# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...types import (
    entity_update_params,
    entity_bulk_create_params,
    entity_bulk_validate_params,
    entity_retrieve_relations_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .synonyms import (
    SynonymsResource,
    AsyncSynonymsResource,
    SynonymsResourceWithRawResponse,
    AsyncSynonymsResourceWithRawResponse,
    SynonymsResourceWithStreamingResponse,
    AsyncSynonymsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.entity_update_response import EntityUpdateResponse
from ...types.entity_bulk_create_response import EntityBulkCreateResponse
from ...types.entity_bulk_validate_response import EntityBulkValidateResponse
from ...types.entity_retrieve_relations_response import EntityRetrieveRelationsResponse
from ...types.entity_retrieve_seed_status_response import EntityRetrieveSeedStatusResponse

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def synonyms(self) -> SynonymsResource:
        """
        Manage the human-readable surface forms (synonyms) attached to a canonical
        entity. Synonyms feed the matcher's exact-match path, so adding the right
        synonyms improves cross-document entity resolution.

        - **`POST /v3/entities/{id}/synonyms`** attaches a `customer_defined`
          synonym. If the same normalized form already exists as an `extracted`
          synonym, it is upgraded to `customer_defined` (so the matcher weights it
          higher); an existing customer/SME synonym is returned unchanged.
        - **`DELETE /v3/entities/{id}/synonyms/{synonymID}`** soft-deletes a
          synonym. Only `customer_defined` and `sme_approved` synonyms are
          deletable; `extracted` synonyms are resolver-owned and the request is
          rejected with `409 Conflict`.

        A merged-away entity id transparently resolves to its surviving canonical
        entity, so a synonym added to a stale id lands on the entity that persists.
        """
        return SynonymsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        add_synonyms: SequenceNotStr[str] | Omit = omit,
        assigned_type_id: str | Omit = omit,
        canonical: str | Omit = omit,
        locale: str | Omit = omit,
        remove_synonym_ids: SequenceNotStr[str] | Omit = omit,
        status: Literal["approved", "rejected"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityUpdateResponse:
        """
        Update Entity

        Args:
          add_synonyms: Surface forms to attach as `customer_defined` synonyms.

          assigned_type_id: The `ety_...` public ID of the type to assign (overriding the bem-inferred
              type). The empty string clears the assignment. Omit to leave unchanged.

          canonical: Replace the entity's canonical surface form (re-derives its normalized form).

          locale: Optional BCP 47 locale tag stamped on any added synonyms.

          remove_synonym_ids: `esn_...` synonym IDs to soft-delete. Only `customer_defined` / `sme_approved`
              synonyms may be removed; an `extracted` synonym is rejected with `409`.

          status: Transition the entity's curation status. Only `approved` or `rejected` are
              accepted, and only from `extracted` or `proposed` (any other transition is
              rejected with `409`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v3/entities/{id}", id=id),
            body=maybe_transform(
                {
                    "add_synonyms": add_synonyms,
                    "assigned_type_id": assigned_type_id,
                    "canonical": canonical,
                    "locale": locale,
                    "remove_synonym_ids": remove_synonym_ids,
                    "status": status,
                },
                entity_update_params.EntityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityUpdateResponse,
        )

    def bulk_create(
        self,
        *,
        entities: Iterable[entity_bulk_create_params.Entity],
        bucket: str | Omit = omit,
        on_conflict: Literal["merge"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityBulkCreateResponse:
        """Bulk Seed Entities

        Args:
          entities: The entities to seed.

        Must be non-empty.

          bucket: Optional bucket public ID (`bkt_...`) to seed into. Omit to use the
              account+environment default bucket.

          on_conflict: Conflict strategy for an entity that already exists. Only `merge` is supported
              and it is the default: synonyms are added additively, a longer description
              replaces the old one, and attributes are merged with new keys winning.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/entities/bulk",
            body=maybe_transform(
                {
                    "entities": entities,
                    "bucket": bucket,
                    "on_conflict": on_conflict,
                },
                entity_bulk_create_params.EntityBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityBulkCreateResponse,
        )

    def bulk_validate(
        self,
        *,
        entity_ids: SequenceNotStr[str],
        status: Literal["approved", "rejected"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityBulkValidateResponse:
        """Bulk Validate Entities

        Args:
          entity_ids: The `ent_...` IDs to transition.

        Must be non-empty.

          status: Terminal status to apply to every entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/entities/bulk-validate",
            body=maybe_transform(
                {
                    "entity_ids": entity_ids,
                    "status": status,
                },
                entity_bulk_validate_params.EntityBulkValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityBulkValidateResponse,
        )

    def retrieve_relations(
        self,
        id: str,
        *,
        bucket: str | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["inbound", "outbound", "both"] | Omit = omit,
        limit: int | Omit = omit,
        relation_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityRetrieveRelationsResponse:
        """
        Get an Entity's Relations

        Args:
          bucket: Optional bucket public ID (`bkt_...`) to scope the read to one bucket. Omit for
              the unscoped (all account+environment) view.

          cursor: Cursor: return edges whose KSUID sorts after this value.

          direction: Which edges to return relative to the entity. Defaults to `both`.

          limit: Maximum number of edges to return (default 50, max 200).

          relation_type: Exact-match filter on the relation label.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v3/entities/{id}/relations", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bucket": bucket,
                        "cursor": cursor,
                        "direction": direction,
                        "limit": limit,
                        "relation_type": relation_type,
                    },
                    entity_retrieve_relations_params.EntityRetrieveRelationsParams,
                ),
            ),
            cast_to=EntityRetrieveRelationsResponse,
        )

    def retrieve_seed_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityRetrieveSeedStatusResponse:
        """
        Get Seed Job Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v3/entities/seed/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityRetrieveSeedStatusResponse,
        )


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def synonyms(self) -> AsyncSynonymsResource:
        """
        Manage the human-readable surface forms (synonyms) attached to a canonical
        entity. Synonyms feed the matcher's exact-match path, so adding the right
        synonyms improves cross-document entity resolution.

        - **`POST /v3/entities/{id}/synonyms`** attaches a `customer_defined`
          synonym. If the same normalized form already exists as an `extracted`
          synonym, it is upgraded to `customer_defined` (so the matcher weights it
          higher); an existing customer/SME synonym is returned unchanged.
        - **`DELETE /v3/entities/{id}/synonyms/{synonymID}`** soft-deletes a
          synonym. Only `customer_defined` and `sme_approved` synonyms are
          deletable; `extracted` synonyms are resolver-owned and the request is
          rejected with `409 Conflict`.

        A merged-away entity id transparently resolves to its surviving canonical
        entity, so a synonym added to a stale id lands on the entity that persists.
        """
        return AsyncSynonymsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        add_synonyms: SequenceNotStr[str] | Omit = omit,
        assigned_type_id: str | Omit = omit,
        canonical: str | Omit = omit,
        locale: str | Omit = omit,
        remove_synonym_ids: SequenceNotStr[str] | Omit = omit,
        status: Literal["approved", "rejected"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityUpdateResponse:
        """
        Update Entity

        Args:
          add_synonyms: Surface forms to attach as `customer_defined` synonyms.

          assigned_type_id: The `ety_...` public ID of the type to assign (overriding the bem-inferred
              type). The empty string clears the assignment. Omit to leave unchanged.

          canonical: Replace the entity's canonical surface form (re-derives its normalized form).

          locale: Optional BCP 47 locale tag stamped on any added synonyms.

          remove_synonym_ids: `esn_...` synonym IDs to soft-delete. Only `customer_defined` / `sme_approved`
              synonyms may be removed; an `extracted` synonym is rejected with `409`.

          status: Transition the entity's curation status. Only `approved` or `rejected` are
              accepted, and only from `extracted` or `proposed` (any other transition is
              rejected with `409`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v3/entities/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "add_synonyms": add_synonyms,
                    "assigned_type_id": assigned_type_id,
                    "canonical": canonical,
                    "locale": locale,
                    "remove_synonym_ids": remove_synonym_ids,
                    "status": status,
                },
                entity_update_params.EntityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityUpdateResponse,
        )

    async def bulk_create(
        self,
        *,
        entities: Iterable[entity_bulk_create_params.Entity],
        bucket: str | Omit = omit,
        on_conflict: Literal["merge"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityBulkCreateResponse:
        """Bulk Seed Entities

        Args:
          entities: The entities to seed.

        Must be non-empty.

          bucket: Optional bucket public ID (`bkt_...`) to seed into. Omit to use the
              account+environment default bucket.

          on_conflict: Conflict strategy for an entity that already exists. Only `merge` is supported
              and it is the default: synonyms are added additively, a longer description
              replaces the old one, and attributes are merged with new keys winning.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/entities/bulk",
            body=await async_maybe_transform(
                {
                    "entities": entities,
                    "bucket": bucket,
                    "on_conflict": on_conflict,
                },
                entity_bulk_create_params.EntityBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityBulkCreateResponse,
        )

    async def bulk_validate(
        self,
        *,
        entity_ids: SequenceNotStr[str],
        status: Literal["approved", "rejected"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityBulkValidateResponse:
        """Bulk Validate Entities

        Args:
          entity_ids: The `ent_...` IDs to transition.

        Must be non-empty.

          status: Terminal status to apply to every entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/entities/bulk-validate",
            body=await async_maybe_transform(
                {
                    "entity_ids": entity_ids,
                    "status": status,
                },
                entity_bulk_validate_params.EntityBulkValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityBulkValidateResponse,
        )

    async def retrieve_relations(
        self,
        id: str,
        *,
        bucket: str | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["inbound", "outbound", "both"] | Omit = omit,
        limit: int | Omit = omit,
        relation_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityRetrieveRelationsResponse:
        """
        Get an Entity's Relations

        Args:
          bucket: Optional bucket public ID (`bkt_...`) to scope the read to one bucket. Omit for
              the unscoped (all account+environment) view.

          cursor: Cursor: return edges whose KSUID sorts after this value.

          direction: Which edges to return relative to the entity. Defaults to `both`.

          limit: Maximum number of edges to return (default 50, max 200).

          relation_type: Exact-match filter on the relation label.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v3/entities/{id}/relations", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bucket": bucket,
                        "cursor": cursor,
                        "direction": direction,
                        "limit": limit,
                        "relation_type": relation_type,
                    },
                    entity_retrieve_relations_params.EntityRetrieveRelationsParams,
                ),
            ),
            cast_to=EntityRetrieveRelationsResponse,
        )

    async def retrieve_seed_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityRetrieveSeedStatusResponse:
        """
        Get Seed Job Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v3/entities/seed/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityRetrieveSeedStatusResponse,
        )


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.update = to_raw_response_wrapper(
            entities.update,
        )
        self.bulk_create = to_raw_response_wrapper(
            entities.bulk_create,
        )
        self.bulk_validate = to_raw_response_wrapper(
            entities.bulk_validate,
        )
        self.retrieve_relations = to_raw_response_wrapper(
            entities.retrieve_relations,
        )
        self.retrieve_seed_status = to_raw_response_wrapper(
            entities.retrieve_seed_status,
        )

    @cached_property
    def synonyms(self) -> SynonymsResourceWithRawResponse:
        """
        Manage the human-readable surface forms (synonyms) attached to a canonical
        entity. Synonyms feed the matcher's exact-match path, so adding the right
        synonyms improves cross-document entity resolution.

        - **`POST /v3/entities/{id}/synonyms`** attaches a `customer_defined`
          synonym. If the same normalized form already exists as an `extracted`
          synonym, it is upgraded to `customer_defined` (so the matcher weights it
          higher); an existing customer/SME synonym is returned unchanged.
        - **`DELETE /v3/entities/{id}/synonyms/{synonymID}`** soft-deletes a
          synonym. Only `customer_defined` and `sme_approved` synonyms are
          deletable; `extracted` synonyms are resolver-owned and the request is
          rejected with `409 Conflict`.

        A merged-away entity id transparently resolves to its surviving canonical
        entity, so a synonym added to a stale id lands on the entity that persists.
        """
        return SynonymsResourceWithRawResponse(self._entities.synonyms)


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.update = async_to_raw_response_wrapper(
            entities.update,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            entities.bulk_create,
        )
        self.bulk_validate = async_to_raw_response_wrapper(
            entities.bulk_validate,
        )
        self.retrieve_relations = async_to_raw_response_wrapper(
            entities.retrieve_relations,
        )
        self.retrieve_seed_status = async_to_raw_response_wrapper(
            entities.retrieve_seed_status,
        )

    @cached_property
    def synonyms(self) -> AsyncSynonymsResourceWithRawResponse:
        """
        Manage the human-readable surface forms (synonyms) attached to a canonical
        entity. Synonyms feed the matcher's exact-match path, so adding the right
        synonyms improves cross-document entity resolution.

        - **`POST /v3/entities/{id}/synonyms`** attaches a `customer_defined`
          synonym. If the same normalized form already exists as an `extracted`
          synonym, it is upgraded to `customer_defined` (so the matcher weights it
          higher); an existing customer/SME synonym is returned unchanged.
        - **`DELETE /v3/entities/{id}/synonyms/{synonymID}`** soft-deletes a
          synonym. Only `customer_defined` and `sme_approved` synonyms are
          deletable; `extracted` synonyms are resolver-owned and the request is
          rejected with `409 Conflict`.

        A merged-away entity id transparently resolves to its surviving canonical
        entity, so a synonym added to a stale id lands on the entity that persists.
        """
        return AsyncSynonymsResourceWithRawResponse(self._entities.synonyms)


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.update = to_streamed_response_wrapper(
            entities.update,
        )
        self.bulk_create = to_streamed_response_wrapper(
            entities.bulk_create,
        )
        self.bulk_validate = to_streamed_response_wrapper(
            entities.bulk_validate,
        )
        self.retrieve_relations = to_streamed_response_wrapper(
            entities.retrieve_relations,
        )
        self.retrieve_seed_status = to_streamed_response_wrapper(
            entities.retrieve_seed_status,
        )

    @cached_property
    def synonyms(self) -> SynonymsResourceWithStreamingResponse:
        """
        Manage the human-readable surface forms (synonyms) attached to a canonical
        entity. Synonyms feed the matcher's exact-match path, so adding the right
        synonyms improves cross-document entity resolution.

        - **`POST /v3/entities/{id}/synonyms`** attaches a `customer_defined`
          synonym. If the same normalized form already exists as an `extracted`
          synonym, it is upgraded to `customer_defined` (so the matcher weights it
          higher); an existing customer/SME synonym is returned unchanged.
        - **`DELETE /v3/entities/{id}/synonyms/{synonymID}`** soft-deletes a
          synonym. Only `customer_defined` and `sme_approved` synonyms are
          deletable; `extracted` synonyms are resolver-owned and the request is
          rejected with `409 Conflict`.

        A merged-away entity id transparently resolves to its surviving canonical
        entity, so a synonym added to a stale id lands on the entity that persists.
        """
        return SynonymsResourceWithStreamingResponse(self._entities.synonyms)


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.update = async_to_streamed_response_wrapper(
            entities.update,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            entities.bulk_create,
        )
        self.bulk_validate = async_to_streamed_response_wrapper(
            entities.bulk_validate,
        )
        self.retrieve_relations = async_to_streamed_response_wrapper(
            entities.retrieve_relations,
        )
        self.retrieve_seed_status = async_to_streamed_response_wrapper(
            entities.retrieve_seed_status,
        )

    @cached_property
    def synonyms(self) -> AsyncSynonymsResourceWithStreamingResponse:
        """
        Manage the human-readable surface forms (synonyms) attached to a canonical
        entity. Synonyms feed the matcher's exact-match path, so adding the right
        synonyms improves cross-document entity resolution.

        - **`POST /v3/entities/{id}/synonyms`** attaches a `customer_defined`
          synonym. If the same normalized form already exists as an `extracted`
          synonym, it is upgraded to `customer_defined` (so the matcher weights it
          higher); an existing customer/SME synonym is returned unchanged.
        - **`DELETE /v3/entities/{id}/synonyms/{synonymID}`** soft-deletes a
          synonym. Only `customer_defined` and `sme_approved` synonyms are
          deletable; `extracted` synonyms are resolver-owned and the request is
          rejected with `409 Conflict`.

        A merged-away entity id transparently resolves to its surviving canonical
        entity, so a synonym added to a stale id lands on the entity that persists.
        """
        return AsyncSynonymsResourceWithStreamingResponse(self._entities.synonyms)
