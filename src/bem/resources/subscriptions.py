# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import subscription_list_params, subscription_create_params, subscription_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.subscription_v3 import SubscriptionV3
from ..types.subscription_list_response import SubscriptionListResponse

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: Literal[
            "transform",
            "analyze",
            "route",
            "join",
            "split_collection",
            "split_item",
            "evaluation",
            "error",
            "payload_shaping",
            "enrich",
            "collection_processing",
        ],
        collection_id: str | Omit = omit,
        collection_name: str | Omit = omit,
        disabled: bool | Omit = omit,
        function_id: str | Omit = omit,
        function_name: str | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_file_path: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionV3:
        """
        Creates a new subscription to listen to transform or error events.

        Args:
          name: Name of subscription.

          type: Type of subscription.

          collection_id: Unique identifier of collection this subscription listens to (alternative to
              collectionName).

          collection_name: Name of collection this subscription listens to (required for collection-based
              subscriptions).

          disabled: Toggles whether subscription is active or not.

          function_id: Unique identifier of function this subscription listens to (alternative to
              functionName).

          function_name: Unique name of function this subscription listens to (required for
              function-based subscriptions).

          google_drive_folder_id: Google Drive folder ID for syncing output data to Google Drive.

          s3_bucket: S3 bucket name for syncing output data to AWS S3.

          s3_file_path: S3 file path for syncing output data to AWS S3.

          webhook_url: URL bem will send webhook requests to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/subscriptions",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "collection_id": collection_id,
                    "collection_name": collection_name,
                    "disabled": disabled,
                    "function_id": function_id,
                    "function_name": function_name,
                    "google_drive_folder_id": google_drive_folder_id,
                    "s3_bucket": s3_bucket,
                    "s3_file_path": s3_file_path,
                    "webhook_url": webhook_url,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionV3,
        )

    def retrieve(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionV3:
        """
        Get a Subscription

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._get(
            path_template("/v3/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionV3,
        )

    def update(
        self,
        subscription_id: str,
        *,
        disabled: bool | Omit = omit,
        function_name: str | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        name: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_file_path: str | Omit = omit,
        type: Literal[
            "transform",
            "analyze",
            "route",
            "join",
            "split_collection",
            "split_item",
            "evaluation",
            "error",
            "payload_shaping",
            "enrich",
            "collection_processing",
        ]
        | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionV3:
        """Updates an existing subscription.

        Follow conventional PATCH behavior, so only
        included fields will be updated.

        Args:
          disabled: Toggles whether subscription is active or not.

          function_name: Unique name of function this subscription listens to.

          google_drive_folder_id: Google Drive folder ID for syncing output data to Google Drive.

          name: Name of subscription.

          s3_bucket: S3 bucket name for syncing output data to AWS S3.

          s3_file_path: S3 file path for syncing output data to AWS S3.

          type: Type of subscription.

          webhook_url: URL bem will send webhook requests to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._patch(
            path_template("/v3/subscriptions/{subscription_id}", subscription_id=subscription_id),
            body=maybe_transform(
                {
                    "disabled": disabled,
                    "function_name": function_name,
                    "google_drive_folder_id": google_drive_folder_id,
                    "name": name,
                    "s3_bucket": s3_bucket,
                    "s3_file_path": s3_file_path,
                    "type": type,
                    "webhook_url": webhook_url,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionV3,
        )

    def list(
        self,
        *,
        ending_before: str | Omit = omit,
        function_names: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """List Subscriptions

        Args:
          ending_before: A cursor to use in pagination.

        `endingBefore` is a task ID that defines your
              place in the list. For example, if you make a list request and receive 50
              objects, starting with `sub_2c9AXIj48cUYJtCuv1gsQtHGDzK`, your subsequent call
              can include `endingBefore=sub_2c9AXIj48cUYJtCuv1gsQtHGDzK` to fetch the previous
              page of the list.

          function_names: Filters to subscriptions linked to included array of function names.

          limit: This specifies a limit on the number of objects to return, ranging between 1
              and 100.

          sort_order: Specifies sorting behavior. The two options are `asc` and `desc` to sort
              ascending and descending respectively, with default sort being ascending. Paging
              works in both directions.

          starting_after: A cursor to use in pagination. `startingAfter` is a task ID that defines your
              place in the list. For example, if you make a list request and receive 50
              objects, ending with `sub_2c9AXIj48cUYJtCuv1gsQtHGDzK`, your subsequent call can
              include `startingAfter=sub_2c9AXIj48cUYJtCuv1gsQtHGDzK` to fetch the next page
              of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "function_names": function_names,
                        "limit": limit,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            cast_to=SubscriptionListResponse,
        )

    def delete(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes an existing subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: Literal[
            "transform",
            "analyze",
            "route",
            "join",
            "split_collection",
            "split_item",
            "evaluation",
            "error",
            "payload_shaping",
            "enrich",
            "collection_processing",
        ],
        collection_id: str | Omit = omit,
        collection_name: str | Omit = omit,
        disabled: bool | Omit = omit,
        function_id: str | Omit = omit,
        function_name: str | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_file_path: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionV3:
        """
        Creates a new subscription to listen to transform or error events.

        Args:
          name: Name of subscription.

          type: Type of subscription.

          collection_id: Unique identifier of collection this subscription listens to (alternative to
              collectionName).

          collection_name: Name of collection this subscription listens to (required for collection-based
              subscriptions).

          disabled: Toggles whether subscription is active or not.

          function_id: Unique identifier of function this subscription listens to (alternative to
              functionName).

          function_name: Unique name of function this subscription listens to (required for
              function-based subscriptions).

          google_drive_folder_id: Google Drive folder ID for syncing output data to Google Drive.

          s3_bucket: S3 bucket name for syncing output data to AWS S3.

          s3_file_path: S3 file path for syncing output data to AWS S3.

          webhook_url: URL bem will send webhook requests to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/subscriptions",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "collection_id": collection_id,
                    "collection_name": collection_name,
                    "disabled": disabled,
                    "function_id": function_id,
                    "function_name": function_name,
                    "google_drive_folder_id": google_drive_folder_id,
                    "s3_bucket": s3_bucket,
                    "s3_file_path": s3_file_path,
                    "webhook_url": webhook_url,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionV3,
        )

    async def retrieve(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionV3:
        """
        Get a Subscription

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._get(
            path_template("/v3/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionV3,
        )

    async def update(
        self,
        subscription_id: str,
        *,
        disabled: bool | Omit = omit,
        function_name: str | Omit = omit,
        google_drive_folder_id: str | Omit = omit,
        name: str | Omit = omit,
        s3_bucket: str | Omit = omit,
        s3_file_path: str | Omit = omit,
        type: Literal[
            "transform",
            "analyze",
            "route",
            "join",
            "split_collection",
            "split_item",
            "evaluation",
            "error",
            "payload_shaping",
            "enrich",
            "collection_processing",
        ]
        | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionV3:
        """Updates an existing subscription.

        Follow conventional PATCH behavior, so only
        included fields will be updated.

        Args:
          disabled: Toggles whether subscription is active or not.

          function_name: Unique name of function this subscription listens to.

          google_drive_folder_id: Google Drive folder ID for syncing output data to Google Drive.

          name: Name of subscription.

          s3_bucket: S3 bucket name for syncing output data to AWS S3.

          s3_file_path: S3 file path for syncing output data to AWS S3.

          type: Type of subscription.

          webhook_url: URL bem will send webhook requests to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._patch(
            path_template("/v3/subscriptions/{subscription_id}", subscription_id=subscription_id),
            body=await async_maybe_transform(
                {
                    "disabled": disabled,
                    "function_name": function_name,
                    "google_drive_folder_id": google_drive_folder_id,
                    "name": name,
                    "s3_bucket": s3_bucket,
                    "s3_file_path": s3_file_path,
                    "type": type,
                    "webhook_url": webhook_url,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionV3,
        )

    async def list(
        self,
        *,
        ending_before: str | Omit = omit,
        function_names: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """List Subscriptions

        Args:
          ending_before: A cursor to use in pagination.

        `endingBefore` is a task ID that defines your
              place in the list. For example, if you make a list request and receive 50
              objects, starting with `sub_2c9AXIj48cUYJtCuv1gsQtHGDzK`, your subsequent call
              can include `endingBefore=sub_2c9AXIj48cUYJtCuv1gsQtHGDzK` to fetch the previous
              page of the list.

          function_names: Filters to subscriptions linked to included array of function names.

          limit: This specifies a limit on the number of objects to return, ranging between 1
              and 100.

          sort_order: Specifies sorting behavior. The two options are `asc` and `desc` to sort
              ascending and descending respectively, with default sort being ascending. Paging
              works in both directions.

          starting_after: A cursor to use in pagination. `startingAfter` is a task ID that defines your
              place in the list. For example, if you make a list request and receive 50
              objects, ending with `sub_2c9AXIj48cUYJtCuv1gsQtHGDzK`, your subsequent call can
              include `startingAfter=sub_2c9AXIj48cUYJtCuv1gsQtHGDzK` to fetch the next page
              of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ending_before": ending_before,
                        "function_names": function_names,
                        "limit": limit,
                        "sort_order": sort_order,
                        "starting_after": starting_after,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            cast_to=SubscriptionListResponse,
        )

    async def delete(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes an existing subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            subscriptions.delete,
        )


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subscriptions.delete,
        )


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            subscriptions.delete,
        )


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscriptions.delete,
        )
