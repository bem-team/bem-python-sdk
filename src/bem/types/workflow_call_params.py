# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkflowCallParams", "Input", "InputBatchFiles", "InputBatchFilesInput", "InputSingleFile"]


class WorkflowCallParams(TypedDict, total=False):
    input: Required[Input]
    """Input file(s) for a call. Provide exactly one of `singleFile` or `batchFiles`.

    In the CLI, use the nested flags `--input.single-file` or `--input.batch-files`
    with `@path/to/file` for automatic file embedding:
    `--input.single-file '{"inputContent": "@invoice.pdf", "inputType": "pdf"}' --wait`
    """

    wait: bool
    """
    Block until the call completes (up to 30 seconds) and return the finished call
    object. Default: `false`. This is a boolean flag — use `--wait` or
    `--wait=true`, not `--wait true`.
    """

    call_reference_id: Annotated[str, PropertyInfo(alias="callReferenceID")]
    """Your reference ID for tracking this call."""

    metadata: object
    """Arbitrary JSON object attached to this call.

    Stored on the call record and injected into `transformedContent` under the
    reserved `_metadata` key (alongside `referenceID`). Must be a JSON object.
    Maximum size: 4 KB.
    """


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
    """Multiple files to process in one call.

    Each item in the `inputs` array has its own `inputContent` and `inputType`.
    """

    inputs: Iterable[InputBatchFilesInput]


class InputSingleFile(TypedDict, total=False):
    """A single file input with base64-encoded content.

    When using the Bem CLI, use `@path/to/file` in the `inputContent` field to
    automatically read and base64-encode the file:
    `--input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' --wait`
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
    """Input file(s) for a call. Provide exactly one of `singleFile` or `batchFiles`.

    In the CLI, use the nested flags `--input.single-file` or `--input.batch-files`
    with `@path/to/file` for automatic file embedding:
    `--input.single-file '{"inputContent": "@invoice.pdf", "inputType": "pdf"}' --wait`
    """

    batch_files: Annotated[InputBatchFiles, PropertyInfo(alias="batchFiles")]
    """Multiple files to process in one call.

    Each item in the `inputs` array has its own `inputContent` and `inputType`.
    """

    single_file: Annotated[InputSingleFile, PropertyInfo(alias="singleFile")]
    """A single file input with base64-encoded content.

    When using the Bem CLI, use `@path/to/file` in the `inputContent` field to
    automatically read and base64-encode the file:
    `--input.single-file '{"inputContent": "@file.pdf", "inputType": "pdf"}' --wait`
    """
