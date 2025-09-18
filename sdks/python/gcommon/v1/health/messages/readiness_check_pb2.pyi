import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadinessCheck(_message.Message):
    __slots__ = ("id", "service_name", "dependencies", "min_health_score", "max_response_time", "startup_grace_period", "updated_at", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    MIN_HEALTH_SCORE_FIELD_NUMBER: _ClassVar[int]
    MAX_RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    STARTUP_GRACE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    service_name: str
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    min_health_score: int
    max_response_time: _duration_pb2.Duration
    startup_grace_period: _duration_pb2.Duration
    updated_at: _timestamp_pb2.Timestamp
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., service_name: _Optional[str] = ..., dependencies: _Optional[_Iterable[str]] = ..., min_health_score: _Optional[int] = ..., max_response_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., startup_grace_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., enabled: _Optional[bool] = ...) -> None: ...
