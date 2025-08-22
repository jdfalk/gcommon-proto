from gcommon.v1.config import config_change_type_pb2 as _config_change_type_pb2
from gcommon.v1.config import config_entry_pb2 as _config_entry_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchConfigResponse(_message.Message):
    __slots__ = ("change_type", "entry", "previous_entry", "timestamp")
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_ENTRY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    change_type: _config_change_type_pb2.ConfigChangeType
    entry: _config_entry_pb2.ConfigEntry
    previous_entry: _config_entry_pb2.ConfigEntry
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, change_type: _Optional[_Union[_config_change_type_pb2.ConfigChangeType, str]] = ..., entry: _Optional[_Union[_config_entry_pb2.ConfigEntry, _Mapping]] = ..., previous_entry: _Optional[_Union[_config_entry_pb2.ConfigEntry, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
