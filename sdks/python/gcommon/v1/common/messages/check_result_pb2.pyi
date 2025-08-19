from gcommon.v1.common.enums import health_status_pb2 as _health_status_pb2
from gcommon.v1.common.messages import error_pb2 as _error_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckResult(_message.Message):
    __slots__ = ("name", "status", "timestamp", "execution_time", "message", "error", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: _health_status_pb2.CommonHealthStatus
    timestamp: _timestamp_pb2.Timestamp
    execution_time: _duration_pb2.Duration
    message: str
    error: _error_pb2.Error
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., execution_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., message: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
