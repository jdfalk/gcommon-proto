from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FilterCriteria(_message.Message):
    __slots__ = (
        "include_patterns",
        "exclude_patterns",
        "header_filters",
        "content_types",
    )
    class HeaderFiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    INCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    HEADER_FILTERS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    include_patterns: _containers.RepeatedScalarFieldContainer[str]
    exclude_patterns: _containers.RepeatedScalarFieldContainer[str]
    header_filters: _containers.ScalarMap[str, str]
    content_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        include_patterns: _Optional[_Iterable[str]] = ...,
        exclude_patterns: _Optional[_Iterable[str]] = ...,
        header_filters: _Optional[_Mapping[str, str]] = ...,
        content_types: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
