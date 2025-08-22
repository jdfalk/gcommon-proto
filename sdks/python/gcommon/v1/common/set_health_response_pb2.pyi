from gcommon.v1.common import health_status_pb2 as _health_status_pb2
from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetHealthResponse(_message.Message):
    __slots__ = ("success", "previous_status", "new_status", "changed_at", "error", "reason")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATUS_FIELD_NUMBER: _ClassVar[int]
    NEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    CHANGED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    success: bool
    previous_status: _health_status_pb2.CommonHealthStatus
    new_status: _health_status_pb2.CommonHealthStatus
    changed_at: _timestamp_pb2.Timestamp
    error: _error_pb2.Error
    reason: str
    def __init__(self, success: bool = ..., previous_status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., new_status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., changed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...
