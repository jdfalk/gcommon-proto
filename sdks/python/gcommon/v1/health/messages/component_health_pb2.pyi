import datetime

from gcommon.v1.health.enums import health_status_pb2 as _health_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComponentHealth(_message.Message):
    __slots__ = ("component_name", "status", "description", "last_updated", "check_ids", "healthy_checks", "unhealthy_checks", "total_checks", "metadata", "version", "dependencies", "last_restart")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    CHECK_IDS_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHECKS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    LAST_RESTART_FIELD_NUMBER: _ClassVar[int]
    component_name: str
    status: _health_status_pb2.HealthStatus
    description: str
    last_updated: _timestamp_pb2.Timestamp
    check_ids: _containers.RepeatedScalarFieldContainer[str]
    healthy_checks: int
    unhealthy_checks: int
    total_checks: int
    metadata: _containers.ScalarMap[str, str]
    version: str
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    last_restart: _timestamp_pb2.Timestamp
    def __init__(self, component_name: _Optional[str] = ..., status: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ..., description: _Optional[str] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., check_ids: _Optional[_Iterable[str]] = ..., healthy_checks: _Optional[int] = ..., unhealthy_checks: _Optional[int] = ..., total_checks: _Optional[int] = ..., metadata: _Optional[_Mapping[str, str]] = ..., version: _Optional[str] = ..., dependencies: _Optional[_Iterable[str]] = ..., last_restart: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
