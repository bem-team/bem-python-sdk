# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.functions import regression_run_params, regression_apply_corrections_params
from ...types.functions.regression_run_response import RegressionRunResponse
from ...types.functions.regression_apply_corrections_response import RegressionApplyCorrectionsResponse

__all__ = ["RegressionResource", "AsyncRegressionResource"]


class RegressionResource(SyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> RegressionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return RegressionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegressionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return RegressionResourceWithStreamingResponse(self)

    def apply_corrections(
        self,
        *,
        baseline_version_num: int,
        comparison_version_num: int,
        function_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegressionApplyCorrectionsResponse:
        """
        **Copy baseline corrections onto regression transformations.**

        Looks up regression transformations created against the comparison version
        (`isRegression: true`, `correctedJSON IS NULL`), finds the matching baseline
        transformation by `referenceID`, and copies the baseline's `correctedJSON` onto
        the regression row via the same code path used by
        `POST /v3/events/{eventID}/feedback`. The applied corrections are immediately
        scored against the regression output, populating the confusion-matrix metrics
        used by `function-review` and `function-version-compare`.

        Works for every function type that produces correctable transformations,
        including `extract` on both the vision and OCR paths. (Previously the vision
        path silently dropped `is_regression` during the original regression run, so no
        rows matched the predicate — that has been fixed.)

        Returns counts plus the list of **event KSUIDs** whose underlying regression
        transformation received a correction. Errors (e.g. baseline transformation
        missing for a given `referenceID`) are returned per-row in the `errors` map,
        keyed by event KSUID, rather than aborting the whole call.

        Args:
          baseline_version_num: **Baseline version number (source of corrected data)**

              The function version number that contains transformations with corrected JSON
              that should be copied to regression transformations.

          comparison_version_num: **Comparison version number (target for applying corrections)**

              The function version number of regression transformations that should receive
              the corrected JSON from the baseline version.

          function_name: **Name of the function to apply corrections for**

              Must be an existing function with both baseline and regression transformation
              data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/functions/regression/corrections",
            body=maybe_transform(
                {
                    "baseline_version_num": baseline_version_num,
                    "comparison_version_num": comparison_version_num,
                    "function_name": function_name,
                },
                regression_apply_corrections_params.RegressionApplyCorrectionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegressionApplyCorrectionsResponse,
        )

    def run(
        self,
        *,
        function_name: str,
        baseline_version_num: int | Omit = omit,
        comparison_version_num: int | Omit = omit,
        only_corrected_data: bool | Omit = omit,
        sample_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegressionRunResponse:
        """
        **Kick off a regression run between two versions of a function.**

        Replays a sample of corrected historical inputs against the comparison version,
        producing fresh transformations marked `isRegression: true`. Each new run
        returns the workflow `callID`s you can monitor via `GET /v3/calls/{callID}`.

        Supported for every function type that produces correctable transformations:
        `extract`, `transform`, `analyze`, `join`. For `extract` specifically, the
        regression sample is dispatched through the same OCR vs. vision path used at
        original call time (PDF, PNG, JPEG, HEIC, HEIF, WebP go through the vision
        worker; everything else goes through OCR → transform).

        The comparison version must share a schema-compatible output shape with the
        baseline; structural differences are reported as a 400 with the offending
        field-level diffs.

        ## Typical flow

        1. `POST /v3/functions/regression` — queues calls, returns
           `{ originalReferenceID, callID }` per sample.
        2. Wait (poll `GET /v3/calls/{callID}` or subscribe to webhooks).
        3. `POST /v3/functions/regression/corrections` to copy baseline corrections onto
           the new regression transformations.
        4. `POST /v3/functions/compare` to compare baseline vs comparison metrics for
           the regression dataset.

        Args:
          function_name: **Name of the function to test for regressions**

              Must be an existing function with historical transformation data containing user
              corrections. The function must be currently active and callable.

          baseline_version_num: **Function version number to use as baseline for comparison**

              - Defaults to `currentVersionNum - 1` (previous version)
              - Must be a valid, existing version number for the function
              - Used to retrieve historical transformation data for comparison
              - Cannot be the same as `comparisonVersionNum`

          comparison_version_num: **Function version number to test against the baseline**

              - Defaults to current version number (latest version)
              - Must be a valid, existing version number for the function
              - This version will be used to create new function calls for testing
              - Cannot be the same as `baselineVersionNum`

          only_corrected_data: **Whether to only test transformations with user corrections**

              - Defaults to `true` (recommended)
              - When `true`: Only uses transformations with `correctedJSON` as ground truth
              - When `false`: May include transformations without corrections (less reliable)
              - Corrected data provides the most accurate regression testing results

          sample_size: **Number of historical samples to test**

              - Defaults to 50 samples
              - Minimum: 1, Maximum: 1000
              - Only transformations with `correctedJSON` (user corrections) are eligible
              - Actual sample size may be smaller if insufficient corrected data exists
              - Larger samples provide more statistical confidence but take longer to process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/functions/regression",
            body=maybe_transform(
                {
                    "function_name": function_name,
                    "baseline_version_num": baseline_version_num,
                    "comparison_version_num": comparison_version_num,
                    "only_corrected_data": only_corrected_data,
                    "sample_size": sample_size,
                },
                regression_run_params.RegressionRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegressionRunResponse,
        )


class AsyncRegressionResource(AsyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> AsyncRegressionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRegressionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegressionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bem-team/bem-python-sdk#with_streaming_response
        """
        return AsyncRegressionResourceWithStreamingResponse(self)

    async def apply_corrections(
        self,
        *,
        baseline_version_num: int,
        comparison_version_num: int,
        function_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegressionApplyCorrectionsResponse:
        """
        **Copy baseline corrections onto regression transformations.**

        Looks up regression transformations created against the comparison version
        (`isRegression: true`, `correctedJSON IS NULL`), finds the matching baseline
        transformation by `referenceID`, and copies the baseline's `correctedJSON` onto
        the regression row via the same code path used by
        `POST /v3/events/{eventID}/feedback`. The applied corrections are immediately
        scored against the regression output, populating the confusion-matrix metrics
        used by `function-review` and `function-version-compare`.

        Works for every function type that produces correctable transformations,
        including `extract` on both the vision and OCR paths. (Previously the vision
        path silently dropped `is_regression` during the original regression run, so no
        rows matched the predicate — that has been fixed.)

        Returns counts plus the list of **event KSUIDs** whose underlying regression
        transformation received a correction. Errors (e.g. baseline transformation
        missing for a given `referenceID`) are returned per-row in the `errors` map,
        keyed by event KSUID, rather than aborting the whole call.

        Args:
          baseline_version_num: **Baseline version number (source of corrected data)**

              The function version number that contains transformations with corrected JSON
              that should be copied to regression transformations.

          comparison_version_num: **Comparison version number (target for applying corrections)**

              The function version number of regression transformations that should receive
              the corrected JSON from the baseline version.

          function_name: **Name of the function to apply corrections for**

              Must be an existing function with both baseline and regression transformation
              data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/functions/regression/corrections",
            body=await async_maybe_transform(
                {
                    "baseline_version_num": baseline_version_num,
                    "comparison_version_num": comparison_version_num,
                    "function_name": function_name,
                },
                regression_apply_corrections_params.RegressionApplyCorrectionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegressionApplyCorrectionsResponse,
        )

    async def run(
        self,
        *,
        function_name: str,
        baseline_version_num: int | Omit = omit,
        comparison_version_num: int | Omit = omit,
        only_corrected_data: bool | Omit = omit,
        sample_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegressionRunResponse:
        """
        **Kick off a regression run between two versions of a function.**

        Replays a sample of corrected historical inputs against the comparison version,
        producing fresh transformations marked `isRegression: true`. Each new run
        returns the workflow `callID`s you can monitor via `GET /v3/calls/{callID}`.

        Supported for every function type that produces correctable transformations:
        `extract`, `transform`, `analyze`, `join`. For `extract` specifically, the
        regression sample is dispatched through the same OCR vs. vision path used at
        original call time (PDF, PNG, JPEG, HEIC, HEIF, WebP go through the vision
        worker; everything else goes through OCR → transform).

        The comparison version must share a schema-compatible output shape with the
        baseline; structural differences are reported as a 400 with the offending
        field-level diffs.

        ## Typical flow

        1. `POST /v3/functions/regression` — queues calls, returns
           `{ originalReferenceID, callID }` per sample.
        2. Wait (poll `GET /v3/calls/{callID}` or subscribe to webhooks).
        3. `POST /v3/functions/regression/corrections` to copy baseline corrections onto
           the new regression transformations.
        4. `POST /v3/functions/compare` to compare baseline vs comparison metrics for
           the regression dataset.

        Args:
          function_name: **Name of the function to test for regressions**

              Must be an existing function with historical transformation data containing user
              corrections. The function must be currently active and callable.

          baseline_version_num: **Function version number to use as baseline for comparison**

              - Defaults to `currentVersionNum - 1` (previous version)
              - Must be a valid, existing version number for the function
              - Used to retrieve historical transformation data for comparison
              - Cannot be the same as `comparisonVersionNum`

          comparison_version_num: **Function version number to test against the baseline**

              - Defaults to current version number (latest version)
              - Must be a valid, existing version number for the function
              - This version will be used to create new function calls for testing
              - Cannot be the same as `baselineVersionNum`

          only_corrected_data: **Whether to only test transformations with user corrections**

              - Defaults to `true` (recommended)
              - When `true`: Only uses transformations with `correctedJSON` as ground truth
              - When `false`: May include transformations without corrections (less reliable)
              - Corrected data provides the most accurate regression testing results

          sample_size: **Number of historical samples to test**

              - Defaults to 50 samples
              - Minimum: 1, Maximum: 1000
              - Only transformations with `correctedJSON` (user corrections) are eligible
              - Actual sample size may be smaller if insufficient corrected data exists
              - Larger samples provide more statistical confidence but take longer to process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/functions/regression",
            body=await async_maybe_transform(
                {
                    "function_name": function_name,
                    "baseline_version_num": baseline_version_num,
                    "comparison_version_num": comparison_version_num,
                    "only_corrected_data": only_corrected_data,
                    "sample_size": sample_size,
                },
                regression_run_params.RegressionRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegressionRunResponse,
        )


class RegressionResourceWithRawResponse:
    def __init__(self, regression: RegressionResource) -> None:
        self._regression = regression

        self.apply_corrections = to_raw_response_wrapper(
            regression.apply_corrections,
        )
        self.run = to_raw_response_wrapper(
            regression.run,
        )


class AsyncRegressionResourceWithRawResponse:
    def __init__(self, regression: AsyncRegressionResource) -> None:
        self._regression = regression

        self.apply_corrections = async_to_raw_response_wrapper(
            regression.apply_corrections,
        )
        self.run = async_to_raw_response_wrapper(
            regression.run,
        )


class RegressionResourceWithStreamingResponse:
    def __init__(self, regression: RegressionResource) -> None:
        self._regression = regression

        self.apply_corrections = to_streamed_response_wrapper(
            regression.apply_corrections,
        )
        self.run = to_streamed_response_wrapper(
            regression.run,
        )


class AsyncRegressionResourceWithStreamingResponse:
    def __init__(self, regression: AsyncRegressionResource) -> None:
        self._regression = regression

        self.apply_corrections = async_to_streamed_response_wrapper(
            regression.apply_corrections,
        )
        self.run = async_to_streamed_response_wrapper(
            regression.run,
        )
