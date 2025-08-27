from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageFilter(_message.Message):
    __slots__ = ("header_filters", "property_filters", "min_priority", "max_age_seconds", "content_type", "filter_expression")
    class HeaderFiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PropertyFiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FILTERS_FIELD_NUMBER: _ClassVar[int]
    MIN_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    header_filters: _containers.ScalarMap[str, str]
    property_filters: _containers.ScalarMap[str, str]
    min_priority: int
    max_age_seconds: int
    content_type: str
    filter_expression: str
    def __init__(self, header_filters: _Optional[_Mapping[str, str]] = ..., property_filters: _Optional[_Mapping[str, str]] = ..., min_priority: _Optional[int] = ..., max_age_seconds: _Optional[int] = ..., content_type: _Optional[str] = ..., filter_expression: _Optional[str] = ...) -> None: ...
