# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RenderConfigInputParam", "Template"]


class Template(TypedDict, total=False):
    base64: Required[str]
    """Base64-encoded `.docx` bytes.

    In the Bem CLI, use `@path/to/file` to embed it automatically.
    """

    name: str
    """Original upload filename (e.g.

    `contract.docx`), stored for display only. Does not affect where the template is
    stored.
    """


class RenderConfigInputParam(TypedDict, total=False):
    """Request-side render configuration.

    Carries the template document as
    base64-encoded `.docx` bytes: the server validates them, stores the template,
    and derives the placeholder/style-id contract at create/update time, so
    clients never submit `placeholders` or `styleIds`. The response shape
    (`RenderConfig`) returns the derived contract.
    """

    template: Required[Template]
