from gcommon.v1.queue import routing_condition_pb2 as _routing_condition_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingRule(_message.Message):
    __slots__ = ("name", "priority", "condition", "destination", "enabled", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    priority: int
    condition: _routing_condition_pb2.RoutingCondition
    destination: str
    enabled: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., priority: _Optional[int] = ..., condition: _Optional[_Union[_routing_condition_pb2.RoutingCondition, _Mapping]] = ..., destination: _Optional[str] = ..., enabled: _Optional[bool] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
