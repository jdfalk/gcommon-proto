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

class DependencyCheck(_message.Message):
    __slots__ = ("id", "dependency_name", "dependency_type", "endpoint", "status", "criticality", "timeout", "check_interval", "last_checked", "configured_at", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CRITICALITY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CHECK_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECKED_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_AT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    dependency_name: str
    dependency_type: str
    endpoint: str
    status: _health_status_pb2.HealthStatus
    criticality: int
    timeout: _duration_pb2.Duration
    check_interval: _duration_pb2.Duration
    last_checked: _timestamp_pb2.Timestamp
    configured_at: _timestamp_pb2.Timestamp
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., dependency_name: _Optional[str] = ..., dependency_type: _Optional[str] = ..., endpoint: _Optional[str] = ..., status: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ..., criticality: _Optional[int] = ..., timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., check_interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., last_checked: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., configured_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
