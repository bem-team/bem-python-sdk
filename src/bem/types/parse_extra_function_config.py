# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ParseExtraFunctionConfig"]


class ParseExtraFunctionConfig(BaseModel):
    """Cross-cutting toggles for Parse functions.

    Mirrors the `extraConfig`
    surface on Extract / Join — separated from `parseConfig` so the per-call
    Parse output shape stays distinct from operator-level execution flags.
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
