# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnrichConfigParam", "Step"]


class Step(TypedDict, total=False):
    """Single enrichment step configuration.

    **Process Flow:**
    1. Extract values from `sourceField` using JMESPath
    2. Perform search against the specified collection (semantic, exact, or hybrid based on `searchMode`)
    3. Return top K matches sorted by relevance (best match first)
    4. Inject results into `targetField`

    **Search Modes:**
    - `semantic` (default): Vector similarity search - best for natural language and conceptual matching
    - `exact`: Exact keyword matching - best for SKU numbers, IDs, routing numbers
    - `hybrid`: Combined semantic + keyword search - best for tags and categories

    **Result Format:**
    - Results are always returned as an array (list), regardless of `topK` value
    - Array is sorted by relevance (best match first)
    - Each result contains `data` (the collection item) and optionally `cosineDistance`
    - With `topK=1`: Returns array with single best match: `[{data: {...}, cosineDistance: 0.15}]`
    - With `topK>1`: Returns array with multiple matches sorted by relevance
    """

    collection_name: Required[Annotated[str, PropertyInfo(alias="collectionName")]]
    """Name of the collection to search against.

    The collection must exist and contain items. Supports hierarchical paths when
    used with `includeSubcollections`.
    """

    source_field: Required[Annotated[str, PropertyInfo(alias="sourceField")]]
    """
    JMESPath expression to extract source data for semantic search. Can extract
    single values or arrays. All extracted values will be used for search.
    """

    target_field: Required[Annotated[str, PropertyInfo(alias="targetField")]]
    """
    Field path where enriched results should be placed. Use simple field names
    (e.g., "enriched_products"). Results are always injected as an array (list),
    regardless of topK value.
    """

    include_cosine_distance: Annotated[bool, PropertyInfo(alias="includeCosineDistance")]
    """
    Whether to include cosine distance scores in results. Cosine distance ranges
    from 0.0 (perfect match) to 2.0 (completely dissimilar). Lower scores indicate
    better semantic similarity.

    When enabled, each result includes a `cosineDistance` field.
    """

    include_subcollections: Annotated[bool, PropertyInfo(alias="includeSubcollections")]
    """
    When true, searches all collections under the hierarchical path. For example,
    "customers" will match "customers", "customers.premium", etc.
    """

    score_threshold: Annotated[float, PropertyInfo(alias="scoreThreshold")]
    """
    Maximum cosine distance threshold for filtering results (default: 0.6). Results
    with cosine distance above this threshold are excluded.

    **Only applies to `semantic` and `hybrid` search modes.** Exact search does not
    use cosine distance and ignores this setting.

    Cosine distance ranges from 0.0 (identical) to 2.0 (opposite):

    - 0.0 - 0.3: Very similar (strict threshold, high-quality matches only)
    - 0.3 - 0.6: Reasonably similar (moderate threshold)
    - 0.6 - 1.0: Loosely related (lenient threshold)
    - > 1.0: Rarely useful — allows nearly unrelated results

    For most semantic search use cases, good matches typically fall in the 0.2 - 0.5
    range.
    """

    search_mode: Annotated[Literal["semantic", "exact", "hybrid"], PropertyInfo(alias="searchMode")]
    """Search mode to use for enrichment (default: "semantic").

    **semantic**: Vector similarity search using dense embeddings. Best for finding
    conceptually similar items.

    - Use for: Product descriptions, natural language content
    - Example: "red sports car" matches "crimson convertible automobile"

    **exact**: Exact keyword matching using PostgreSQL text search. Best for exact
    identifiers.

    - Use for: SKU numbers, routing numbers, account IDs, exact tags
    - Example: "SKU-12345" only matches items containing that exact text

    **hybrid**: Combined search using 20% semantic + 80% sparse embeddings
    (keyword-based).

    - Use for: Tags, categories, partial identifiers
    - Example: Balances semantic meaning with exact keyword matching
    """

    top_k: Annotated[int, PropertyInfo(alias="topK")]
    """
    Number of top matching results to return per query (default: 1). Results are
    always returned as an array (list) and automatically sorted by cosine distance
    (best match = lowest distance first).

    - 1: Returns array with single best match: `[{...}]`
    - > 1: Returns array with multiple matches: `[{...}, {...}, ...]`
    """


class EnrichConfigParam(TypedDict, total=False):
    """Configuration for enrich function with semantic search steps.

    **How Enrich Functions Work:**

    Enrich functions use semantic search to augment JSON data with relevant information from collections.
    They take JSON input (typically from a transform function), extract specified fields, perform vector-based
    semantic search against collections, and inject the results back into the data.

    **Input Requirements:**
    - Must receive JSON input (typically uploaded to S3 from a previous function)
    - Can be chained after transform or other functions that produce JSON output

    **Example Use Cases:**
    - Match product descriptions to SKU codes from a product catalog
    - Enrich customer data with account information
    - Link order line items to inventory records

    **Configuration:**
    - Define one or more enrichment steps
    - Each step extracts values, searches a collection, and injects results
    - Steps are executed sequentially
    """

    steps: Required[Iterable[Step]]
    """Array of enrichment steps to execute sequentially"""
