# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import infer_schema_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.infer_schema_create_response import InferSchemaCreateResponse

__all__ = ["InferSchemaResource", "AsyncInferSchemaResource"]


class InferSchemaResource(SyncAPIResource):
    """Infer JSON Schemas from uploaded documents using AI.

    Upload a file (PDF, image, spreadsheet, email, etc.) and receive a general-purpose JSON Schema
    that captures the document's structure. The inferred schema can be used directly as the
    `outputSchema` when creating Extract functions.

    The schema is designed to be broadly applicable to documents of the same type, not just
    the specific file uploaded.
    """

    @cached_property
    def with_raw_response(self) -> InferSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return InferSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InferSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return InferSchemaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferSchemaCreateResponse:
        """
        **Analyze a file and infer a JSON Schema from its contents.**

        Accepts a file via multipart form upload and uses Gemini to analyze the
        document, returning a description of its contents, an inferred JSON Schema
        capturing all extractable fields, and document classification metadata.

        The returned schema is designed to be reusable across many similar documents of
        the same type, not just the specific file uploaded. It can be used directly as
        the `outputSchema` when creating a Transform function.

        The endpoint also detects whether the file contains multiple bundled documents
        and classifies the content nature (textual, visual, audio, video, or mixed).

        ## Supported file types

        PDF, PNG, JPEG, HEIC, HEIF, WebP, CSV, XLS, XLSX, DOCX, JSON, HTML, XML, EML,
        plain text, WAV, MP3, M4A, MP4.

        ## File size limit

        Maximum file size is **20 MB**.

        ## Examples

        Using curl:

        ```bash
        curl -X POST https://api.bem.ai/v3/infer-schema \\
          -H "x-api-key: YOUR_API_KEY" \\
          -F "file=@invoice.pdf"
        ```

        Using the Bem CLI:

        ```bash
        bem infer-schema create --file @invoice.pdf
        ```

        Args:
          file: The file to analyze and infer a JSON schema from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v3/infer-schema",
            body=maybe_transform({"file": file}, infer_schema_create_params.InferSchemaCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferSchemaCreateResponse,
        )


class AsyncInferSchemaResource(AsyncAPIResource):
    """Infer JSON Schemas from uploaded documents using AI.

    Upload a file (PDF, image, spreadsheet, email, etc.) and receive a general-purpose JSON Schema
    that captures the document's structure. The inferred schema can be used directly as the
    `outputSchema` when creating Extract functions.

    The schema is designed to be broadly applicable to documents of the same type, not just
    the specific file uploaded.
    """

    @cached_property
    def with_raw_response(self) -> AsyncInferSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncInferSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInferSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncInferSchemaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferSchemaCreateResponse:
        """
        **Analyze a file and infer a JSON Schema from its contents.**

        Accepts a file via multipart form upload and uses Gemini to analyze the
        document, returning a description of its contents, an inferred JSON Schema
        capturing all extractable fields, and document classification metadata.

        The returned schema is designed to be reusable across many similar documents of
        the same type, not just the specific file uploaded. It can be used directly as
        the `outputSchema` when creating a Transform function.

        The endpoint also detects whether the file contains multiple bundled documents
        and classifies the content nature (textual, visual, audio, video, or mixed).

        ## Supported file types

        PDF, PNG, JPEG, HEIC, HEIF, WebP, CSV, XLS, XLSX, DOCX, JSON, HTML, XML, EML,
        plain text, WAV, MP3, M4A, MP4.

        ## File size limit

        Maximum file size is **20 MB**.

        ## Examples

        Using curl:

        ```bash
        curl -X POST https://api.bem.ai/v3/infer-schema \\
          -H "x-api-key: YOUR_API_KEY" \\
          -F "file=@invoice.pdf"
        ```

        Using the Bem CLI:

        ```bash
        bem infer-schema create --file @invoice.pdf
        ```

        Args:
          file: The file to analyze and infer a JSON schema from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v3/infer-schema",
            body=await async_maybe_transform({"file": file}, infer_schema_create_params.InferSchemaCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferSchemaCreateResponse,
        )


class InferSchemaResourceWithRawResponse:
    def __init__(self, infer_schema: InferSchemaResource) -> None:
        self._infer_schema = infer_schema

        self.create = to_raw_response_wrapper(
            infer_schema.create,
        )


class AsyncInferSchemaResourceWithRawResponse:
    def __init__(self, infer_schema: AsyncInferSchemaResource) -> None:
        self._infer_schema = infer_schema

        self.create = async_to_raw_response_wrapper(
            infer_schema.create,
        )


class InferSchemaResourceWithStreamingResponse:
    def __init__(self, infer_schema: InferSchemaResource) -> None:
        self._infer_schema = infer_schema

        self.create = to_streamed_response_wrapper(
            infer_schema.create,
        )


class AsyncInferSchemaResourceWithStreamingResponse:
    def __init__(self, infer_schema: AsyncInferSchemaResource) -> None:
        self._infer_schema = infer_schema

        self.create = async_to_streamed_response_wrapper(
            infer_schema.create,
        )
