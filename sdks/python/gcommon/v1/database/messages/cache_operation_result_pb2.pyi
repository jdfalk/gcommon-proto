from gcommon.v1.common.messages import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheOperationResult(_message.Message):
    __slots__ = ("success", "operation_type", "key", "namespace", "duration_microseconds", "timestamp", "items_affected", "error", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    DURATION_MICROSECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ITEMS_AFFECTED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    operation_type: str
    key: str
    namespace: str
    duration_microseconds: int
    timestamp: _timestamp_pb2.Timestamp
    items_affected: int
    error: _error_pb2.Error
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, success: bool = ..., operation_type: _Optional[str] = ..., key: _Optional[str] = ..., namespace: _Optional[str] = ..., duration_microseconds: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., items_affected: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
