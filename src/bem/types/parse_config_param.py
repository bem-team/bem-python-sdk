# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ParseConfigParam"]


class ParseConfigParam(TypedDict, total=False):
    """Per-version configuration for a Parse function.

    Parse renders document pages (PDF, image) via vision LLM and emits
    structured JSON. The two toggles below independently control entity
    extraction (a per-call output concern) and cross-document memory
    linking (an environment-wide concern).
    """

    extract_entities: Annotated[bool, PropertyInfo(alias="extractEntities")]
    """
    When true, extract named entities (people, organizations, products, studies,
    identifiers, etc.) and the relationships between them, and dedupe by canonical
    name within the document. When false, only `sections[]` is extracted;
    `entities[]` and `relationships[]` come back empty in the parse output. Defaults
    to true.
    """

    link_across_documents: Annotated[bool, PropertyInfo(alias="linkAcrossDocuments")]
    """
    When true, link this document's entities to entities seen in earlier documents
    in this environment, building one canonical record per real-world thing across
    the corpus. Visible in the Memory tab and queryable via `POST /v3/fs` (op=find /
    open / xref). Doesn't change this call's parse output. Requires
    `extractEntities=true`. Defaults to true.
    """

    schema: object
    """Optional JSONSchema.

    When provided, each chunk performs schema-guided extraction. When absent, chunks
    perform open-ended discovery and return sections, entities, and relationships
    per the discovery schema.
    """
