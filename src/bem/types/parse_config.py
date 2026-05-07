# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ParseConfig"]


class ParseConfig(BaseModel):
    """Per-version configuration for a Parse function.

    Parse renders document pages (PDF, image) via vision LLM and emits
    structured JSON. The two toggles below independently control entity
    extraction (a per-call output concern) and cross-document memory
    linking (an environment-wide concern).
    """

    extract_entities: Optional[bool] = FieldInfo(alias="extractEntities", default=None)
    """
    When true, extract named entities (people, organizations, products, studies,
    identifiers, etc.) and the relationships between them, and dedupe by canonical
    name within the document. When false, only `sections[]` is extracted;
    `entities[]` and `relationships[]` come back empty in the parse output. Defaults
    to true.
    """

    link_across_documents: Optional[bool] = FieldInfo(alias="linkAcrossDocuments", default=None)
    """
    When true, link this document's entities to entities seen in earlier documents
    in this environment, building one canonical record per real-world thing across
    the corpus. Visible in the Memory tab and queryable via `POST /v3/fs` (op=find /
    open / xref). Doesn't change this call's parse output. Requires
    `extractEntities=true`. Defaults to true.
    """

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)
    """Optional JSONSchema.

    When provided, each chunk performs schema-guided extraction. When absent, chunks
    perform open-ended discovery and return sections, entities, and relationships
    per the discovery schema.
    """
