# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CollectionCountTokensResponse", "TokenCount"]


class TokenCount(BaseModel):
    """Per-text token count result."""

    char_count: Optional[int] = None
    """Character count of the input text."""

    exceeds_limit: Optional[bool] = None
    """True if `token_count` exceeds the embedding model's per-text limit."""

    index: Optional[int] = None
    """Zero-based position of this entry in the request `texts` array."""

    token_count: Optional[int] = None
    """Number of tokens produced by the tokenizer."""


class CollectionCountTokensResponse(BaseModel):
    """Response for the token count endpoint."""

    max_token_limit: Optional[int] = None
    """Maximum tokens allowed per text by the embedding model."""

    texts_exceeding_limit: Optional[int] = None
    """Number of input texts that exceed `max_token_limit`."""

    token_counts: Optional[List[TokenCount]] = None
    """Per-text tokenization results in the same order as the request."""

    total_tokens: Optional[int] = None
    """Sum of `token_count` across all texts."""
