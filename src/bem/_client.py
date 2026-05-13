# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import BemError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        fs,
        eval,
        calls,
        errors,
        events,
        outputs,
        functions,
        workflows,
        connectors,
        collections,
        infer_schema,
        subscriptions,
        webhook_secret,
    )
    from .resources.fs import FsResource, AsyncFsResource
    from .resources.calls import CallsResource, AsyncCallsResource
    from .resources.errors import ErrorsResource, AsyncErrorsResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.outputs import OutputsResource, AsyncOutputsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.eval.eval import EvalResource, AsyncEvalResource
    from .resources.connectors import ConnectorsResource, AsyncConnectorsResource
    from .resources.infer_schema import InferSchemaResource, AsyncInferSchemaResource
    from .resources.subscriptions import SubscriptionsResource, AsyncSubscriptionsResource
    from .resources.webhook_secret import WebhookSecretResource, AsyncWebhookSecretResource
    from .resources.functions.functions import FunctionsResource, AsyncFunctionsResource
    from .resources.workflows.workflows import WorkflowsResource, AsyncWorkflowsResource
    from .resources.collections.collections import CollectionsResource, AsyncCollectionsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Bem", "AsyncBem", "Client", "AsyncClient"]


class Bem(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Bem client instance.

        This automatically infers the `api_key` argument from the `BEM_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BEM_API_KEY")
        if api_key is None:
            raise BemError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BEM_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BEM_BASE_URL")
        if base_url is None:
            base_url = f"https://api.bem.ai"

        custom_headers_env = os.environ.get("BEM_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def functions(self) -> FunctionsResource:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        from .resources.functions import FunctionsResource

        return FunctionsResource(self)

    @cached_property
    def calls(self) -> CallsResource:
        """
        The Calls API provides a unified interface for invoking both **Workflows** and **Functions**.

        Use this API when you want to:
        - Execute a complete workflow that chains multiple functions together
        - Call a single function directly without defining a workflow
        - Submit batch requests with multiple inputs in a single API call
        - Track execution status using call reference IDs

        **Key Difference**: Calls vs Function Calls
        - **Calls API** (`/v3/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v3/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
        """
        from .resources.calls import CallsResource

        return CallsResource(self)

    @cached_property
    def errors(self) -> ErrorsResource:
        """Retrieve terminal error events from workflow calls.

        Errors are events produced by function steps that failed during processing. A single workflow
        call may produce multiple error events if several steps fail independently.

        Errors and outputs from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/errors` to list errors across calls, or `GET /v3/errors/{eventID}` to retrieve
        a specific error. To get errors scoped to a single call, filter by `callIDs`.
        """
        from .resources.errors import ErrorsResource

        return ErrorsResource(self)

    @cached_property
    def outputs(self) -> OutputsResource:
        """Retrieve terminal non-error output events from workflow calls.

        Outputs are events produced by successful terminal function steps — steps that completed
        without errors and did not spawn further downstream function calls. A single workflow call
        may produce multiple outputs (e.g. from a split-then-transform pipeline).

        Outputs and errors from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/outputs` to list outputs across calls, or `GET /v3/outputs/{eventID}` to
        retrieve a specific output. To get outputs scoped to a single call, filter by `callIDs`.
        """
        from .resources.outputs import OutputsResource

        return OutputsResource(self)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        from .resources.workflows import WorkflowsResource

        return WorkflowsResource(self)

    @cached_property
    def infer_schema(self) -> InferSchemaResource:
        """Infer JSON Schemas from uploaded documents using AI.

        Upload a file (PDF, image, spreadsheet, email, etc.) and receive a general-purpose JSON Schema
        that captures the document's structure. The inferred schema can be used directly as the
        `outputSchema` when creating Extract functions.

        The schema is designed to be broadly applicable to documents of the same type, not just
        the specific file uploaded.
        """
        from .resources.infer_schema import InferSchemaResource

        return InferSchemaResource(self)

    @cached_property
    def collections(self) -> CollectionsResource:
        """
        Collections are named groups of embedded items used by Enrich functions for semantic search.

        Each collection is referenced by a `collectionName`, which supports dot notation for
        hierarchical paths (e.g. `customers.premium.vip`). Names must contain only letters,
        digits, underscores, and dots, and each segment must start with a letter or underscore.

        ## Items

        Items carry either a string or a JSON object in their `data` field. When items are added
        or updated, their `data` is embedded asynchronously — `POST /v3/collections/items` and
        `PUT /v3/collections/items` return immediately with a `pending` status and an `eventID`
        that can be correlated with webhook notifications once processing completes.

        ## Listing and hierarchy

        Use `GET /v3/collections` with `parentCollectionName` to list collections under a path,
        or `collectionNameSearch` for a case-insensitive substring match. `GET /v3/collections/items`
        retrieves a specific collection's items; pass `includeSubcollections=true` to fold in items
        from all descendant collections.

        ## Token counting

        Use `POST /v3/collections/token-count` to check whether texts fit within the embedding
        model's 8,192-token-per-text limit before submitting them for embedding.
        """
        from .resources.collections import CollectionsResource

        return CollectionsResource(self)

    @cached_property
    def events(self) -> EventsResource:
        """Submit training corrections for `extract`, `classify`, and `join` events.

        Feedback is event-centric — each correction is attached to an event by its `eventID`,
        and the server resolves the correct underlying storage (extract/join transformations
        or classify route events) from the event's function type.

        Split and enrich function types do not support feedback.
        """
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def webhook_secret(self) -> WebhookSecretResource:
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
        from .resources.webhook_secret import WebhookSecretResource

        return WebhookSecretResource(self)

    @cached_property
    def eval(self) -> EvalResource:
        """
        Monitor, evaluate, and iterate on the quality of every function in your
        environment. Function Accuracy bundles two complementary loops:

        ## Evaluations (`/v3/eval`)

        Trigger and retrieve per-transformation evaluations. Evaluations run
        asynchronously and score each transformation's output against the
        function's schema for confidence, per-field hallucination detection,
        and relevance. Supported for `extract`, `transform`, `analyze`, and
        `join` events.

        1. **Trigger** — `POST /v3/eval` queues jobs for a batch of transformation IDs.
        2. **Poll** — `GET /v3/eval/results` returns the current state of each
           requested ID, partitioned into `results`, `pending`, and `failed`.
           Accepts either `eventIDs` (preferred) or `transformationIDs` as a
           comma-separated query parameter, and always keys the response by
           event KSUID.

        Up to 100 IDs may be submitted per request.

        ## Metrics, review, regression (`/v3/functions/{metrics,review,regression,compare}`)

        Roll evaluation results and user corrections up into actionable
        function-level signal:

        - **`GET /v3/functions/metrics`** — aggregate accuracy, precision,
          recall, F1, and confusion-matrix counts per function.
        - **`POST /v3/functions/review`** — sample-size estimation,
          confidence-bucketed distribution, PR-AUC, and per-threshold
          confidence intervals (Wald or Wilson) for picking review cutoffs.
        - **`POST /v3/functions/regression`** — replay corrected historical
          inputs against a new function version, producing a labeled
          regression dataset.
        - **`POST /v3/functions/regression/corrections`** — propagate
          baseline corrections onto the regression dataset so it can be
          scored.
        - **`POST /v3/functions/compare`** — compute aggregate and
          field-level lift between any two versions, optionally scoped to
          the regression dataset.

        All five endpoints support `extract` end-to-end on both the vision
        and OCR paths, alongside the legacy `transform` / `analyze` / `join`
        types.
        """
        from .resources.eval import EvalResource

        return EvalResource(self)

    @cached_property
    def fs(self) -> FsResource:
        """Unix-shell-style nav over parsed documents and the cross-doc memory store.

        `POST /v3/fs` is a single op-driven endpoint designed for LLM agents
        and programmatic consumers that want to walk a corpus the way they'd
        walk a filesystem.

        ## Doc-level ops (every parsed document)

        - `ls` — list parsed documents with rich per-doc metadata.
        - `cat` — read one doc's parse JSON, sliced (`range`) or projected (`select`).
        - `head` — first N sections of one doc.
        - `grep` — substring or regex search; `scope`, `path`, `countOnly` available.
        - `stat` — metadata only (page/section/entity counts, timestamps).

        ## Memory-level ops (require `linkAcrossDocuments: true` on the parse function)

        - `find` — list canonical entities across the corpus.
        - `open` — entity + mentions.
        - `xref` — for one entity, sections across docs that mention it (with content).

        Memory ops return an empty list with a `hint` when no docs in this
        environment have been memory-linked.

        ## Pagination

        List ops paginate by cursor — pass the previous response's `nextCursor`
        back as `cursor`; `hasMore: false` signals the last page. Same idiom as
        `/v3/calls` and `/v3/outputs`.
        """
        from .resources.fs import FsResource

        return FsResource(self)

    @cached_property
    def connectors(self) -> ConnectorsResource:
        """Connectors are integrations that trigger a Bem workflow from an external system.

        A connector binds an inbound source — currently Box or a Paragon-managed integration such as
        Google Drive — to a specific workflow (by `workflowName` or `workflowID`). When the source
        observes a new file, Bem invokes the bound workflow against that file.

        Use these endpoints to create, list, and remove connectors. The fields used at create time
        depend on the connector `type`: Box connectors require Box credentials and a folder to watch,
        while Paragon connectors carry a `paragonIntegration` identifier and an integration-specific
        `paragonConfiguration` object (for example, `{ "folderId": "..." }` for Google Drive).
        """
        from .resources.connectors import ConnectorsResource

        return ConnectorsResource(self)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        """
        Subscriptions wire up notifications for the events your functions and collections produce.

        Each subscription targets a single function (by `functionName` or `functionID`) or a single
        collection (by `collectionName` or `collectionID`) and selects a `type` corresponding to the
        event you want to receive — for example `transform`, `route`, `join`, `evaluation`, `error`,
        `enrich`, or `collection_processing`.

        Deliveries can be sent to any combination of:

        - `webhookURL` — HTTPS endpoint that receives a JSON POST per event.
        - `s3Bucket` + `s3FilePath` — sync output JSON into an AWS S3 prefix you own.
        - `googleDriveFolderID` — drop output JSON into a Google Drive folder.

        Use `disabled: true` to pause delivery without deleting the subscription. Updates follow
        conventional PATCH semantics — only the fields you include are changed.
        """
        from .resources.subscriptions import SubscriptionsResource

        return SubscriptionsResource(self)

    @cached_property
    def with_raw_response(self) -> BemWithRawResponse:
        return BemWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BemWithStreamedResponse:
        return BemWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key if security.get("api_key", False) else {}),
        }

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBem(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBem client instance.

        This automatically infers the `api_key` argument from the `BEM_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BEM_API_KEY")
        if api_key is None:
            raise BemError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BEM_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BEM_BASE_URL")
        if base_url is None:
            base_url = f"https://api.bem.ai"

        custom_headers_env = os.environ.get("BEM_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        from .resources.functions import AsyncFunctionsResource

        return AsyncFunctionsResource(self)

    @cached_property
    def calls(self) -> AsyncCallsResource:
        """
        The Calls API provides a unified interface for invoking both **Workflows** and **Functions**.

        Use this API when you want to:
        - Execute a complete workflow that chains multiple functions together
        - Call a single function directly without defining a workflow
        - Submit batch requests with multiple inputs in a single API call
        - Track execution status using call reference IDs

        **Key Difference**: Calls vs Function Calls
        - **Calls API** (`/v3/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v3/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
        """
        from .resources.calls import AsyncCallsResource

        return AsyncCallsResource(self)

    @cached_property
    def errors(self) -> AsyncErrorsResource:
        """Retrieve terminal error events from workflow calls.

        Errors are events produced by function steps that failed during processing. A single workflow
        call may produce multiple error events if several steps fail independently.

        Errors and outputs from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/errors` to list errors across calls, or `GET /v3/errors/{eventID}` to retrieve
        a specific error. To get errors scoped to a single call, filter by `callIDs`.
        """
        from .resources.errors import AsyncErrorsResource

        return AsyncErrorsResource(self)

    @cached_property
    def outputs(self) -> AsyncOutputsResource:
        """Retrieve terminal non-error output events from workflow calls.

        Outputs are events produced by successful terminal function steps — steps that completed
        without errors and did not spawn further downstream function calls. A single workflow call
        may produce multiple outputs (e.g. from a split-then-transform pipeline).

        Outputs and errors from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/outputs` to list outputs across calls, or `GET /v3/outputs/{eventID}` to
        retrieve a specific output. To get outputs scoped to a single call, filter by `callIDs`.
        """
        from .resources.outputs import AsyncOutputsResource

        return AsyncOutputsResource(self)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        from .resources.workflows import AsyncWorkflowsResource

        return AsyncWorkflowsResource(self)

    @cached_property
    def infer_schema(self) -> AsyncInferSchemaResource:
        """Infer JSON Schemas from uploaded documents using AI.

        Upload a file (PDF, image, spreadsheet, email, etc.) and receive a general-purpose JSON Schema
        that captures the document's structure. The inferred schema can be used directly as the
        `outputSchema` when creating Extract functions.

        The schema is designed to be broadly applicable to documents of the same type, not just
        the specific file uploaded.
        """
        from .resources.infer_schema import AsyncInferSchemaResource

        return AsyncInferSchemaResource(self)

    @cached_property
    def collections(self) -> AsyncCollectionsResource:
        """
        Collections are named groups of embedded items used by Enrich functions for semantic search.

        Each collection is referenced by a `collectionName`, which supports dot notation for
        hierarchical paths (e.g. `customers.premium.vip`). Names must contain only letters,
        digits, underscores, and dots, and each segment must start with a letter or underscore.

        ## Items

        Items carry either a string or a JSON object in their `data` field. When items are added
        or updated, their `data` is embedded asynchronously — `POST /v3/collections/items` and
        `PUT /v3/collections/items` return immediately with a `pending` status and an `eventID`
        that can be correlated with webhook notifications once processing completes.

        ## Listing and hierarchy

        Use `GET /v3/collections` with `parentCollectionName` to list collections under a path,
        or `collectionNameSearch` for a case-insensitive substring match. `GET /v3/collections/items`
        retrieves a specific collection's items; pass `includeSubcollections=true` to fold in items
        from all descendant collections.

        ## Token counting

        Use `POST /v3/collections/token-count` to check whether texts fit within the embedding
        model's 8,192-token-per-text limit before submitting them for embedding.
        """
        from .resources.collections import AsyncCollectionsResource

        return AsyncCollectionsResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        """Submit training corrections for `extract`, `classify`, and `join` events.

        Feedback is event-centric — each correction is attached to an event by its `eventID`,
        and the server resolves the correct underlying storage (extract/join transformations
        or classify route events) from the event's function type.

        Split and enrich function types do not support feedback.
        """
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def webhook_secret(self) -> AsyncWebhookSecretResource:
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
        from .resources.webhook_secret import AsyncWebhookSecretResource

        return AsyncWebhookSecretResource(self)

    @cached_property
    def eval(self) -> AsyncEvalResource:
        """
        Monitor, evaluate, and iterate on the quality of every function in your
        environment. Function Accuracy bundles two complementary loops:

        ## Evaluations (`/v3/eval`)

        Trigger and retrieve per-transformation evaluations. Evaluations run
        asynchronously and score each transformation's output against the
        function's schema for confidence, per-field hallucination detection,
        and relevance. Supported for `extract`, `transform`, `analyze`, and
        `join` events.

        1. **Trigger** — `POST /v3/eval` queues jobs for a batch of transformation IDs.
        2. **Poll** — `GET /v3/eval/results` returns the current state of each
           requested ID, partitioned into `results`, `pending`, and `failed`.
           Accepts either `eventIDs` (preferred) or `transformationIDs` as a
           comma-separated query parameter, and always keys the response by
           event KSUID.

        Up to 100 IDs may be submitted per request.

        ## Metrics, review, regression (`/v3/functions/{metrics,review,regression,compare}`)

        Roll evaluation results and user corrections up into actionable
        function-level signal:

        - **`GET /v3/functions/metrics`** — aggregate accuracy, precision,
          recall, F1, and confusion-matrix counts per function.
        - **`POST /v3/functions/review`** — sample-size estimation,
          confidence-bucketed distribution, PR-AUC, and per-threshold
          confidence intervals (Wald or Wilson) for picking review cutoffs.
        - **`POST /v3/functions/regression`** — replay corrected historical
          inputs against a new function version, producing a labeled
          regression dataset.
        - **`POST /v3/functions/regression/corrections`** — propagate
          baseline corrections onto the regression dataset so it can be
          scored.
        - **`POST /v3/functions/compare`** — compute aggregate and
          field-level lift between any two versions, optionally scoped to
          the regression dataset.

        All five endpoints support `extract` end-to-end on both the vision
        and OCR paths, alongside the legacy `transform` / `analyze` / `join`
        types.
        """
        from .resources.eval import AsyncEvalResource

        return AsyncEvalResource(self)

    @cached_property
    def fs(self) -> AsyncFsResource:
        """Unix-shell-style nav over parsed documents and the cross-doc memory store.

        `POST /v3/fs` is a single op-driven endpoint designed for LLM agents
        and programmatic consumers that want to walk a corpus the way they'd
        walk a filesystem.

        ## Doc-level ops (every parsed document)

        - `ls` — list parsed documents with rich per-doc metadata.
        - `cat` — read one doc's parse JSON, sliced (`range`) or projected (`select`).
        - `head` — first N sections of one doc.
        - `grep` — substring or regex search; `scope`, `path`, `countOnly` available.
        - `stat` — metadata only (page/section/entity counts, timestamps).

        ## Memory-level ops (require `linkAcrossDocuments: true` on the parse function)

        - `find` — list canonical entities across the corpus.
        - `open` — entity + mentions.
        - `xref` — for one entity, sections across docs that mention it (with content).

        Memory ops return an empty list with a `hint` when no docs in this
        environment have been memory-linked.

        ## Pagination

        List ops paginate by cursor — pass the previous response's `nextCursor`
        back as `cursor`; `hasMore: false` signals the last page. Same idiom as
        `/v3/calls` and `/v3/outputs`.
        """
        from .resources.fs import AsyncFsResource

        return AsyncFsResource(self)

    @cached_property
    def connectors(self) -> AsyncConnectorsResource:
        """Connectors are integrations that trigger a Bem workflow from an external system.

        A connector binds an inbound source — currently Box or a Paragon-managed integration such as
        Google Drive — to a specific workflow (by `workflowName` or `workflowID`). When the source
        observes a new file, Bem invokes the bound workflow against that file.

        Use these endpoints to create, list, and remove connectors. The fields used at create time
        depend on the connector `type`: Box connectors require Box credentials and a folder to watch,
        while Paragon connectors carry a `paragonIntegration` identifier and an integration-specific
        `paragonConfiguration` object (for example, `{ "folderId": "..." }` for Google Drive).
        """
        from .resources.connectors import AsyncConnectorsResource

        return AsyncConnectorsResource(self)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        """
        Subscriptions wire up notifications for the events your functions and collections produce.

        Each subscription targets a single function (by `functionName` or `functionID`) or a single
        collection (by `collectionName` or `collectionID`) and selects a `type` corresponding to the
        event you want to receive — for example `transform`, `route`, `join`, `evaluation`, `error`,
        `enrich`, or `collection_processing`.

        Deliveries can be sent to any combination of:

        - `webhookURL` — HTTPS endpoint that receives a JSON POST per event.
        - `s3Bucket` + `s3FilePath` — sync output JSON into an AWS S3 prefix you own.
        - `googleDriveFolderID` — drop output JSON into a Google Drive folder.

        Use `disabled: true` to pause delivery without deleting the subscription. Updates follow
        conventional PATCH semantics — only the fields you include are changed.
        """
        from .resources.subscriptions import AsyncSubscriptionsResource

        return AsyncSubscriptionsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncBemWithRawResponse:
        return AsyncBemWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBemWithStreamedResponse:
        return AsyncBemWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key if security.get("api_key", False) else {}),
        }

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BemWithRawResponse:
    _client: Bem

    def __init__(self, client: Bem) -> None:
        self._client = client

    @cached_property
    def functions(self) -> functions.FunctionsResourceWithRawResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        from .resources.functions import FunctionsResourceWithRawResponse

        return FunctionsResourceWithRawResponse(self._client.functions)

    @cached_property
    def calls(self) -> calls.CallsResourceWithRawResponse:
        """
        The Calls API provides a unified interface for invoking both **Workflows** and **Functions**.

        Use this API when you want to:
        - Execute a complete workflow that chains multiple functions together
        - Call a single function directly without defining a workflow
        - Submit batch requests with multiple inputs in a single API call
        - Track execution status using call reference IDs

        **Key Difference**: Calls vs Function Calls
        - **Calls API** (`/v3/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v3/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
        """
        from .resources.calls import CallsResourceWithRawResponse

        return CallsResourceWithRawResponse(self._client.calls)

    @cached_property
    def errors(self) -> errors.ErrorsResourceWithRawResponse:
        """Retrieve terminal error events from workflow calls.

        Errors are events produced by function steps that failed during processing. A single workflow
        call may produce multiple error events if several steps fail independently.

        Errors and outputs from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/errors` to list errors across calls, or `GET /v3/errors/{eventID}` to retrieve
        a specific error. To get errors scoped to a single call, filter by `callIDs`.
        """
        from .resources.errors import ErrorsResourceWithRawResponse

        return ErrorsResourceWithRawResponse(self._client.errors)

    @cached_property
    def outputs(self) -> outputs.OutputsResourceWithRawResponse:
        """Retrieve terminal non-error output events from workflow calls.

        Outputs are events produced by successful terminal function steps — steps that completed
        without errors and did not spawn further downstream function calls. A single workflow call
        may produce multiple outputs (e.g. from a split-then-transform pipeline).

        Outputs and errors from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/outputs` to list outputs across calls, or `GET /v3/outputs/{eventID}` to
        retrieve a specific output. To get outputs scoped to a single call, filter by `callIDs`.
        """
        from .resources.outputs import OutputsResourceWithRawResponse

        return OutputsResourceWithRawResponse(self._client.outputs)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithRawResponse:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        from .resources.workflows import WorkflowsResourceWithRawResponse

        return WorkflowsResourceWithRawResponse(self._client.workflows)

    @cached_property
    def infer_schema(self) -> infer_schema.InferSchemaResourceWithRawResponse:
        """Infer JSON Schemas from uploaded documents using AI.

        Upload a file (PDF, image, spreadsheet, email, etc.) and receive a general-purpose JSON Schema
        that captures the document's structure. The inferred schema can be used directly as the
        `outputSchema` when creating Extract functions.

        The schema is designed to be broadly applicable to documents of the same type, not just
        the specific file uploaded.
        """
        from .resources.infer_schema import InferSchemaResourceWithRawResponse

        return InferSchemaResourceWithRawResponse(self._client.infer_schema)

    @cached_property
    def collections(self) -> collections.CollectionsResourceWithRawResponse:
        """
        Collections are named groups of embedded items used by Enrich functions for semantic search.

        Each collection is referenced by a `collectionName`, which supports dot notation for
        hierarchical paths (e.g. `customers.premium.vip`). Names must contain only letters,
        digits, underscores, and dots, and each segment must start with a letter or underscore.

        ## Items

        Items carry either a string or a JSON object in their `data` field. When items are added
        or updated, their `data` is embedded asynchronously — `POST /v3/collections/items` and
        `PUT /v3/collections/items` return immediately with a `pending` status and an `eventID`
        that can be correlated with webhook notifications once processing completes.

        ## Listing and hierarchy

        Use `GET /v3/collections` with `parentCollectionName` to list collections under a path,
        or `collectionNameSearch` for a case-insensitive substring match. `GET /v3/collections/items`
        retrieves a specific collection's items; pass `includeSubcollections=true` to fold in items
        from all descendant collections.

        ## Token counting

        Use `POST /v3/collections/token-count` to check whether texts fit within the embedding
        model's 8,192-token-per-text limit before submitting them for embedding.
        """
        from .resources.collections import CollectionsResourceWithRawResponse

        return CollectionsResourceWithRawResponse(self._client.collections)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        """Submit training corrections for `extract`, `classify`, and `join` events.

        Feedback is event-centric — each correction is attached to an event by its `eventID`,
        and the server resolves the correct underlying storage (extract/join transformations
        or classify route events) from the event's function type.

        Split and enrich function types do not support feedback.
        """
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def webhook_secret(self) -> webhook_secret.WebhookSecretResourceWithRawResponse:
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
        from .resources.webhook_secret import WebhookSecretResourceWithRawResponse

        return WebhookSecretResourceWithRawResponse(self._client.webhook_secret)

    @cached_property
    def eval(self) -> eval.EvalResourceWithRawResponse:
        """
        Monitor, evaluate, and iterate on the quality of every function in your
        environment. Function Accuracy bundles two complementary loops:

        ## Evaluations (`/v3/eval`)

        Trigger and retrieve per-transformation evaluations. Evaluations run
        asynchronously and score each transformation's output against the
        function's schema for confidence, per-field hallucination detection,
        and relevance. Supported for `extract`, `transform`, `analyze`, and
        `join` events.

        1. **Trigger** — `POST /v3/eval` queues jobs for a batch of transformation IDs.
        2. **Poll** — `GET /v3/eval/results` returns the current state of each
           requested ID, partitioned into `results`, `pending`, and `failed`.
           Accepts either `eventIDs` (preferred) or `transformationIDs` as a
           comma-separated query parameter, and always keys the response by
           event KSUID.

        Up to 100 IDs may be submitted per request.

        ## Metrics, review, regression (`/v3/functions/{metrics,review,regression,compare}`)

        Roll evaluation results and user corrections up into actionable
        function-level signal:

        - **`GET /v3/functions/metrics`** — aggregate accuracy, precision,
          recall, F1, and confusion-matrix counts per function.
        - **`POST /v3/functions/review`** — sample-size estimation,
          confidence-bucketed distribution, PR-AUC, and per-threshold
          confidence intervals (Wald or Wilson) for picking review cutoffs.
        - **`POST /v3/functions/regression`** — replay corrected historical
          inputs against a new function version, producing a labeled
          regression dataset.
        - **`POST /v3/functions/regression/corrections`** — propagate
          baseline corrections onto the regression dataset so it can be
          scored.
        - **`POST /v3/functions/compare`** — compute aggregate and
          field-level lift between any two versions, optionally scoped to
          the regression dataset.

        All five endpoints support `extract` end-to-end on both the vision
        and OCR paths, alongside the legacy `transform` / `analyze` / `join`
        types.
        """
        from .resources.eval import EvalResourceWithRawResponse

        return EvalResourceWithRawResponse(self._client.eval)

    @cached_property
    def fs(self) -> fs.FsResourceWithRawResponse:
        """Unix-shell-style nav over parsed documents and the cross-doc memory store.

        `POST /v3/fs` is a single op-driven endpoint designed for LLM agents
        and programmatic consumers that want to walk a corpus the way they'd
        walk a filesystem.

        ## Doc-level ops (every parsed document)

        - `ls` — list parsed documents with rich per-doc metadata.
        - `cat` — read one doc's parse JSON, sliced (`range`) or projected (`select`).
        - `head` — first N sections of one doc.
        - `grep` — substring or regex search; `scope`, `path`, `countOnly` available.
        - `stat` — metadata only (page/section/entity counts, timestamps).

        ## Memory-level ops (require `linkAcrossDocuments: true` on the parse function)

        - `find` — list canonical entities across the corpus.
        - `open` — entity + mentions.
        - `xref` — for one entity, sections across docs that mention it (with content).

        Memory ops return an empty list with a `hint` when no docs in this
        environment have been memory-linked.

        ## Pagination

        List ops paginate by cursor — pass the previous response's `nextCursor`
        back as `cursor`; `hasMore: false` signals the last page. Same idiom as
        `/v3/calls` and `/v3/outputs`.
        """
        from .resources.fs import FsResourceWithRawResponse

        return FsResourceWithRawResponse(self._client.fs)

    @cached_property
    def connectors(self) -> connectors.ConnectorsResourceWithRawResponse:
        """Connectors are integrations that trigger a Bem workflow from an external system.

        A connector binds an inbound source — currently Box or a Paragon-managed integration such as
        Google Drive — to a specific workflow (by `workflowName` or `workflowID`). When the source
        observes a new file, Bem invokes the bound workflow against that file.

        Use these endpoints to create, list, and remove connectors. The fields used at create time
        depend on the connector `type`: Box connectors require Box credentials and a folder to watch,
        while Paragon connectors carry a `paragonIntegration` identifier and an integration-specific
        `paragonConfiguration` object (for example, `{ "folderId": "..." }` for Google Drive).
        """
        from .resources.connectors import ConnectorsResourceWithRawResponse

        return ConnectorsResourceWithRawResponse(self._client.connectors)

    @cached_property
    def subscriptions(self) -> subscriptions.SubscriptionsResourceWithRawResponse:
        """
        Subscriptions wire up notifications for the events your functions and collections produce.

        Each subscription targets a single function (by `functionName` or `functionID`) or a single
        collection (by `collectionName` or `collectionID`) and selects a `type` corresponding to the
        event you want to receive — for example `transform`, `route`, `join`, `evaluation`, `error`,
        `enrich`, or `collection_processing`.

        Deliveries can be sent to any combination of:

        - `webhookURL` — HTTPS endpoint that receives a JSON POST per event.
        - `s3Bucket` + `s3FilePath` — sync output JSON into an AWS S3 prefix you own.
        - `googleDriveFolderID` — drop output JSON into a Google Drive folder.

        Use `disabled: true` to pause delivery without deleting the subscription. Updates follow
        conventional PATCH semantics — only the fields you include are changed.
        """
        from .resources.subscriptions import SubscriptionsResourceWithRawResponse

        return SubscriptionsResourceWithRawResponse(self._client.subscriptions)


class AsyncBemWithRawResponse:
    _client: AsyncBem

    def __init__(self, client: AsyncBem) -> None:
        self._client = client

    @cached_property
    def functions(self) -> functions.AsyncFunctionsResourceWithRawResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        from .resources.functions import AsyncFunctionsResourceWithRawResponse

        return AsyncFunctionsResourceWithRawResponse(self._client.functions)

    @cached_property
    def calls(self) -> calls.AsyncCallsResourceWithRawResponse:
        """
        The Calls API provides a unified interface for invoking both **Workflows** and **Functions**.

        Use this API when you want to:
        - Execute a complete workflow that chains multiple functions together
        - Call a single function directly without defining a workflow
        - Submit batch requests with multiple inputs in a single API call
        - Track execution status using call reference IDs

        **Key Difference**: Calls vs Function Calls
        - **Calls API** (`/v3/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v3/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
        """
        from .resources.calls import AsyncCallsResourceWithRawResponse

        return AsyncCallsResourceWithRawResponse(self._client.calls)

    @cached_property
    def errors(self) -> errors.AsyncErrorsResourceWithRawResponse:
        """Retrieve terminal error events from workflow calls.

        Errors are events produced by function steps that failed during processing. A single workflow
        call may produce multiple error events if several steps fail independently.

        Errors and outputs from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/errors` to list errors across calls, or `GET /v3/errors/{eventID}` to retrieve
        a specific error. To get errors scoped to a single call, filter by `callIDs`.
        """
        from .resources.errors import AsyncErrorsResourceWithRawResponse

        return AsyncErrorsResourceWithRawResponse(self._client.errors)

    @cached_property
    def outputs(self) -> outputs.AsyncOutputsResourceWithRawResponse:
        """Retrieve terminal non-error output events from workflow calls.

        Outputs are events produced by successful terminal function steps — steps that completed
        without errors and did not spawn further downstream function calls. A single workflow call
        may produce multiple outputs (e.g. from a split-then-transform pipeline).

        Outputs and errors from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/outputs` to list outputs across calls, or `GET /v3/outputs/{eventID}` to
        retrieve a specific output. To get outputs scoped to a single call, filter by `callIDs`.
        """
        from .resources.outputs import AsyncOutputsResourceWithRawResponse

        return AsyncOutputsResourceWithRawResponse(self._client.outputs)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithRawResponse:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        from .resources.workflows import AsyncWorkflowsResourceWithRawResponse

        return AsyncWorkflowsResourceWithRawResponse(self._client.workflows)

    @cached_property
    def infer_schema(self) -> infer_schema.AsyncInferSchemaResourceWithRawResponse:
        """Infer JSON Schemas from uploaded documents using AI.

        Upload a file (PDF, image, spreadsheet, email, etc.) and receive a general-purpose JSON Schema
        that captures the document's structure. The inferred schema can be used directly as the
        `outputSchema` when creating Extract functions.

        The schema is designed to be broadly applicable to documents of the same type, not just
        the specific file uploaded.
        """
        from .resources.infer_schema import AsyncInferSchemaResourceWithRawResponse

        return AsyncInferSchemaResourceWithRawResponse(self._client.infer_schema)

    @cached_property
    def collections(self) -> collections.AsyncCollectionsResourceWithRawResponse:
        """
        Collections are named groups of embedded items used by Enrich functions for semantic search.

        Each collection is referenced by a `collectionName`, which supports dot notation for
        hierarchical paths (e.g. `customers.premium.vip`). Names must contain only letters,
        digits, underscores, and dots, and each segment must start with a letter or underscore.

        ## Items

        Items carry either a string or a JSON object in their `data` field. When items are added
        or updated, their `data` is embedded asynchronously — `POST /v3/collections/items` and
        `PUT /v3/collections/items` return immediately with a `pending` status and an `eventID`
        that can be correlated with webhook notifications once processing completes.

        ## Listing and hierarchy

        Use `GET /v3/collections` with `parentCollectionName` to list collections under a path,
        or `collectionNameSearch` for a case-insensitive substring match. `GET /v3/collections/items`
        retrieves a specific collection's items; pass `includeSubcollections=true` to fold in items
        from all descendant collections.

        ## Token counting

        Use `POST /v3/collections/token-count` to check whether texts fit within the embedding
        model's 8,192-token-per-text limit before submitting them for embedding.
        """
        from .resources.collections import AsyncCollectionsResourceWithRawResponse

        return AsyncCollectionsResourceWithRawResponse(self._client.collections)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        """Submit training corrections for `extract`, `classify`, and `join` events.

        Feedback is event-centric — each correction is attached to an event by its `eventID`,
        and the server resolves the correct underlying storage (extract/join transformations
        or classify route events) from the event's function type.

        Split and enrich function types do not support feedback.
        """
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def webhook_secret(self) -> webhook_secret.AsyncWebhookSecretResourceWithRawResponse:
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
        from .resources.webhook_secret import AsyncWebhookSecretResourceWithRawResponse

        return AsyncWebhookSecretResourceWithRawResponse(self._client.webhook_secret)

    @cached_property
    def eval(self) -> eval.AsyncEvalResourceWithRawResponse:
        """
        Monitor, evaluate, and iterate on the quality of every function in your
        environment. Function Accuracy bundles two complementary loops:

        ## Evaluations (`/v3/eval`)

        Trigger and retrieve per-transformation evaluations. Evaluations run
        asynchronously and score each transformation's output against the
        function's schema for confidence, per-field hallucination detection,
        and relevance. Supported for `extract`, `transform`, `analyze`, and
        `join` events.

        1. **Trigger** — `POST /v3/eval` queues jobs for a batch of transformation IDs.
        2. **Poll** — `GET /v3/eval/results` returns the current state of each
           requested ID, partitioned into `results`, `pending`, and `failed`.
           Accepts either `eventIDs` (preferred) or `transformationIDs` as a
           comma-separated query parameter, and always keys the response by
           event KSUID.

        Up to 100 IDs may be submitted per request.

        ## Metrics, review, regression (`/v3/functions/{metrics,review,regression,compare}`)

        Roll evaluation results and user corrections up into actionable
        function-level signal:

        - **`GET /v3/functions/metrics`** — aggregate accuracy, precision,
          recall, F1, and confusion-matrix counts per function.
        - **`POST /v3/functions/review`** — sample-size estimation,
          confidence-bucketed distribution, PR-AUC, and per-threshold
          confidence intervals (Wald or Wilson) for picking review cutoffs.
        - **`POST /v3/functions/regression`** — replay corrected historical
          inputs against a new function version, producing a labeled
          regression dataset.
        - **`POST /v3/functions/regression/corrections`** — propagate
          baseline corrections onto the regression dataset so it can be
          scored.
        - **`POST /v3/functions/compare`** — compute aggregate and
          field-level lift between any two versions, optionally scoped to
          the regression dataset.

        All five endpoints support `extract` end-to-end on both the vision
        and OCR paths, alongside the legacy `transform` / `analyze` / `join`
        types.
        """
        from .resources.eval import AsyncEvalResourceWithRawResponse

        return AsyncEvalResourceWithRawResponse(self._client.eval)

    @cached_property
    def fs(self) -> fs.AsyncFsResourceWithRawResponse:
        """Unix-shell-style nav over parsed documents and the cross-doc memory store.

        `POST /v3/fs` is a single op-driven endpoint designed for LLM agents
        and programmatic consumers that want to walk a corpus the way they'd
        walk a filesystem.

        ## Doc-level ops (every parsed document)

        - `ls` — list parsed documents with rich per-doc metadata.
        - `cat` — read one doc's parse JSON, sliced (`range`) or projected (`select`).
        - `head` — first N sections of one doc.
        - `grep` — substring or regex search; `scope`, `path`, `countOnly` available.
        - `stat` — metadata only (page/section/entity counts, timestamps).

        ## Memory-level ops (require `linkAcrossDocuments: true` on the parse function)

        - `find` — list canonical entities across the corpus.
        - `open` — entity + mentions.
        - `xref` — for one entity, sections across docs that mention it (with content).

        Memory ops return an empty list with a `hint` when no docs in this
        environment have been memory-linked.

        ## Pagination

        List ops paginate by cursor — pass the previous response's `nextCursor`
        back as `cursor`; `hasMore: false` signals the last page. Same idiom as
        `/v3/calls` and `/v3/outputs`.
        """
        from .resources.fs import AsyncFsResourceWithRawResponse

        return AsyncFsResourceWithRawResponse(self._client.fs)

    @cached_property
    def connectors(self) -> connectors.AsyncConnectorsResourceWithRawResponse:
        """Connectors are integrations that trigger a Bem workflow from an external system.

        A connector binds an inbound source — currently Box or a Paragon-managed integration such as
        Google Drive — to a specific workflow (by `workflowName` or `workflowID`). When the source
        observes a new file, Bem invokes the bound workflow against that file.

        Use these endpoints to create, list, and remove connectors. The fields used at create time
        depend on the connector `type`: Box connectors require Box credentials and a folder to watch,
        while Paragon connectors carry a `paragonIntegration` identifier and an integration-specific
        `paragonConfiguration` object (for example, `{ "folderId": "..." }` for Google Drive).
        """
        from .resources.connectors import AsyncConnectorsResourceWithRawResponse

        return AsyncConnectorsResourceWithRawResponse(self._client.connectors)

    @cached_property
    def subscriptions(self) -> subscriptions.AsyncSubscriptionsResourceWithRawResponse:
        """
        Subscriptions wire up notifications for the events your functions and collections produce.

        Each subscription targets a single function (by `functionName` or `functionID`) or a single
        collection (by `collectionName` or `collectionID`) and selects a `type` corresponding to the
        event you want to receive — for example `transform`, `route`, `join`, `evaluation`, `error`,
        `enrich`, or `collection_processing`.

        Deliveries can be sent to any combination of:

        - `webhookURL` — HTTPS endpoint that receives a JSON POST per event.
        - `s3Bucket` + `s3FilePath` — sync output JSON into an AWS S3 prefix you own.
        - `googleDriveFolderID` — drop output JSON into a Google Drive folder.

        Use `disabled: true` to pause delivery without deleting the subscription. Updates follow
        conventional PATCH semantics — only the fields you include are changed.
        """
        from .resources.subscriptions import AsyncSubscriptionsResourceWithRawResponse

        return AsyncSubscriptionsResourceWithRawResponse(self._client.subscriptions)


class BemWithStreamedResponse:
    _client: Bem

    def __init__(self, client: Bem) -> None:
        self._client = client

    @cached_property
    def functions(self) -> functions.FunctionsResourceWithStreamingResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        from .resources.functions import FunctionsResourceWithStreamingResponse

        return FunctionsResourceWithStreamingResponse(self._client.functions)

    @cached_property
    def calls(self) -> calls.CallsResourceWithStreamingResponse:
        """
        The Calls API provides a unified interface for invoking both **Workflows** and **Functions**.

        Use this API when you want to:
        - Execute a complete workflow that chains multiple functions together
        - Call a single function directly without defining a workflow
        - Submit batch requests with multiple inputs in a single API call
        - Track execution status using call reference IDs

        **Key Difference**: Calls vs Function Calls
        - **Calls API** (`/v3/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v3/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
        """
        from .resources.calls import CallsResourceWithStreamingResponse

        return CallsResourceWithStreamingResponse(self._client.calls)

    @cached_property
    def errors(self) -> errors.ErrorsResourceWithStreamingResponse:
        """Retrieve terminal error events from workflow calls.

        Errors are events produced by function steps that failed during processing. A single workflow
        call may produce multiple error events if several steps fail independently.

        Errors and outputs from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/errors` to list errors across calls, or `GET /v3/errors/{eventID}` to retrieve
        a specific error. To get errors scoped to a single call, filter by `callIDs`.
        """
        from .resources.errors import ErrorsResourceWithStreamingResponse

        return ErrorsResourceWithStreamingResponse(self._client.errors)

    @cached_property
    def outputs(self) -> outputs.OutputsResourceWithStreamingResponse:
        """Retrieve terminal non-error output events from workflow calls.

        Outputs are events produced by successful terminal function steps — steps that completed
        without errors and did not spawn further downstream function calls. A single workflow call
        may produce multiple outputs (e.g. from a split-then-transform pipeline).

        Outputs and errors from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/outputs` to list outputs across calls, or `GET /v3/outputs/{eventID}` to
        retrieve a specific output. To get outputs scoped to a single call, filter by `callIDs`.
        """
        from .resources.outputs import OutputsResourceWithStreamingResponse

        return OutputsResourceWithStreamingResponse(self._client.outputs)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithStreamingResponse:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        from .resources.workflows import WorkflowsResourceWithStreamingResponse

        return WorkflowsResourceWithStreamingResponse(self._client.workflows)

    @cached_property
    def infer_schema(self) -> infer_schema.InferSchemaResourceWithStreamingResponse:
        """Infer JSON Schemas from uploaded documents using AI.

        Upload a file (PDF, image, spreadsheet, email, etc.) and receive a general-purpose JSON Schema
        that captures the document's structure. The inferred schema can be used directly as the
        `outputSchema` when creating Extract functions.

        The schema is designed to be broadly applicable to documents of the same type, not just
        the specific file uploaded.
        """
        from .resources.infer_schema import InferSchemaResourceWithStreamingResponse

        return InferSchemaResourceWithStreamingResponse(self._client.infer_schema)

    @cached_property
    def collections(self) -> collections.CollectionsResourceWithStreamingResponse:
        """
        Collections are named groups of embedded items used by Enrich functions for semantic search.

        Each collection is referenced by a `collectionName`, which supports dot notation for
        hierarchical paths (e.g. `customers.premium.vip`). Names must contain only letters,
        digits, underscores, and dots, and each segment must start with a letter or underscore.

        ## Items

        Items carry either a string or a JSON object in their `data` field. When items are added
        or updated, their `data` is embedded asynchronously — `POST /v3/collections/items` and
        `PUT /v3/collections/items` return immediately with a `pending` status and an `eventID`
        that can be correlated with webhook notifications once processing completes.

        ## Listing and hierarchy

        Use `GET /v3/collections` with `parentCollectionName` to list collections under a path,
        or `collectionNameSearch` for a case-insensitive substring match. `GET /v3/collections/items`
        retrieves a specific collection's items; pass `includeSubcollections=true` to fold in items
        from all descendant collections.

        ## Token counting

        Use `POST /v3/collections/token-count` to check whether texts fit within the embedding
        model's 8,192-token-per-text limit before submitting them for embedding.
        """
        from .resources.collections import CollectionsResourceWithStreamingResponse

        return CollectionsResourceWithStreamingResponse(self._client.collections)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        """Submit training corrections for `extract`, `classify`, and `join` events.

        Feedback is event-centric — each correction is attached to an event by its `eventID`,
        and the server resolves the correct underlying storage (extract/join transformations
        or classify route events) from the event's function type.

        Split and enrich function types do not support feedback.
        """
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def webhook_secret(self) -> webhook_secret.WebhookSecretResourceWithStreamingResponse:
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
        from .resources.webhook_secret import WebhookSecretResourceWithStreamingResponse

        return WebhookSecretResourceWithStreamingResponse(self._client.webhook_secret)

    @cached_property
    def eval(self) -> eval.EvalResourceWithStreamingResponse:
        """
        Monitor, evaluate, and iterate on the quality of every function in your
        environment. Function Accuracy bundles two complementary loops:

        ## Evaluations (`/v3/eval`)

        Trigger and retrieve per-transformation evaluations. Evaluations run
        asynchronously and score each transformation's output against the
        function's schema for confidence, per-field hallucination detection,
        and relevance. Supported for `extract`, `transform`, `analyze`, and
        `join` events.

        1. **Trigger** — `POST /v3/eval` queues jobs for a batch of transformation IDs.
        2. **Poll** — `GET /v3/eval/results` returns the current state of each
           requested ID, partitioned into `results`, `pending`, and `failed`.
           Accepts either `eventIDs` (preferred) or `transformationIDs` as a
           comma-separated query parameter, and always keys the response by
           event KSUID.

        Up to 100 IDs may be submitted per request.

        ## Metrics, review, regression (`/v3/functions/{metrics,review,regression,compare}`)

        Roll evaluation results and user corrections up into actionable
        function-level signal:

        - **`GET /v3/functions/metrics`** — aggregate accuracy, precision,
          recall, F1, and confusion-matrix counts per function.
        - **`POST /v3/functions/review`** — sample-size estimation,
          confidence-bucketed distribution, PR-AUC, and per-threshold
          confidence intervals (Wald or Wilson) for picking review cutoffs.
        - **`POST /v3/functions/regression`** — replay corrected historical
          inputs against a new function version, producing a labeled
          regression dataset.
        - **`POST /v3/functions/regression/corrections`** — propagate
          baseline corrections onto the regression dataset so it can be
          scored.
        - **`POST /v3/functions/compare`** — compute aggregate and
          field-level lift between any two versions, optionally scoped to
          the regression dataset.

        All five endpoints support `extract` end-to-end on both the vision
        and OCR paths, alongside the legacy `transform` / `analyze` / `join`
        types.
        """
        from .resources.eval import EvalResourceWithStreamingResponse

        return EvalResourceWithStreamingResponse(self._client.eval)

    @cached_property
    def fs(self) -> fs.FsResourceWithStreamingResponse:
        """Unix-shell-style nav over parsed documents and the cross-doc memory store.

        `POST /v3/fs` is a single op-driven endpoint designed for LLM agents
        and programmatic consumers that want to walk a corpus the way they'd
        walk a filesystem.

        ## Doc-level ops (every parsed document)

        - `ls` — list parsed documents with rich per-doc metadata.
        - `cat` — read one doc's parse JSON, sliced (`range`) or projected (`select`).
        - `head` — first N sections of one doc.
        - `grep` — substring or regex search; `scope`, `path`, `countOnly` available.
        - `stat` — metadata only (page/section/entity counts, timestamps).

        ## Memory-level ops (require `linkAcrossDocuments: true` on the parse function)

        - `find` — list canonical entities across the corpus.
        - `open` — entity + mentions.
        - `xref` — for one entity, sections across docs that mention it (with content).

        Memory ops return an empty list with a `hint` when no docs in this
        environment have been memory-linked.

        ## Pagination

        List ops paginate by cursor — pass the previous response's `nextCursor`
        back as `cursor`; `hasMore: false` signals the last page. Same idiom as
        `/v3/calls` and `/v3/outputs`.
        """
        from .resources.fs import FsResourceWithStreamingResponse

        return FsResourceWithStreamingResponse(self._client.fs)

    @cached_property
    def connectors(self) -> connectors.ConnectorsResourceWithStreamingResponse:
        """Connectors are integrations that trigger a Bem workflow from an external system.

        A connector binds an inbound source — currently Box or a Paragon-managed integration such as
        Google Drive — to a specific workflow (by `workflowName` or `workflowID`). When the source
        observes a new file, Bem invokes the bound workflow against that file.

        Use these endpoints to create, list, and remove connectors. The fields used at create time
        depend on the connector `type`: Box connectors require Box credentials and a folder to watch,
        while Paragon connectors carry a `paragonIntegration` identifier and an integration-specific
        `paragonConfiguration` object (for example, `{ "folderId": "..." }` for Google Drive).
        """
        from .resources.connectors import ConnectorsResourceWithStreamingResponse

        return ConnectorsResourceWithStreamingResponse(self._client.connectors)

    @cached_property
    def subscriptions(self) -> subscriptions.SubscriptionsResourceWithStreamingResponse:
        """
        Subscriptions wire up notifications for the events your functions and collections produce.

        Each subscription targets a single function (by `functionName` or `functionID`) or a single
        collection (by `collectionName` or `collectionID`) and selects a `type` corresponding to the
        event you want to receive — for example `transform`, `route`, `join`, `evaluation`, `error`,
        `enrich`, or `collection_processing`.

        Deliveries can be sent to any combination of:

        - `webhookURL` — HTTPS endpoint that receives a JSON POST per event.
        - `s3Bucket` + `s3FilePath` — sync output JSON into an AWS S3 prefix you own.
        - `googleDriveFolderID` — drop output JSON into a Google Drive folder.

        Use `disabled: true` to pause delivery without deleting the subscription. Updates follow
        conventional PATCH semantics — only the fields you include are changed.
        """
        from .resources.subscriptions import SubscriptionsResourceWithStreamingResponse

        return SubscriptionsResourceWithStreamingResponse(self._client.subscriptions)


class AsyncBemWithStreamedResponse:
    _client: AsyncBem

    def __init__(self, client: AsyncBem) -> None:
        self._client = client

    @cached_property
    def functions(self) -> functions.AsyncFunctionsResourceWithStreamingResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Extract**: Extract structured JSON data from unstructured documents (PDFs, emails, images, spreadsheets), with optional layout-aware bounding-box extraction
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Parse**: Render documents into a navigable structure of page-aware sections, named entities, and relationships — designed to be walked by an LLM agent via the [File System API](/api/v3/file-system) (`POST /v3/fs`). Two toggles, both `true` by default: `extractEntities` controls per-document entity and relationship extraction; `linkAcrossDocuments` merges entities into one canonical record per real-world thing across the environment, populating cross-document memory.
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections
        - **Send**: Deliver workflow outputs to downstream destinations

        Use these endpoints to create, update, list, and manage your functions.
        """
        from .resources.functions import AsyncFunctionsResourceWithStreamingResponse

        return AsyncFunctionsResourceWithStreamingResponse(self._client.functions)

    @cached_property
    def calls(self) -> calls.AsyncCallsResourceWithStreamingResponse:
        """
        The Calls API provides a unified interface for invoking both **Workflows** and **Functions**.

        Use this API when you want to:
        - Execute a complete workflow that chains multiple functions together
        - Call a single function directly without defining a workflow
        - Submit batch requests with multiple inputs in a single API call
        - Track execution status using call reference IDs

        **Key Difference**: Calls vs Function Calls
        - **Calls API** (`/v3/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v3/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
        """
        from .resources.calls import AsyncCallsResourceWithStreamingResponse

        return AsyncCallsResourceWithStreamingResponse(self._client.calls)

    @cached_property
    def errors(self) -> errors.AsyncErrorsResourceWithStreamingResponse:
        """Retrieve terminal error events from workflow calls.

        Errors are events produced by function steps that failed during processing. A single workflow
        call may produce multiple error events if several steps fail independently.

        Errors and outputs from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/errors` to list errors across calls, or `GET /v3/errors/{eventID}` to retrieve
        a specific error. To get errors scoped to a single call, filter by `callIDs`.
        """
        from .resources.errors import AsyncErrorsResourceWithStreamingResponse

        return AsyncErrorsResourceWithStreamingResponse(self._client.errors)

    @cached_property
    def outputs(self) -> outputs.AsyncOutputsResourceWithStreamingResponse:
        """Retrieve terminal non-error output events from workflow calls.

        Outputs are events produced by successful terminal function steps — steps that completed
        without errors and did not spawn further downstream function calls. A single workflow call
        may produce multiple outputs (e.g. from a split-then-transform pipeline).

        Outputs and errors from the same call are not mutually exclusive: a partially-completed
        workflow may have both.

        Use `GET /v3/outputs` to list outputs across calls, or `GET /v3/outputs/{eventID}` to
        retrieve a specific output. To get outputs scoped to a single call, filter by `callIDs`.
        """
        from .resources.outputs import AsyncOutputsResourceWithStreamingResponse

        return AsyncOutputsResourceWithStreamingResponse(self._client.outputs)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithStreamingResponse:
        """
        Workflows orchestrate one or more functions into a directed acyclic graph (DAG) for document processing.

        Use these endpoints to create, update, list, and manage workflows, and to invoke them
        with file input via `POST /v3/workflows/{workflowName}/call`.

        The call endpoint accepts files as either multipart form data or JSON with base64-encoded
        content. In the Bem CLI, use `@path/to/file` inside JSON values to automatically read and
        encode files:

        ```
        bem workflows call --workflow-name my-workflow \\
          --input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' \\
          --wait
        ```
        """
        from .resources.workflows import AsyncWorkflowsResourceWithStreamingResponse

        return AsyncWorkflowsResourceWithStreamingResponse(self._client.workflows)

    @cached_property
    def infer_schema(self) -> infer_schema.AsyncInferSchemaResourceWithStreamingResponse:
        """Infer JSON Schemas from uploaded documents using AI.

        Upload a file (PDF, image, spreadsheet, email, etc.) and receive a general-purpose JSON Schema
        that captures the document's structure. The inferred schema can be used directly as the
        `outputSchema` when creating Extract functions.

        The schema is designed to be broadly applicable to documents of the same type, not just
        the specific file uploaded.
        """
        from .resources.infer_schema import AsyncInferSchemaResourceWithStreamingResponse

        return AsyncInferSchemaResourceWithStreamingResponse(self._client.infer_schema)

    @cached_property
    def collections(self) -> collections.AsyncCollectionsResourceWithStreamingResponse:
        """
        Collections are named groups of embedded items used by Enrich functions for semantic search.

        Each collection is referenced by a `collectionName`, which supports dot notation for
        hierarchical paths (e.g. `customers.premium.vip`). Names must contain only letters,
        digits, underscores, and dots, and each segment must start with a letter or underscore.

        ## Items

        Items carry either a string or a JSON object in their `data` field. When items are added
        or updated, their `data` is embedded asynchronously — `POST /v3/collections/items` and
        `PUT /v3/collections/items` return immediately with a `pending` status and an `eventID`
        that can be correlated with webhook notifications once processing completes.

        ## Listing and hierarchy

        Use `GET /v3/collections` with `parentCollectionName` to list collections under a path,
        or `collectionNameSearch` for a case-insensitive substring match. `GET /v3/collections/items`
        retrieves a specific collection's items; pass `includeSubcollections=true` to fold in items
        from all descendant collections.

        ## Token counting

        Use `POST /v3/collections/token-count` to check whether texts fit within the embedding
        model's 8,192-token-per-text limit before submitting them for embedding.
        """
        from .resources.collections import AsyncCollectionsResourceWithStreamingResponse

        return AsyncCollectionsResourceWithStreamingResponse(self._client.collections)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        """Submit training corrections for `extract`, `classify`, and `join` events.

        Feedback is event-centric — each correction is attached to an event by its `eventID`,
        and the server resolves the correct underlying storage (extract/join transformations
        or classify route events) from the event's function type.

        Split and enrich function types do not support feedback.
        """
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def webhook_secret(self) -> webhook_secret.AsyncWebhookSecretResourceWithStreamingResponse:
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
        from .resources.webhook_secret import AsyncWebhookSecretResourceWithStreamingResponse

        return AsyncWebhookSecretResourceWithStreamingResponse(self._client.webhook_secret)

    @cached_property
    def eval(self) -> eval.AsyncEvalResourceWithStreamingResponse:
        """
        Monitor, evaluate, and iterate on the quality of every function in your
        environment. Function Accuracy bundles two complementary loops:

        ## Evaluations (`/v3/eval`)

        Trigger and retrieve per-transformation evaluations. Evaluations run
        asynchronously and score each transformation's output against the
        function's schema for confidence, per-field hallucination detection,
        and relevance. Supported for `extract`, `transform`, `analyze`, and
        `join` events.

        1. **Trigger** — `POST /v3/eval` queues jobs for a batch of transformation IDs.
        2. **Poll** — `GET /v3/eval/results` returns the current state of each
           requested ID, partitioned into `results`, `pending`, and `failed`.
           Accepts either `eventIDs` (preferred) or `transformationIDs` as a
           comma-separated query parameter, and always keys the response by
           event KSUID.

        Up to 100 IDs may be submitted per request.

        ## Metrics, review, regression (`/v3/functions/{metrics,review,regression,compare}`)

        Roll evaluation results and user corrections up into actionable
        function-level signal:

        - **`GET /v3/functions/metrics`** — aggregate accuracy, precision,
          recall, F1, and confusion-matrix counts per function.
        - **`POST /v3/functions/review`** — sample-size estimation,
          confidence-bucketed distribution, PR-AUC, and per-threshold
          confidence intervals (Wald or Wilson) for picking review cutoffs.
        - **`POST /v3/functions/regression`** — replay corrected historical
          inputs against a new function version, producing a labeled
          regression dataset.
        - **`POST /v3/functions/regression/corrections`** — propagate
          baseline corrections onto the regression dataset so it can be
          scored.
        - **`POST /v3/functions/compare`** — compute aggregate and
          field-level lift between any two versions, optionally scoped to
          the regression dataset.

        All five endpoints support `extract` end-to-end on both the vision
        and OCR paths, alongside the legacy `transform` / `analyze` / `join`
        types.
        """
        from .resources.eval import AsyncEvalResourceWithStreamingResponse

        return AsyncEvalResourceWithStreamingResponse(self._client.eval)

    @cached_property
    def fs(self) -> fs.AsyncFsResourceWithStreamingResponse:
        """Unix-shell-style nav over parsed documents and the cross-doc memory store.

        `POST /v3/fs` is a single op-driven endpoint designed for LLM agents
        and programmatic consumers that want to walk a corpus the way they'd
        walk a filesystem.

        ## Doc-level ops (every parsed document)

        - `ls` — list parsed documents with rich per-doc metadata.
        - `cat` — read one doc's parse JSON, sliced (`range`) or projected (`select`).
        - `head` — first N sections of one doc.
        - `grep` — substring or regex search; `scope`, `path`, `countOnly` available.
        - `stat` — metadata only (page/section/entity counts, timestamps).

        ## Memory-level ops (require `linkAcrossDocuments: true` on the parse function)

        - `find` — list canonical entities across the corpus.
        - `open` — entity + mentions.
        - `xref` — for one entity, sections across docs that mention it (with content).

        Memory ops return an empty list with a `hint` when no docs in this
        environment have been memory-linked.

        ## Pagination

        List ops paginate by cursor — pass the previous response's `nextCursor`
        back as `cursor`; `hasMore: false` signals the last page. Same idiom as
        `/v3/calls` and `/v3/outputs`.
        """
        from .resources.fs import AsyncFsResourceWithStreamingResponse

        return AsyncFsResourceWithStreamingResponse(self._client.fs)

    @cached_property
    def connectors(self) -> connectors.AsyncConnectorsResourceWithStreamingResponse:
        """Connectors are integrations that trigger a Bem workflow from an external system.

        A connector binds an inbound source — currently Box or a Paragon-managed integration such as
        Google Drive — to a specific workflow (by `workflowName` or `workflowID`). When the source
        observes a new file, Bem invokes the bound workflow against that file.

        Use these endpoints to create, list, and remove connectors. The fields used at create time
        depend on the connector `type`: Box connectors require Box credentials and a folder to watch,
        while Paragon connectors carry a `paragonIntegration` identifier and an integration-specific
        `paragonConfiguration` object (for example, `{ "folderId": "..." }` for Google Drive).
        """
        from .resources.connectors import AsyncConnectorsResourceWithStreamingResponse

        return AsyncConnectorsResourceWithStreamingResponse(self._client.connectors)

    @cached_property
    def subscriptions(self) -> subscriptions.AsyncSubscriptionsResourceWithStreamingResponse:
        """
        Subscriptions wire up notifications for the events your functions and collections produce.

        Each subscription targets a single function (by `functionName` or `functionID`) or a single
        collection (by `collectionName` or `collectionID`) and selects a `type` corresponding to the
        event you want to receive — for example `transform`, `route`, `join`, `evaluation`, `error`,
        `enrich`, or `collection_processing`.

        Deliveries can be sent to any combination of:

        - `webhookURL` — HTTPS endpoint that receives a JSON POST per event.
        - `s3Bucket` + `s3FilePath` — sync output JSON into an AWS S3 prefix you own.
        - `googleDriveFolderID` — drop output JSON into a Google Drive folder.

        Use `disabled: true` to pause delivery without deleting the subscription. Updates follow
        conventional PATCH semantics — only the fields you include are changed.
        """
        from .resources.subscriptions import AsyncSubscriptionsResourceWithStreamingResponse

        return AsyncSubscriptionsResourceWithStreamingResponse(self._client.subscriptions)


Client = Bem

AsyncClient = AsyncBem
