import datetime

from gcommon.v1.common import version_deployment_status_pb2 as _version_deployment_status_pb2
from gcommon.v1.common import version_health_status_pb2 as _version_health_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VersionDeploymentInfo(_message.Message):
    __slots__ = ("status", "deployed_at", "environment", "method", "deployed_by", "config", "artifacts", "health", "metrics")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_AT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_BY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    status: _version_deployment_status_pb2.VersionDeploymentStatus
    deployed_at: _timestamp_pb2.Timestamp
    environment: str
    method: str
    deployed_by: str
    config: _containers.ScalarMap[str, str]
    artifacts: _containers.RepeatedScalarFieldContainer[str]
    health: _version_health_status_pb2.VersionHealthStatus
    metrics: _containers.ScalarMap[str, float]
    def __init__(self, status: _Optional[_Union[_version_deployment_status_pb2.VersionDeploymentStatus, str]] = ..., deployed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., environment: _Optional[str] = ..., method: _Optional[str] = ..., deployed_by: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ..., artifacts: _Optional[_Iterable[str]] = ..., health: _Optional[_Union[_version_health_status_pb2.VersionHealthStatus, str]] = ..., metrics: _Optional[_Mapping[str, float]] = ...) -> None: ...
