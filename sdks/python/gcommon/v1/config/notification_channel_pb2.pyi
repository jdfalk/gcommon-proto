from gcommon.v1.common import channel_type_pb2 as _channel_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigNotificationChannel(_message.Message):
    __slots__ = ("type", "config", "enabled", "priority")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    type: _channel_type_pb2.ChannelType
    config: _containers.ScalarMap[str, str]
    enabled: bool
    priority: int
    def __init__(self, type: _Optional[_Union[_channel_type_pb2.ChannelType, str]] = ..., config: _Optional[_Mapping[str, str]] = ..., enabled: bool = ..., priority: _Optional[int] = ...) -> None: ...
