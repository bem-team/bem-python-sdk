# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..input_type import InputType

__all__ = ["FileInputParam"]


class FileInputParam(TypedDict, total=False):
    """A single file input with base64-encoded content.

    When using the Bem CLI, use `@path/to/file` in the `inputContent` field to
    automatically read and base64-encode the file:
    `--input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' --wait`
    """

    input_content: Required[Annotated[str, PropertyInfo(alias="inputContent")]]
    """Base64-encoded file content.

    In the Bem CLI, use `@path/to/file` to embed file contents automatically.
    """

    input_type: Required[Annotated[InputType, PropertyInfo(alias="inputType")]]
    """The input type of the content you're sending for transformation."""
