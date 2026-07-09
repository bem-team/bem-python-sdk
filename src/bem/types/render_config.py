# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RenderConfig", "Template", "TemplatePlaceholders"]


class TemplatePlaceholders(BaseModel):
    """
    The placeholder contract a Render template declares, grouped by how each
    placeholder is filled. Derived from the template at create/update time by
    scanning its `docxtpl` tags; not user-supplied.

    - `stringKeys`: bare string placeholders (`{{ key }}`) filled with a single
    value.
    - `blockKeys`: wrapped-primitive placeholders (`{{p key }}`) — bind one core
    primitive (paragraph, table, image, or list). The placeholder's own
    paragraph dissolves and is replaced by the rendered subdocument's blocks,
    rather than substituting text inline.
    """

    block_keys: List[str] = FieldInfo(alias="blockKeys")

    string_keys: List[str] = FieldInfo(alias="stringKeys")


class Template(BaseModel):
    """
    The uploaded template: its filename, a short-lived presigned download URL,
    and the placeholder/style contract derived from it. Absent on configs
    created before template capture existed.
    """

    download_url: Optional[str] = FieldInfo(alias="downloadURL", default=None)
    """Short-lived presigned URL to download the stored `.docx`.

    The private storage location is never exposed.
    """

    list_kinds: Optional[List[Literal["decimal", "bullet"]]] = FieldInfo(alias="listKinds", default=None)
    """
    Supported list kinds (`decimal`, `bullet`) the template's `numbering.xml`
    defines an `abstractNum` for. Empty means the template can hold no list, so any
    list primitive will fail at render.
    """

    name: Optional[str] = None
    """Original filename of the uploaded template (e.g.

    `contract.docx`), echoed back for display. Absent on templates uploaded before
    the filename was captured.
    """

    placeholders: Optional[TemplatePlaceholders] = None
    """
    The placeholder contract a Render template declares, grouped by how each
    placeholder is filled. Derived from the template at create/update time by
    scanning its `docxtpl` tags; not user-supplied.

    - `stringKeys`: bare string placeholders (`{{ key }}`) filled with a single
      value.
    - `blockKeys`: wrapped-primitive placeholders (`{{p key }}`) — bind one core
      primitive (paragraph, table, image, or list). The placeholder's own paragraph
      dissolves and is replaced by the rendered subdocument's blocks, rather than
      substituting text inline.
    """

    style_ids: Optional[List[str]] = FieldInfo(alias="styleIds", default=None)
    """
    Paragraph/character style IDs the uploaded template defines and the rendered
    output can reference. Derived from the template's `styles.xml` at create/update
    time.
    """

    table_style_ids: Optional[List[str]] = FieldInfo(alias="tableStyleIds", default=None)
    """
    Style IDs whose type is table — the styles a `table` primitive's required
    `styleId` can name. Empty means the template defines no table style, so any
    table primitive will fail at render.
    """


class RenderConfig(BaseModel):
    """Per-version configuration for a Render function.

    Render emits a `.docx` from schema-typed JSON by composing the JSON into a
    `.docx` template. The template document is stored server-side; this response
    exposes only the contract derived from it. Schema validation runs internally
    in the ML service against the bundled core schema; no customer-supplied
    schema rides this surface.
    """

    template: Optional[Template] = None
    """
    The uploaded template: its filename, a short-lived presigned download URL, and
    the placeholder/style contract derived from it. Absent on configs created before
    template capture existed.
    """
