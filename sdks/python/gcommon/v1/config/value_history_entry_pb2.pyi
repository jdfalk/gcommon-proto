from gcommon.v1.common import config_change_type_pb2 as _config_change_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValueHistoryEntry(_message.Message):
    __slots__ = ("entry_id", "previous_value", "new_value", "timestamp", "changed_by", "reason", "change_type", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CHANGED_BY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    previous_value: str
    new_value: str
    timestamp: _timestamp_pb2.Timestamp
    changed_by: str
    reason: str
    change_type: _config_change_type_pb2.TemplateChangeType
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, entry_id: _Optional[str] = ..., previous_value: _Optional[str] = ..., new_value: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., changed_by: _Optional[str] = ..., reason: _Optional[str] = ..., change_type: _Optional[_Union[_config_change_type_pb2.TemplateChangeType, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
