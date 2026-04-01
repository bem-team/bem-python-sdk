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
from ._utils import is_given, get_async_library
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
    from .resources import calls, errors, outputs, functions, workflows
    from .resources.calls import CallsResource, AsyncCallsResource
    from .resources.errors import ErrorsResource, AsyncErrorsResource
    from .resources.outputs import OutputsResource, AsyncOutputsResource
    from .resources.functions.functions import FunctionsResource, AsyncFunctionsResource
    from .resources.workflows.workflows import WorkflowsResource, AsyncWorkflowsResource

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

        - **Transform**: Extract structured JSON data from unstructured documents (PDFs, emails, images)
        - **Analyze**: Perform visual analysis on documents to extract layout-aware information
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections

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
        - **Calls API** (`/v2/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v2/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
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
        """Workflow operations"""
        from .resources.workflows import WorkflowsResource

        return WorkflowsResource(self)

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

        - **Transform**: Extract structured JSON data from unstructured documents (PDFs, emails, images)
        - **Analyze**: Perform visual analysis on documents to extract layout-aware information
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections

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
        - **Calls API** (`/v2/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v2/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
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
        """Workflow operations"""
        from .resources.workflows import AsyncWorkflowsResource

        return AsyncWorkflowsResource(self)

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

        - **Transform**: Extract structured JSON data from unstructured documents (PDFs, emails, images)
        - **Analyze**: Perform visual analysis on documents to extract layout-aware information
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections

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
        - **Calls API** (`/v2/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v2/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
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
        """Workflow operations"""
        from .resources.workflows import WorkflowsResourceWithRawResponse

        return WorkflowsResourceWithRawResponse(self._client.workflows)


class AsyncBemWithRawResponse:
    _client: AsyncBem

    def __init__(self, client: AsyncBem) -> None:
        self._client = client

    @cached_property
    def functions(self) -> functions.AsyncFunctionsResourceWithRawResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Transform**: Extract structured JSON data from unstructured documents (PDFs, emails, images)
        - **Analyze**: Perform visual analysis on documents to extract layout-aware information
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections

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
        - **Calls API** (`/v2/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v2/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
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
        """Workflow operations"""
        from .resources.workflows import AsyncWorkflowsResourceWithRawResponse

        return AsyncWorkflowsResourceWithRawResponse(self._client.workflows)


class BemWithStreamedResponse:
    _client: Bem

    def __init__(self, client: Bem) -> None:
        self._client = client

    @cached_property
    def functions(self) -> functions.FunctionsResourceWithStreamingResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Transform**: Extract structured JSON data from unstructured documents (PDFs, emails, images)
        - **Analyze**: Perform visual analysis on documents to extract layout-aware information
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections

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
        - **Calls API** (`/v2/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v2/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
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
        """Workflow operations"""
        from .resources.workflows import WorkflowsResourceWithStreamingResponse

        return WorkflowsResourceWithStreamingResponse(self._client.workflows)


class AsyncBemWithStreamedResponse:
    _client: AsyncBem

    def __init__(self, client: AsyncBem) -> None:
        self._client = client

    @cached_property
    def functions(self) -> functions.AsyncFunctionsResourceWithStreamingResponse:
        """Functions are the core building blocks of data transformation in Bem.

        Each function type serves a specific purpose:

        - **Transform**: Extract structured JSON data from unstructured documents (PDFs, emails, images)
        - **Analyze**: Perform visual analysis on documents to extract layout-aware information
        - **Route**: Direct data to different processing paths based on conditions
        - **Split**: Break multi-page documents into individual pages for parallel processing
        - **Join**: Combine outputs from multiple function calls into a single result
        - **Payload Shaping**: Transform and restructure data using JMESPath expressions
        - **Enrich**: Enhance data with semantic search against collections

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
        - **Calls API** (`/v2/calls`): High-level API for invoking workflows or functions by name/ID. Supports batch processing and workflow orchestration.
        - **Function Calls API** (`/v2/functions/{functionName}/call`): Direct function invocation with function-type-specific arguments. Better for granular control over individual function calls.
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
        """Workflow operations"""
        from .resources.workflows import AsyncWorkflowsResourceWithStreamingResponse

        return AsyncWorkflowsResourceWithStreamingResponse(self._client.workflows)


Client = Bem

AsyncClient = AsyncBem
