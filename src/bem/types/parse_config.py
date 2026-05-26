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

    enable_bounding_boxes: Optional[bool] = FieldInfo(alias="enableBoundingBoxes", default=None)
    """
    When true, return per-section and per-entity-mention coordinates in the parse
    event's `fieldBoundingBoxes` map (same shape as Extract: JSON Pointer key →
    array of `{page, left, top, width, height}` with coordinates normalized to [0,
    1]). Keys are `/sections/{N}` and `/entities/{N}/occurrences/{M}` into the parse
    output. Only applies to the open-ended discovery path (no `schema`) and to
    vision input types. Bedrock-backed parse functions silently return an empty map
    (no native bbox support). Defaults to false.
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
