# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["FunctionType"]

FunctionType: TypeAlias = Literal[
    "transform", "extract", "route", "send", "split", "join", "analyze", "payload_shaping", "enrich"
]
