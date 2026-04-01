# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.functions import copy_create_params
from ...types.function_response import FunctionResponse

__all__ = ["CopyResource", "AsyncCopyResource"]


class CopyResource(SyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> CopyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bem-python#accessing-raw-response-data-eg-headers
        """
        return CopyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CopyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bem-python#with_streaming_response
        """
        return CopyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        source_function_name: str,
        target_function_name: str,
        tags: SequenceNotStr[str] | Omit = omit,
        target_display_name: str | Omit = omit,
        target_environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """Copy a Function

        Args:
          source_function_name: Name of the function to copy from.

        Must be a valid existing function name.

          target_function_name: Name for the new copied function. Must be unique within the target environment.

          tags: Optional array of tags for the copied function. If not provided, defaults to the
              source function's tags.

          target_display_name: Optional display name for the copied function. If not provided, defaults to the
              source function's display name with " (Copy)" appended.

          target_environment: Optional environment name to copy the function to. If not provided, the function
              will be copied within the same environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/functions/copy",
            body=maybe_transform(
                {
                    "source_function_name": source_function_name,
                    "target_function_name": target_function_name,
                    "tags": tags,
                    "target_display_name": target_display_name,
                    "target_environment": target_environment,
                },
                copy_create_params.CopyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionResponse,
        )


class AsyncCopyResource(AsyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> AsyncCopyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bem-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCopyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCopyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bem-python#with_streaming_response
        """
        return AsyncCopyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        source_function_name: str,
        target_function_name: str,
        tags: SequenceNotStr[str] | Omit = omit,
        target_display_name: str | Omit = omit,
        target_environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionResponse:
        """Copy a Function

        Args:
          source_function_name: Name of the function to copy from.

        Must be a valid existing function name.

          target_function_name: Name for the new copied function. Must be unique within the target environment.

          tags: Optional array of tags for the copied function. If not provided, defaults to the
              source function's tags.

          target_display_name: Optional display name for the copied function. If not provided, defaults to the
              source function's display name with " (Copy)" appended.

          target_environment: Optional environment name to copy the function to. If not provided, the function
              will be copied within the same environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/functions/copy",
            body=await async_maybe_transform(
                {
                    "source_function_name": source_function_name,
                    "target_function_name": target_function_name,
                    "tags": tags,
                    "target_display_name": target_display_name,
                    "target_environment": target_environment,
                },
                copy_create_params.CopyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionResponse,
        )


class CopyResourceWithRawResponse:
    def __init__(self, copy: CopyResource) -> None:
        self._copy = copy

        self.create = to_raw_response_wrapper(
            copy.create,
        )


class AsyncCopyResourceWithRawResponse:
    def __init__(self, copy: AsyncCopyResource) -> None:
        self._copy = copy

        self.create = async_to_raw_response_wrapper(
            copy.create,
        )


class CopyResourceWithStreamingResponse:
    def __init__(self, copy: CopyResource) -> None:
        self._copy = copy

        self.create = to_streamed_response_wrapper(
            copy.create,
        )


class AsyncCopyResourceWithStreamingResponse:
    def __init__(self, copy: AsyncCopyResource) -> None:
        self._copy = copy

        self.create = async_to_streamed_response_wrapper(
            copy.create,
        )
