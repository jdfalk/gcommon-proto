from gcommon.v1.common.enums import health_status_pb2 as _health_status_pb2
from gcommon.v1.common.messages import error_pb2 as _error_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseHealthCheckResponse(_message.Message):
    __slots__ = ("status", "connection_ok", "response_time", "error")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_OK_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: _health_status_pb2.CommonHealthStatus
    connection_ok: bool
    response_time: _duration_pb2.Duration
    error: _error_pb2.Error
    def __init__(self, status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., connection_ok: bool = ..., response_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
