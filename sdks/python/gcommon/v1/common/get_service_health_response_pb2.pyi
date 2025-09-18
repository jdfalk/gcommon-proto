import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import health_status_pb2 as _health_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetServiceHealthResponse(_message.Message):
    __slots__ = ("status", "last_check", "error")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECK_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: _health_status_pb2.CommonHealthStatus
    last_check: _timestamp_pb2.Timestamp
    error: _error_pb2.Error
    def __init__(self, status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., last_check: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
