from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import health_status_pb2 as _health_status_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunCheckResponse(_message.Message):
    __slots__ = ("success", "check_id", "status", "executed_at", "execution_time", "message", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_AT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    check_id: str
    status: _health_status_pb2.CommonHealthStatus
    executed_at: _timestamp_pb2.Timestamp
    execution_time: _duration_pb2.Duration
    message: str
    error: _error_pb2.Error
    def __init__(self, success: bool = ..., check_id: _Optional[str] = ..., status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., executed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., execution_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., message: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
