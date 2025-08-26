from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigConfigChange(_message.Message):
    __slots__ = ("change_id", "key", "old_value", "new_value", "change_type", "timestamp", "changed_by", "reason", "namespace", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CHANGED_BY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    change_id: str
    key: str
    old_value: _any_pb2.Any
    new_value: _any_pb2.Any
    change_type: str
    timestamp: _timestamp_pb2.Timestamp
    changed_by: str
    reason: str
    namespace: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, change_id: _Optional[str] = ..., key: _Optional[str] = ..., old_value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., new_value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., change_type: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., changed_by: _Optional[str] = ..., reason: _Optional[str] = ..., namespace: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
