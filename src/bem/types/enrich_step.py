# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EnrichStep"]


class EnrichStep(BaseModel):
    """Single enrichment step configuration.

    **Process Flow (collection source):**
    1. Extract values from `sourceField` using JMESPath
    2. Perform search against the specified collection (semantic, exact, or hybrid based on `searchMode`)
    3. Return top K matches sorted by relevance (best match first)
    4. Inject results into `targetField`

    **Process Flow (endpoint source):**
    1. Extract values from `sourceField` using JMESPath
    2. Call the named endpoint once per extracted value, following pagination if
    `nextPagePath`/`nextPageParam` are configured on the endpoint
    3. Optionally apply LLM agent reasoning to rank candidates (`matchInstructions`),
    batching across all fetched pages in groups of `maxCandidates`
    4. Inject results into `targetField`

    **Collection Search Modes** (`source: "collection"` only):
    - `semantic` (default): Vector similarity search — best for natural language and conceptual matching
    - `exact`: Exact keyword matching — best for SKU numbers, IDs, routing numbers
    - `hybrid`: Combined semantic + keyword search — best for tags and categories

    **Result Format (collection source, exact mode — no re-ranking):**
    - Always an array sorted by relevance (best match first)
    - Each element: `{ data, cosine_distance? }` or `{ data, hybrid_score? }`

    **Result Format (collection source, semantic/hybrid — re-ranking always on):**
    - Re-ranking uses a fixed, built-in instruction to the LLM (rank the candidates by how well each matches the source value); it is not configurable per step
    - Array of matches, best first: `[{ data, rank, confidence?, reasoning?, score?, scoreType? }, ...]`
    - `rank` is 1-based (1 = best)
    - `confidence` is the LLM's 0–1 score. It is present only for entries the LLM ranked and **omitted** for backfilled entries (see below) — a missing `confidence` means "not ranked by the LLM", not a score of 0
    - `score` is the retrieval score and `scoreType` says which metric it is: `"cosineDistance"` for semantic or `"hybridScore"` for hybrid. Both are 0–2 dissimilarities where **lower = better** — hybrid's Reciprocal Rank Fusion score is mapped onto the same scale as cosine distance (0 = top of both rankings). Included only when `includeScore` is set
    - Results are de-duplicated by item payload, so they are distinct. Length is `min(distinct candidates retrieved, topK)`; semantic additionally drops candidates beyond `scoreThreshold`. The LLM re-orders the survivors; if it ranks fewer than that length, the remaining survivors are backfilled in retrieval (score) order with `confidence` omitted

    **Result Format (endpoint source, no matchInstructions):**
    - Always an array; the raw fetched value is the single element

    **Result Format (endpoint source, with matchInstructions):**
    - Array of LLM-ranked matches, best first: `[{ data, rank, confidence, reasoning? }, ...]`
    - `rank` is 1-based (1 = best); `confidence` is the LLM's 0–1 score
    - Length capped by `enrichEndpoint.matchTopK` (default 1)
    """

    source_field: str = FieldInfo(alias="sourceField")
    """
    JMESPath expression to extract source data. Can extract a single value or an
    array. Each extracted value is looked up independently.
    """

    target_field: str = FieldInfo(alias="targetField")
    """
    Field path where enriched results should be placed. Use simple field names
    (e.g., "enriched_products"). Results are always injected as an array (list),
    regardless of topK value.
    """

    collection_name: Optional[str] = FieldInfo(alias="collectionName", default=None)
    """
    Name of the collection to search against. Required when `source` is
    `"collection"`. The collection must exist and contain items. Supports
    hierarchical paths when used with `includeSubcollections`.
    """

    endpoint_name: Optional[str] = FieldInfo(alias="endpointName", default=None)
    """
    Name of an endpoint defined in `enrichConfig.endpoints`. Required when `source`
    is `"endpoint"`.
    """

    include_score: Optional[bool] = FieldInfo(alias="includeScore", default=None)
    """Whether to include retrieval scores in results.

    When enabled, each result includes a `score` field and a `scoreType` identifying
    the metric:

    - `"cosineDistance"` (semantic): 0.0 (perfect match) to 2.0 (completely
      dissimilar) — lower is better.
    - `"hybridScore"` (hybrid): an RRF score mapped onto cosine distance's 0–2 scale
      — lower is better (0.0 = top of both rankings).
    """

    include_subcollections: Optional[bool] = FieldInfo(alias="includeSubcollections", default=None)
    """
    When true, searches all collections under the hierarchical path. For example,
    "customers" will match "customers", "customers.premium", etc.
    """

    score_threshold: Optional[float] = FieldInfo(alias="scoreThreshold", default=None)
    """
    Maximum cosine distance threshold for filtering results (default: 0.6). Results
    with cosine distance above this threshold are excluded.

    **Applies to `semantic` and `hybrid` search modes.** For `hybrid`, the
    Reciprocal Rank Fusion score is mapped onto the same 0–2 dissimilarity scale as
    cosine distance, so a single threshold works for both. `exact` uses keyword
    matching and ignores this setting. Note the default `0.6` is calibrated for
    cosine distance and is relatively strict for hybrid.

    Cosine distance ranges from 0.0 (identical) to 2.0 (opposite):

    - 0.0 - 0.3: Very similar (strict threshold, high-quality matches only)
    - 0.3 - 0.6: Reasonably similar (moderate threshold)
    - 0.6 - 1.0: Loosely related (lenient threshold)
    - > 1.0: Rarely useful — allows nearly unrelated results

    For most semantic search use cases, good matches typically fall in the 0.2 - 0.5
    range.
    """

    search_mode: Optional[Literal["semantic", "exact", "hybrid"]] = FieldInfo(alias="searchMode", default=None)
    """Search mode to use for enrichment (default: "semantic").

    **semantic**: Vector similarity search using dense embeddings. Best for finding
    conceptually similar items.

    - Use for: Product descriptions, natural language content
    - Example: "red sports car" matches "crimson convertible automobile"

    **exact**: Exact keyword matching using PostgreSQL text search. Best for exact
    identifiers.

    - Use for: SKU numbers, routing numbers, account IDs, exact tags
    - Example: "SKU-12345" only matches items containing that exact text

    **hybrid**: Fuses the dense (semantic) and sparse (keyword) rankings with
    weighted Reciprocal Rank Fusion (k=60, 0.5 dense / 0.5 sparse). Because RRF
    combines rank positions rather than raw scores, semantic meaning and exact-token
    overlap contribute on the same scale.

    - Use for: Tags, categories, partial identifiers
    - Example: Balances semantic meaning with exact keyword matching
    """

    source: Optional[Literal["collection", "endpoint"]] = None
    """Where to fetch enrichment data from (default: `"collection"`).

    - `"collection"`: Vector/keyword search against a BEM collection. Requires
      `collectionName`.
    - `"endpoint"`: HTTP call to a named endpoint defined in
      `enrichConfig.endpoints`. Requires `endpointName`.
    """

    top_k: Optional[int] = FieldInfo(alias="topK", default=None)
    """
    Number of top matching results to return per query (default: 1). Results are
    always returned as an array (list), sorted best match first (by cosine distance
    for `semantic`/`exact`, or by fused relevance score for `hybrid`). Duplicate
    items are collapsed, so results are distinct: you get `topK` distinct matches
    unless the collection contains fewer.

    - 1: Returns array with single best match: `[{...}]`
    - > 1: Returns array with multiple matches: `[{...}, {...}, ...]`

    When re-ranking is on (the default for `semantic`/`hybrid`), `topK` is still the
    number of results returned — re-ranking changes their order, not the count. The
    candidate pool the LLM chooses from is widened internally to at least 5, so even
    `topK: 1` re-ranks a real pool and returns the single best match.
    """
