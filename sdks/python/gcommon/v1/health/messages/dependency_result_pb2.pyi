import datetime

from gcommon.v1.health.enums import health_status_pb2 as _health_status_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DependencyResult(_message.Message):
    __slots__ = ("check_id", "dependency_name", "status", "checked_at", "duration", "error_message", "response_time", "reachable", "details")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    REACHABLE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    check_id: str
    dependency_name: str
    status: _health_status_pb2.HealthStatus
    checked_at: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    error_message: str
    response_time: _duration_pb2.Duration
    reachable: bool
    details: _containers.ScalarMap[str, str]
    def __init__(self, check_id: _Optional[str] = ..., dependency_name: _Optional[str] = ..., status: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ..., checked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., error_message: _Optional[str] = ..., response_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., reachable: _Optional[bool] = ..., details: _Optional[_Mapping[str, str]] = ...) -> None: ...
