import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LivenessCheck(_message.Message):
    __slots__ = ("id", "service_name", "probe_endpoint", "interval", "timeout", "failure_threshold", "initial_delay", "created_at", "active")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROBE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    service_name: str
    probe_endpoint: str
    interval: _duration_pb2.Duration
    timeout: _duration_pb2.Duration
    failure_threshold: int
    initial_delay: _duration_pb2.Duration
    created_at: _timestamp_pb2.Timestamp
    active: bool
    def __init__(self, id: _Optional[str] = ..., service_name: _Optional[str] = ..., probe_endpoint: _Optional[str] = ..., interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., failure_threshold: _Optional[int] = ..., initial_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., active: _Optional[bool] = ...) -> None: ...
