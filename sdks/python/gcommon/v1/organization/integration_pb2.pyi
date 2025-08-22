from gcommon.v1.common import key_value_pb2 as _key_value_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Integration(_message.Message):
    __slots__ = ("name", "enabled", "config", "created_at", "configured_by")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_BY_FIELD_NUMBER: _ClassVar[int]
    name: str
    enabled: bool
    config: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    created_at: _timestamp_pb2.Timestamp
    configured_by: str
    def __init__(self, name: _Optional[str] = ..., enabled: bool = ..., config: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., configured_by: _Optional[str] = ...) -> None: ...
