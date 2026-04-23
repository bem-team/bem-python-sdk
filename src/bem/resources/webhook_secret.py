# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.webhook_secret_create_response import WebhookSecretCreateResponse
from ..types.webhook_secret_retrieve_response import WebhookSecretRetrieveResponse

__all__ = ["WebhookSecretResource", "AsyncWebhookSecretResource"]


class WebhookSecretResource(SyncAPIResource):
    """
    Manage the webhook signing secret used to authenticate outbound webhook deliveries.

    When a signing secret is active, every webhook delivery includes a `bem-signature` header
    in the format `t={unix_timestamp},v1={hex_hmac_sha256}`. The signature covers
    `{timestamp}.{raw_request_body}` and can be verified using HMAC-SHA256 with your secret.

    Rotate the secret at any time with `POST /v3/webhook-secret`. To avoid downtime during
    rotation, update your verification logic to accept both the old and new secret briefly
    before revoking the old one.
    """

    @cached_property
    def with_raw_response(self) -> WebhookSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WebhookSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return WebhookSecretResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSecretCreateResponse:
        """
        **Generate a new webhook signing secret.**

        Creates a new signing secret for this environment (or replaces the existing
        one). The new secret is returned in full exactly once — store it securely.

        After rotation all newly delivered webhooks will be signed with the new secret.
        Update your verification logic before calling this endpoint if you need
        zero-downtime rotation.
        """
        return self._post(
            "/v3/webhook-secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSecretCreateResponse,
        )

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSecretRetrieveResponse:
        """
        **Get the current webhook signing secret.**

        Returns the active secret used to sign outbound webhook deliveries via the
        `bem-signature` header. Returns 404 if no secret has been generated for this
        environment yet.

        Use the secret to verify incoming webhook payloads:

        1. Parse `bem-signature: t={timestamp},v1={signature}`.
        2. Construct the signed string: `{timestamp}.{raw request body}`.
        3. Compute HMAC-SHA256 of that string using the secret.
        4. Compare the hex digest against `v1`.
        5. Reject requests where the timestamp is more than a few minutes old.
        """
        return self._get(
            "/v3/webhook-secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSecretRetrieveResponse,
        )

    def revoke(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        **Revoke the current webhook signing secret.**

        Deletes the active signing secret. Webhook deliveries will continue but will no
        longer include a `bem-signature` header until a new secret is generated.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/v3/webhook-secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWebhookSecretResource(AsyncAPIResource):
    """
    Manage the webhook signing secret used to authenticate outbound webhook deliveries.

    When a signing secret is active, every webhook delivery includes a `bem-signature` header
    in the format `t={unix_timestamp},v1={hex_hmac_sha256}`. The signature covers
    `{timestamp}.{raw_request_body}` and can be verified using HMAC-SHA256 with your secret.

    Rotate the secret at any time with `POST /v3/webhook-secret`. To avoid downtime during
    rotation, update your verification logic to accept both the old and new secret briefly
    before revoking the old one.
    """

    @cached_property
    def with_raw_response(self) -> AsyncWebhookSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncWebhookSecretResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSecretCreateResponse:
        """
        **Generate a new webhook signing secret.**

        Creates a new signing secret for this environment (or replaces the existing
        one). The new secret is returned in full exactly once — store it securely.

        After rotation all newly delivered webhooks will be signed with the new secret.
        Update your verification logic before calling this endpoint if you need
        zero-downtime rotation.
        """
        return await self._post(
            "/v3/webhook-secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSecretCreateResponse,
        )

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookSecretRetrieveResponse:
        """
        **Get the current webhook signing secret.**

        Returns the active secret used to sign outbound webhook deliveries via the
        `bem-signature` header. Returns 404 if no secret has been generated for this
        environment yet.

        Use the secret to verify incoming webhook payloads:

        1. Parse `bem-signature: t={timestamp},v1={signature}`.
        2. Construct the signed string: `{timestamp}.{raw request body}`.
        3. Compute HMAC-SHA256 of that string using the secret.
        4. Compare the hex digest against `v1`.
        5. Reject requests where the timestamp is more than a few minutes old.
        """
        return await self._get(
            "/v3/webhook-secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookSecretRetrieveResponse,
        )

    async def revoke(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        **Revoke the current webhook signing secret.**

        Deletes the active signing secret. Webhook deliveries will continue but will no
        longer include a `bem-signature` header until a new secret is generated.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/v3/webhook-secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WebhookSecretResourceWithRawResponse:
    def __init__(self, webhook_secret: WebhookSecretResource) -> None:
        self._webhook_secret = webhook_secret

        self.create = to_raw_response_wrapper(
            webhook_secret.create,
        )
        self.retrieve = to_raw_response_wrapper(
            webhook_secret.retrieve,
        )
        self.revoke = to_raw_response_wrapper(
            webhook_secret.revoke,
        )


class AsyncWebhookSecretResourceWithRawResponse:
    def __init__(self, webhook_secret: AsyncWebhookSecretResource) -> None:
        self._webhook_secret = webhook_secret

        self.create = async_to_raw_response_wrapper(
            webhook_secret.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            webhook_secret.retrieve,
        )
        self.revoke = async_to_raw_response_wrapper(
            webhook_secret.revoke,
        )


class WebhookSecretResourceWithStreamingResponse:
    def __init__(self, webhook_secret: WebhookSecretResource) -> None:
        self._webhook_secret = webhook_secret

        self.create = to_streamed_response_wrapper(
            webhook_secret.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhook_secret.retrieve,
        )
        self.revoke = to_streamed_response_wrapper(
            webhook_secret.revoke,
        )


class AsyncWebhookSecretResourceWithStreamingResponse:
    def __init__(self, webhook_secret: AsyncWebhookSecretResource) -> None:
        self._webhook_secret = webhook_secret

        self.create = async_to_streamed_response_wrapper(
            webhook_secret.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhook_secret.retrieve,
        )
        self.revoke = async_to_streamed_response_wrapper(
            webhook_secret.revoke,
        )
