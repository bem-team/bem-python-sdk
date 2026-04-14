# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkflowCallParams", "Input", "InputBatchFiles", "InputBatchFilesInput", "InputSingleFile"]


class WorkflowCallParams(TypedDict, total=False):
    input: Required[Input]
    """Input to the workflow call.

    Provide exactly one of `singleFile` or `batchFiles`.
    """

    wait: bool
    """
    When `true`, the endpoint blocks until the call completes (up to 30 seconds) and
    returns the finished call object. Default: `false`.
    """

    call_reference_id: Annotated[str, PropertyInfo(alias="callReferenceID")]
    """Your reference ID for tracking this call."""


class InputBatchFilesInput(TypedDict, total=False):
    input_content: Required[Annotated[str, PropertyInfo(alias="inputContent")]]
    """Base64-encoded file content.

    In the Bem CLI, use `@path/to/file` to embed file contents automatically.
    """

    input_type: Required[
        Annotated[
            Literal[
                "csv",
                "docx",
                "email",
                "heic",
                "html",
                "jpeg",
                "json",
                "heif",
                "m4a",
                "mp3",
                "pdf",
                "png",
                "text",
                "wav",
                "webp",
                "xls",
                "xlsx",
                "xml",
            ],
            PropertyInfo(alias="inputType"),
        ]
    ]
    """The input type of the content you're sending for transformation."""

    item_reference_id: Annotated[str, PropertyInfo(alias="itemReferenceID")]


class InputBatchFiles(TypedDict, total=False):
    inputs: Iterable[InputBatchFilesInput]


class InputSingleFile(TypedDict, total=False):
    """A single file input with base64-encoded content.

    When using the Bem CLI, use `@path/to/file` in the `inputContent` field to
    automatically read and base64-encode the file:
    `--input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}'`
    """

    input_content: Required[Annotated[str, PropertyInfo(alias="inputContent")]]
    """Base64-encoded file content.

    In the Bem CLI, use `@path/to/file` to embed file contents automatically.
    """

    input_type: Required[
        Annotated[
            Literal[
                "csv",
                "docx",
                "email",
                "heic",
                "html",
                "jpeg",
                "json",
                "heif",
                "m4a",
                "mp3",
                "pdf",
                "png",
                "text",
                "wav",
                "webp",
                "xls",
                "xlsx",
                "xml",
            ],
            PropertyInfo(alias="inputType"),
        ]
    ]
    """The input type of the content you're sending for transformation."""


class Input(TypedDict, total=False):
    """Input to the workflow call.

    Provide exactly one of `singleFile` or `batchFiles`.
    """

    batch_files: Annotated[InputBatchFiles, PropertyInfo(alias="batchFiles")]

    single_file: Annotated[InputSingleFile, PropertyInfo(alias="singleFile")]
    """A single file input with base64-encoded content.

    When using the Bem CLI, use `@path/to/file` in the `inputContent` field to
    automatically read and base64-encode the file:
    `--input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}'`
    """
