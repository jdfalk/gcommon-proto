import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigWatch(_message.Message):
    __slots__ = ("watch_id", "key_pattern", "namespace", "watch_type", "created_at", "created_by", "options", "active")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WATCH_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_PATTERN_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    WATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    watch_id: str
    key_pattern: str
    namespace: str
    watch_type: str
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    options: _containers.ScalarMap[str, str]
    active: bool
    def __init__(self, watch_id: _Optional[str] = ..., key_pattern: _Optional[str] = ..., namespace: _Optional[str] = ..., watch_type: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ..., active: _Optional[bool] = ...) -> None: ...
