# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.entities import synonym_add_params, synonym_remove_params
from ...types.entities.synonym_add_response import SynonymAddResponse

__all__ = ["SynonymsResource", "AsyncSynonymsResource"]


class SynonymsResource(SyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> SynonymsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SynonymsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SynonymsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return SynonymsResourceWithStreamingResponse(self)

    def add(
        self,
        id: str,
        *,
        text: str,
        bucket: str | Omit = omit,
        locale: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SynonymAddResponse:
        """
        Add a Synonym to an Entity

        Args:
          text: The human-readable synonym surface form to attach (e.g. `Acme Corp`, `ACME`). It
              is normalized (lowercased, whitespace-folded) for the uniqueness key and the
              matcher's exact-match path.

          bucket: Optional bucket public ID (`bkt_...`) to scope the entity lookup to one bucket.
              Omit for the unscoped (all account+environment) view.

          locale: Optional BCP 47 locale tag (e.g. `en-US`) for language-specific synonyms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v3/entities/{id}/synonyms", id=id),
            body=maybe_transform(
                {
                    "text": text,
                    "locale": locale,
                },
                synonym_add_params.SynonymAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"bucket": bucket}, synonym_add_params.SynonymAddParams),
            ),
            cast_to=SynonymAddResponse,
        )

    def remove(
        self,
        synonym_id: str,
        *,
        id: str,
        bucket: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a Synonym from an Entity

        Args:
          bucket: Optional bucket public ID (`bkt_...`) to scope the entity lookup to one bucket.
              Omit for the unscoped (all account+environment) view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not synonym_id:
            raise ValueError(f"Expected a non-empty value for `synonym_id` but received {synonym_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/entities/{id}/synonyms/{synonym_id}", id=id, synonym_id=synonym_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"bucket": bucket}, synonym_remove_params.SynonymRemoveParams),
            ),
            cast_to=NoneType,
        )


class AsyncSynonymsResource(AsyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> AsyncSynonymsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSynonymsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSynonymsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncSynonymsResourceWithStreamingResponse(self)

    async def add(
        self,
        id: str,
        *,
        text: str,
        bucket: str | Omit = omit,
        locale: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SynonymAddResponse:
        """
        Add a Synonym to an Entity

        Args:
          text: The human-readable synonym surface form to attach (e.g. `Acme Corp`, `ACME`). It
              is normalized (lowercased, whitespace-folded) for the uniqueness key and the
              matcher's exact-match path.

          bucket: Optional bucket public ID (`bkt_...`) to scope the entity lookup to one bucket.
              Omit for the unscoped (all account+environment) view.

          locale: Optional BCP 47 locale tag (e.g. `en-US`) for language-specific synonyms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v3/entities/{id}/synonyms", id=id),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "locale": locale,
                },
                synonym_add_params.SynonymAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"bucket": bucket}, synonym_add_params.SynonymAddParams),
            ),
            cast_to=SynonymAddResponse,
        )

    async def remove(
        self,
        synonym_id: str,
        *,
        id: str,
        bucket: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a Synonym from an Entity

        Args:
          bucket: Optional bucket public ID (`bkt_...`) to scope the entity lookup to one bucket.
              Omit for the unscoped (all account+environment) view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not synonym_id:
            raise ValueError(f"Expected a non-empty value for `synonym_id` but received {synonym_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/entities/{id}/synonyms/{synonym_id}", id=id, synonym_id=synonym_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"bucket": bucket}, synonym_remove_params.SynonymRemoveParams),
            ),
            cast_to=NoneType,
        )


class SynonymsResourceWithRawResponse:
    def __init__(self, synonyms: SynonymsResource) -> None:
        self._synonyms = synonyms

        self.add = to_raw_response_wrapper(
            synonyms.add,
        )
        self.remove = to_raw_response_wrapper(
            synonyms.remove,
        )


class AsyncSynonymsResourceWithRawResponse:
    def __init__(self, synonyms: AsyncSynonymsResource) -> None:
        self._synonyms = synonyms

        self.add = async_to_raw_response_wrapper(
            synonyms.add,
        )
        self.remove = async_to_raw_response_wrapper(
            synonyms.remove,
        )


class SynonymsResourceWithStreamingResponse:
    def __init__(self, synonyms: SynonymsResource) -> None:
        self._synonyms = synonyms

        self.add = to_streamed_response_wrapper(
            synonyms.add,
        )
        self.remove = to_streamed_response_wrapper(
            synonyms.remove,
        )


class AsyncSynonymsResourceWithStreamingResponse:
    def __init__(self, synonyms: AsyncSynonymsResource) -> None:
        self._synonyms = synonyms

        self.add = async_to_streamed_response_wrapper(
            synonyms.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            synonyms.remove,
        )
