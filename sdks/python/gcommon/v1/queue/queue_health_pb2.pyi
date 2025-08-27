import datetime

from gcommon.v1.common import health_status_pb2 as _health_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueHealth(_message.Message):
    __slots__ = ("queue_name", "status", "health_score", "issues", "last_check")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_SCORE_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECK_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    status: _health_status_pb2.CommonHealthStatus
    health_score: int
    issues: _containers.RepeatedScalarFieldContainer[str]
    last_check: _timestamp_pb2.Timestamp
    def __init__(self, queue_name: _Optional[str] = ..., status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., health_score: _Optional[int] = ..., issues: _Optional[_Iterable[str]] = ..., last_check: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
