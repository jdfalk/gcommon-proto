from gcommon.v1.queue import content_filter_pb2 as _content_filter_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageFilterConfig(_message.Message):
    __slots__ = ("header_filters", "content_filters", "routing_key_patterns", "message_types", "filter_expressions", "exclude_matching")
    class HeaderFiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_FILTERS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    ROUTING_KEY_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPES_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_MATCHING_FIELD_NUMBER: _ClassVar[int]
    header_filters: _containers.ScalarMap[str, str]
    content_filters: _containers.RepeatedCompositeFieldContainer[_content_filter_pb2.ContentFilter]
    routing_key_patterns: _containers.RepeatedScalarFieldContainer[str]
    message_types: _containers.RepeatedScalarFieldContainer[str]
    filter_expressions: _containers.RepeatedScalarFieldContainer[str]
    exclude_matching: bool
    def __init__(self, header_filters: _Optional[_Mapping[str, str]] = ..., content_filters: _Optional[_Iterable[_Union[_content_filter_pb2.ContentFilter, _Mapping]]] = ..., routing_key_patterns: _Optional[_Iterable[str]] = ..., message_types: _Optional[_Iterable[str]] = ..., filter_expressions: _Optional[_Iterable[str]] = ..., exclude_matching: bool = ...) -> None: ...
