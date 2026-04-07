# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InferSchemaCreateResponse", "Analysis", "AnalysisDocumentType"]


class AnalysisDocumentType(BaseModel):
    """Describes a distinct document type found in the file."""

    count: int
    """Number of instances of this document type in the file."""

    description: str
    """Brief description of this document type."""

    name: str
    """Short snake_case name (e.g. "invoice", "receipt", "utility_bill")."""


class Analysis(BaseModel):
    """Analysis result returned by the infer-schema endpoint."""

    content_nature: str = FieldInfo(alias="contentNature")
    """
    Classification of the primary content. One of: `textual`, `visual`, `audio`,
    `video`, `mixed`.
    """

    content_type: str = FieldInfo(alias="contentType")
    """MIME content type of the uploaded file."""

    description: str
    """2-3 sentence description of what the file contains."""

    document_types: List[AnalysisDocumentType] = FieldInfo(alias="documentTypes")
    """List of distinct document types found in the file with counts."""

    file_name: str = FieldInfo(alias="fileName")
    """Original filename of the uploaded file."""

    file_type: str = FieldInfo(alias="fileType")
    """High-level file category (e.g. "document", "image", "spreadsheet", "email")."""

    is_multi_document: bool = FieldInfo(alias="isMultiDocument")
    """Whether the file contains multiple separate documents bundled together."""

    size_bytes: int = FieldInfo(alias="sizeBytes")
    """Size of the uploaded file in bytes."""

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)
    """Inferred JSON Schema representing all extractable data fields."""


class InferSchemaCreateResponse(BaseModel):
    """Response from the infer-schema endpoint."""

    analysis: Analysis
    """Analysis result returned by the infer-schema endpoint."""

    filename: str
    """Original filename of the uploaded file."""
