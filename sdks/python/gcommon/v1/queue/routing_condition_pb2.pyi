from gcommon.v1.queue import priority_range_pb2 as _priority_range_pb2
from gcommon.v1.queue import size_range_pb2 as _size_range_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingCondition(_message.Message):
    __slots__ = ("header_matches", "content_pattern", "routing_key_pattern", "message_type", "priority_range", "size_range")
    class HeaderMatchesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADER_MATCHES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_PATTERN_FIELD_NUMBER: _ClassVar[int]
    ROUTING_KEY_PATTERN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_RANGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_RANGE_FIELD_NUMBER: _ClassVar[int]
    header_matches: _containers.ScalarMap[str, str]
    content_pattern: str
    routing_key_pattern: str
    message_type: str
    priority_range: _priority_range_pb2.PriorityRange
    size_range: _size_range_pb2.SizeRange
    def __init__(self, header_matches: _Optional[_Mapping[str, str]] = ..., content_pattern: _Optional[str] = ..., routing_key_pattern: _Optional[str] = ..., message_type: _Optional[str] = ..., priority_range: _Optional[_Union[_priority_range_pb2.PriorityRange, _Mapping]] = ..., size_range: _Optional[_Union[_size_range_pb2.SizeRange, _Mapping]] = ...) -> None: ...
