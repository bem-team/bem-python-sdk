# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SynonymAddParams"]


class SynonymAddParams(TypedDict, total=False):
    text: Required[str]
    """The human-readable synonym surface form to attach (e.g.

    `Acme Corp`, `ACME`). It is normalized (lowercased, whitespace-folded) for the
    uniqueness key and the matcher's exact-match path.
    """

    bucket: str
    """Optional bucket public ID (`bkt_...`) to scope the entity lookup to one bucket.

    Omit for the unscoped (all account+environment) view.
    """

    locale: str
    """Optional BCP 47 locale tag (e.g. `en-US`) for language-specific synonyms."""
