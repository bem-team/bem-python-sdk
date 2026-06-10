# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .enrich_step_param import EnrichStepParam

__all__ = ["EnrichConfigParam", "Endpoint"]


class Endpoint(TypedDict, total=False):
    """A named HTTP endpoint that an enrich step can call to fetch enrichment data.

    The platform makes one request per extracted source value, substituting the value
    as a query parameter or body template placeholder. The raw response (or the
    sub-value selected by `responsePath`) is injected into the output, or passed to
    LLM agent reasoning when `matchInstructions` is set.

    **Request formats:**
    - `GET`: Appends `?{queryParam}={value}` to the URL.
    - `POST`: Sends `bodyTemplate` as the request body, replacing `{value}` with the extracted value.
    """

    method: Required[Literal["GET", "POST"]]
    """HTTP method to use."""

    name: Required[str]
    """Unique name for this endpoint, referenced by enrichStep.endpointName."""

    url: Required[str]
    """Full URL of the endpoint (must be http:// or https://)."""

    body_template: Annotated[str, PropertyInfo(alias="bodyTemplate")]
    """
    JSON body template for POST requests. **Required for POST endpoints.** Must
    contain the `{value}` placeholder, which is replaced with the extracted source
    value at runtime.

    Example: `bodyTemplate: "{\"query\": \"{value}\", \"limit\": 10}"`
    """

    headers: object
    """Additional HTTP headers to include in every request (e.g.

    `Authorization: Bearer <token>`).
    """

    match_instructions: Annotated[str, PropertyInfo(alias="matchInstructions")]
    """Natural-language instructions for LLM agent reasoning.

    When set, the candidates fetched from the endpoint are passed to an LLM with
    these instructions, which selects the best match(es) and returns them with
    confidence scores. Each injected result has the shape
    `{ data, confidence, reasoning? }`.

    When omitted, the raw fetched value is injected without any LLM involvement.
    """

    match_top_k: Annotated[int, PropertyInfo(alias="matchTopK")]
    """
    Maximum number of ranked matches to return per source value when
    `matchInstructions` is set (default: 1). Ignored when `matchInstructions` is
    empty.
    """

    max_candidates: Annotated[int, PropertyInfo(alias="maxCandidates")]
    """LLM batch size during agent reasoning (default: 50).

    All candidates — across all fetched pages — are scored in batches of this size.
    Smaller values reduce per-call token usage; larger values mean fewer LLM calls.
    Ignored when `matchInstructions` is empty.
    """

    max_pages: Annotated[int, PropertyInfo(alias="maxPages")]
    """Maximum number of pages to fetch (default: 10).

    Acts as a safety cap against infinite pagination loops when the server never
    returns an empty cursor.
    """

    next_page_param: Annotated[str, PropertyInfo(alias="nextPageParam")]
    """
    Query parameter name used to pass the cursor on subsequent GET requests, or the
    `{placeholder}` name used in the POST `bodyTemplate` (e.g. `"cursor"`,
    `"pageToken"`, `"offset"`).

    Must be set together with `nextPagePath`.
    """

    next_page_path: Annotated[str, PropertyInfo(alias="nextPagePath")]
    """
    JMESPath expression applied to each raw response to extract the cursor or token
    for the next page (e.g. `"nextCursor"`, `"pagination.nextToken"`). An absent,
    null, or empty-string result stops pagination. Both string and numeric values
    are supported — numbers are converted to their decimal string representation
    before being forwarded as a query parameter.

    Must be set together with `nextPageParam`.

    **Supported pagination styles:**

    - **Cursor/token-based** — server returns an opaque token in the response body
      (e.g. `{"nextCursor": "abc123"}`). Set `nextPagePath: "nextCursor"` and the
      platform forwards it verbatim on the next request.
    - **Server-computed offset/page** — server echoes back the next offset or page
      number in the response body (e.g. `{"nextOffset": 50}` or `{"nextPage": 2}`).
      Set `nextPagePath: "nextOffset"` and the platform forwards the value as-is.

    **Not supported:**

    - **Client-computed offset** — APIs where the client must compute
      `offset += limit` itself (e.g. `?offset=0&limit=50` with no next-offset in the
      response). Workaround: ask the API provider to return the next offset in the
      response body, or bake a fixed page size into the URL and use a server-side
      cursor instead.
    - **Client-computed page number** — APIs where the client increments `?page=N`
      itself with no next-page value in the response. Same workaround applies.
    - **Link header** — `Link: <url>; rel="next"` in HTTP response headers. The
      platform only inspects the response body.
    """

    query_param: Annotated[str, PropertyInfo(alias="queryParam")]
    """
    Query parameter name used to pass the extracted source value. **Required for GET
    endpoints.** The value is URL-encoded and appended as
    `?{queryParam}={sourceValue}`.

    Example: `queryParam: "q"` → `GET /products?q=blue+widget`
    """

    response_path: Annotated[str, PropertyInfo(alias="responsePath")]
    """
    JMESPath expression applied to the response body to extract the enrichment
    value. Omit to use the entire response body as the result.

    **For agent reasoning:** use a wildcard projection (e.g. `items[*]` or
    `results[*].data`) so the endpoint's list of candidates is flattened into an
    array before being passed to the LLM. A non-wildcard path (e.g. `data.product`)
    extracts a single value treated as one candidate.

    **Response size:** the platform reads at most 50 MB of the response body before
    decoding, regardless of the Content-Length header.
    """


class EnrichConfigParam(TypedDict, total=False):
    """Configuration for an enrich function.

    **How Enrich Functions Work:**

    Enrich functions augment JSON input with data from external sources. They take JSON input
    (typically from a previous function), extract specified fields, fetch or search for matching
    data, and inject the results back into the JSON.

    **Data Sources:**
    - **Collections** (`source: "collection"`): Vector/keyword search against a BEM collection.
    Best for semantic matching against pre-indexed documents.
    - **Endpoints** (`source: "endpoint"`): HTTP call to any user-provided REST API.
    Best for looking up live data from CRMs, ERPs, or other external systems.
    Optionally uses LLM agent reasoning to rank candidates returned by the endpoint.

    **Input Requirements:**
    - Must receive JSON input (typically from a previous function's output)

    **Example Use Cases:**
    - Match product descriptions to SKU codes from a product catalog collection
    - Enrich customer data with account details from a CRM endpoint
    - Use LLM agent reasoning to fuzzy-match line item descriptions to catalog products

    **Configuration:**
    - Define named endpoints (for endpoint-source steps)
    - Define one or more enrichment steps; steps are executed sequentially
    """

    steps: Required[Iterable[EnrichStepParam]]
    """Array of enrichment steps to execute sequentially."""

    endpoints: Iterable[Endpoint]
    """
    Named HTTP endpoints available to endpoint-source steps. Each endpoint must have
    a unique `name` referenced by the step's `endpointName`. Required when any step
    uses `source: "endpoint"`.
    """
