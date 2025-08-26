import datetime

from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigWatchEvent(_message.Message):
    __slots__ = ("watch_id", "key", "old_value", "new_value", "change_type", "timestamp", "namespace", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WATCH_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    watch_id: str
    key: str
    old_value: _any_pb2.Any
    new_value: _any_pb2.Any
    change_type: str
    timestamp: _timestamp_pb2.Timestamp
    namespace: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, watch_id: _Optional[str] = ..., key: _Optional[str] = ..., old_value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., new_value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., change_type: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., namespace: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
