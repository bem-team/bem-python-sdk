# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ConnectorType, connector_list_params, connector_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.connector import Connector
from ..types.connector_type import ConnectorType
from ..types.connector_list_response import ConnectorListResponse

__all__ = ["ConnectorsResource", "AsyncConnectorsResource"]


class ConnectorsResource(SyncAPIResource):
    """Connectors are integrations that trigger a Bem workflow from an external system.

    A connector binds an inbound source — currently Box or a Paragon-managed integration such as
    Google Drive — to a specific workflow (by `workflowName` or `workflowID`). When the source
    observes a new file, Bem invokes the bound workflow against that file.

    Use these endpoints to create, list, and remove connectors. The fields used at create time
    depend on the connector `type`: Box connectors require Box credentials and a folder to watch,
    while Paragon connectors carry a `paragonIntegration` identifier and an integration-specific
    `paragonConfiguration` object (for example, `{ "folderId": "..." }` for Google Drive).
    """

    @cached_property
    def with_raw_response(self) -> ConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return ConnectorsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: ConnectorType,
        box_client_id: str | Omit = omit,
        box_client_secret: str | Omit = omit,
        box_enterprise_id: str | Omit = omit,
        box_folder_id: str | Omit = omit,
        paragon_configuration: object | Omit = omit,
        paragon_integration: str | Omit = omit,
        workflow_id: str | Omit = omit,
        workflow_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connector:
        """
        Create a Connector

        Args:
          name: Human-friendly name for this connector.

          type: Connector type.

          box_client_id: Box client ID (from your Box application).

          box_client_secret: Box client secret (from your Box application).

          box_enterprise_id: Box enterprise ID.

          box_folder_id: Box folder ID to watch for new uploads.

          paragon_configuration: Configuration specific to the type of integration.

          paragon_integration: Paragon integration, eg. "googledrive".

          workflow_id: One of `workflowID` or `workflowName` must be provided.

              If both are provided, they must refer to the same workflow.

          workflow_name: One of `workflowID` or `workflowName` must be provided.

              If both are provided, they must refer to the same workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/connectors",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "box_client_id": box_client_id,
                    "box_client_secret": box_client_secret,
                    "box_enterprise_id": box_enterprise_id,
                    "box_folder_id": box_folder_id,
                    "paragon_configuration": paragon_configuration,
                    "paragon_integration": paragon_integration,
                    "workflow_id": workflow_id,
                    "workflow_name": workflow_name,
                },
                connector_create_params.ConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connector,
        )

    def list(
        self,
        *,
        workflow_id: str | Omit = omit,
        workflow_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListResponse:
        """List Connectors

        Args:
          workflow_id: Filter connectors by workflow API ID (e.g.

        `wf_...`).

              If both `workflowID` and `workflowName` are provided, results must match both.

          workflow_name: Filter connectors by workflow name (exact match).

              If both `workflowID` and `workflowName` are provided, results must match both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/connectors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "workflow_id": workflow_id,
                        "workflow_name": workflow_name,
                    },
                    connector_list_params.ConnectorListParams,
                ),
            ),
            cast_to=ConnectorListResponse,
        )

    def delete(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Delete a Connector

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/connectors/{connector_id}", connector_id=connector_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncConnectorsResource(AsyncAPIResource):
    """Connectors are integrations that trigger a Bem workflow from an external system.

    A connector binds an inbound source — currently Box or a Paragon-managed integration such as
    Google Drive — to a specific workflow (by `workflowName` or `workflowID`). When the source
    observes a new file, Bem invokes the bound workflow against that file.

    Use these endpoints to create, list, and remove connectors. The fields used at create time
    depend on the connector `type`: Box connectors require Box credentials and a folder to watch,
    while Paragon connectors carry a `paragonIntegration` identifier and an integration-specific
    `paragonConfiguration` object (for example, `{ "folderId": "..." }` for Google Drive).
    """

    @cached_property
    def with_raw_response(self) -> AsyncConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncConnectorsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: ConnectorType,
        box_client_id: str | Omit = omit,
        box_client_secret: str | Omit = omit,
        box_enterprise_id: str | Omit = omit,
        box_folder_id: str | Omit = omit,
        paragon_configuration: object | Omit = omit,
        paragon_integration: str | Omit = omit,
        workflow_id: str | Omit = omit,
        workflow_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Connector:
        """
        Create a Connector

        Args:
          name: Human-friendly name for this connector.

          type: Connector type.

          box_client_id: Box client ID (from your Box application).

          box_client_secret: Box client secret (from your Box application).

          box_enterprise_id: Box enterprise ID.

          box_folder_id: Box folder ID to watch for new uploads.

          paragon_configuration: Configuration specific to the type of integration.

          paragon_integration: Paragon integration, eg. "googledrive".

          workflow_id: One of `workflowID` or `workflowName` must be provided.

              If both are provided, they must refer to the same workflow.

          workflow_name: One of `workflowID` or `workflowName` must be provided.

              If both are provided, they must refer to the same workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/connectors",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "box_client_id": box_client_id,
                    "box_client_secret": box_client_secret,
                    "box_enterprise_id": box_enterprise_id,
                    "box_folder_id": box_folder_id,
                    "paragon_configuration": paragon_configuration,
                    "paragon_integration": paragon_integration,
                    "workflow_id": workflow_id,
                    "workflow_name": workflow_name,
                },
                connector_create_params.ConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connector,
        )

    async def list(
        self,
        *,
        workflow_id: str | Omit = omit,
        workflow_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorListResponse:
        """List Connectors

        Args:
          workflow_id: Filter connectors by workflow API ID (e.g.

        `wf_...`).

              If both `workflowID` and `workflowName` are provided, results must match both.

          workflow_name: Filter connectors by workflow name (exact match).

              If both `workflowID` and `workflowName` are provided, results must match both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/connectors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "workflow_id": workflow_id,
                        "workflow_name": workflow_name,
                    },
                    connector_list_params.ConnectorListParams,
                ),
            ),
            cast_to=ConnectorListResponse,
        )

    async def delete(
        self,
        connector_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Delete a Connector

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/connectors/{connector_id}", connector_id=connector_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ConnectorsResourceWithRawResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.create = to_raw_response_wrapper(
            connectors.create,
        )
        self.list = to_raw_response_wrapper(
            connectors.list,
        )
        self.delete = to_raw_response_wrapper(
            connectors.delete,
        )


class AsyncConnectorsResourceWithRawResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.create = async_to_raw_response_wrapper(
            connectors.create,
        )
        self.list = async_to_raw_response_wrapper(
            connectors.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connectors.delete,
        )


class ConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.create = to_streamed_response_wrapper(
            connectors.create,
        )
        self.list = to_streamed_response_wrapper(
            connectors.list,
        )
        self.delete = to_streamed_response_wrapper(
            connectors.delete,
        )


class AsyncConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.create = async_to_streamed_response_wrapper(
            connectors.create,
        )
        self.list = async_to_streamed_response_wrapper(
            connectors.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connectors.delete,
        )
