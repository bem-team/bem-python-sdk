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
from ..types.webhook_secret import WebhookSecret

__all__ = ["WebhookSecretResource", "AsyncWebhookSecretResource"]


class WebhookSecretResource(SyncAPIResource):
    """
    bem POSTs a JSON event to your configured webhook URL each time a subscribed function call, workflow output, or collection-processing job fires. This section is the reference for those deliveries: the payload shape per event type, plus the endpoints you use to manage the signing secret.

    Every variant shares the same envelope — function/workflow IDs, timestamps, the inbound email that triggered the call, and so on — and adds a payload field that depends on the function type. The `eventType` field on the body is the discriminator: dispatch on it to select which payload shape to expect. SDKs generated from this spec expose a `webhooks.unwrap()` helper that performs the dispatch and returns a typed event.

    ## Payloads

    | `eventType` | Payload | Schema |
    | --- | --- | --- |
    | `extract` | [Extract event](/api/v3/webhooks/events/extract) | `ExtractEvent` |
    | `classify` | [Classify event](/api/v3/webhooks/events/classify) | `ClassifyEvent` |
    | `parse` | [Parse event](/api/v3/webhooks/events/parse) | `ParseEvent` |
    | `split_collection` | [Split collection event](/api/v3/webhooks/events/split-collection) | `SplitCollectionEvent` |
    | `split_item` | [Split item event](/api/v3/webhooks/events/split-item) | `SplitItemEvent` |
    | `join` | [Join event](/api/v3/webhooks/events/join) | `JoinEvent` |
    | `enrich` | [Enrich event](/api/v3/webhooks/events/enrich) | `EnrichEvent` |
    | `payload_shaping` | [Payload shaping event](/api/v3/webhooks/events/payload-shaping) | `PayloadShapingEvent` |
    | `send` | [Send event](/api/v3/webhooks/events/send) | `SendEvent` |
    | `evaluation` | [Evaluation event](/api/v3/webhooks/events/evaluation) | `EvaluationEvent` |
    | `collection_processing` | [Collection processing event](/api/v3/webhooks/events/collection-processing) | `collectionProcessingEvent` |
    | `error` | [Error event](/api/v3/webhooks/events/error) | `ErrorEvent` |

    ## Signing secret

    Every delivery includes a `bem-signature` header in the format `t={unix_timestamp},v1={hex_hmac_sha256}`. The signature covers `{timestamp}.{raw_request_body}` and is computed with HMAC-SHA256 using the active signing secret for your environment.

    To verify a payload:

    1. Parse `bem-signature: t={timestamp},v1={signature}`.
    2. Construct the signed string: `{timestamp}.{raw_request_body}`.
    3. Compute HMAC-SHA256 of that string using your secret.
    4. Reject the request if the hex digest doesn't match `v1`, or if the timestamp is more than a few minutes old.

    Manage the secret with these endpoints:

    - [**Generate a signing secret**](/api/v3/webhooks/secret/generate-secret) — `POST /v3/webhook-secret`. Returns the new secret in full exactly once.
    - [**Get the signing secret**](/api/v3/webhooks/secret/get-secret) — `GET /v3/webhook-secret`. Returns the active secret.
    - [**Revoke the signing secret**](/api/v3/webhooks/secret/revoke-secret) — `DELETE /v3/webhook-secret`. Webhook deliveries continue but are unsigned until a new secret is generated.

    For zero-downtime rotation, briefly accept both the old and new secret in your verification logic before revoking the old one.

    ## Retries

    bem treats any non-2XX response (or a transport failure) as a delivery error and retries with exponential backoff. Return a 2XX as soon as you have durably queued the payload — do not block on downstream work.
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
    ) -> WebhookSecret:
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
            cast_to=WebhookSecret,
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
    ) -> WebhookSecret:
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
            cast_to=WebhookSecret,
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
    bem POSTs a JSON event to your configured webhook URL each time a subscribed function call, workflow output, or collection-processing job fires. This section is the reference for those deliveries: the payload shape per event type, plus the endpoints you use to manage the signing secret.

    Every variant shares the same envelope — function/workflow IDs, timestamps, the inbound email that triggered the call, and so on — and adds a payload field that depends on the function type. The `eventType` field on the body is the discriminator: dispatch on it to select which payload shape to expect. SDKs generated from this spec expose a `webhooks.unwrap()` helper that performs the dispatch and returns a typed event.

    ## Payloads

    | `eventType` | Payload | Schema |
    | --- | --- | --- |
    | `extract` | [Extract event](/api/v3/webhooks/events/extract) | `ExtractEvent` |
    | `classify` | [Classify event](/api/v3/webhooks/events/classify) | `ClassifyEvent` |
    | `parse` | [Parse event](/api/v3/webhooks/events/parse) | `ParseEvent` |
    | `split_collection` | [Split collection event](/api/v3/webhooks/events/split-collection) | `SplitCollectionEvent` |
    | `split_item` | [Split item event](/api/v3/webhooks/events/split-item) | `SplitItemEvent` |
    | `join` | [Join event](/api/v3/webhooks/events/join) | `JoinEvent` |
    | `enrich` | [Enrich event](/api/v3/webhooks/events/enrich) | `EnrichEvent` |
    | `payload_shaping` | [Payload shaping event](/api/v3/webhooks/events/payload-shaping) | `PayloadShapingEvent` |
    | `send` | [Send event](/api/v3/webhooks/events/send) | `SendEvent` |
    | `evaluation` | [Evaluation event](/api/v3/webhooks/events/evaluation) | `EvaluationEvent` |
    | `collection_processing` | [Collection processing event](/api/v3/webhooks/events/collection-processing) | `collectionProcessingEvent` |
    | `error` | [Error event](/api/v3/webhooks/events/error) | `ErrorEvent` |

    ## Signing secret

    Every delivery includes a `bem-signature` header in the format `t={unix_timestamp},v1={hex_hmac_sha256}`. The signature covers `{timestamp}.{raw_request_body}` and is computed with HMAC-SHA256 using the active signing secret for your environment.

    To verify a payload:

    1. Parse `bem-signature: t={timestamp},v1={signature}`.
    2. Construct the signed string: `{timestamp}.{raw_request_body}`.
    3. Compute HMAC-SHA256 of that string using your secret.
    4. Reject the request if the hex digest doesn't match `v1`, or if the timestamp is more than a few minutes old.

    Manage the secret with these endpoints:

    - [**Generate a signing secret**](/api/v3/webhooks/secret/generate-secret) — `POST /v3/webhook-secret`. Returns the new secret in full exactly once.
    - [**Get the signing secret**](/api/v3/webhooks/secret/get-secret) — `GET /v3/webhook-secret`. Returns the active secret.
    - [**Revoke the signing secret**](/api/v3/webhooks/secret/revoke-secret) — `DELETE /v3/webhook-secret`. Webhook deliveries continue but are unsigned until a new secret is generated.

    For zero-downtime rotation, briefly accept both the old and new secret in your verification logic before revoking the old one.

    ## Retries

    bem treats any non-2XX response (or a transport failure) as a delivery error and retries with exponential backoff. Return a 2XX as soon as you have durably queued the payload — do not block on downstream work.
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
    ) -> WebhookSecret:
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
            cast_to=WebhookSecret,
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
    ) -> WebhookSecret:
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
            cast_to=WebhookSecret,
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
