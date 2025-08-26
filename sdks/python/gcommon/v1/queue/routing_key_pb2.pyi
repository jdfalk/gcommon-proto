from gcommon.v1.common import routing_pattern_pb2 as _routing_pattern_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingKey(_message.Message):
    __slots__ = ("key", "pattern_type", "case_sensitive", "priority", "attributes")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    PATTERN_TYPE_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    key: str
    pattern_type: _routing_pattern_pb2.RoutingPattern
    case_sensitive: bool
    priority: int
    attributes: _containers.ScalarMap[str, str]
    def __init__(self, key: _Optional[str] = ..., pattern_type: _Optional[_Union[_routing_pattern_pb2.RoutingPattern, str]] = ..., case_sensitive: _Optional[bool] = ..., priority: _Optional[int] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...
