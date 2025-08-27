import datetime

from gcommon.v1.common import deployment_status_pb2 as _deployment_status_pb2
from gcommon.v1.config import (
    deployment_rollback_info_pb2 as _deployment_rollback_info_pb2,
)
from gcommon.v1.config import health_check_pb2 as _health_check_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentInfo(_message.Message):
    __slots__ = (
        "status",
        "last_deployed_at",
        "version",
        "method",
        "target",
        "config",
        "health_checks",
        "rollback_info",
    )
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_DEPLOYED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECKS_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_INFO_FIELD_NUMBER: _ClassVar[int]
    status: _deployment_status_pb2.DeploymentStatus
    last_deployed_at: _timestamp_pb2.Timestamp
    version: str
    method: str
    target: str
    config: _containers.ScalarMap[str, str]
    health_checks: _containers.RepeatedCompositeFieldContainer[
        _health_check_pb2.HealthCheck
    ]
    rollback_info: _deployment_rollback_info_pb2.DeploymentRollbackInfo
    def __init__(
        self,
        status: _Optional[_Union[_deployment_status_pb2.DeploymentStatus, str]] = ...,
        last_deployed_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        version: _Optional[str] = ...,
        method: _Optional[str] = ...,
        target: _Optional[str] = ...,
        config: _Optional[_Mapping[str, str]] = ...,
        health_checks: _Optional[
            _Iterable[_Union[_health_check_pb2.HealthCheck, _Mapping]]
        ] = ...,
        rollback_info: _Optional[
            _Union[_deployment_rollback_info_pb2.DeploymentRollbackInfo, _Mapping]
        ] = ...,
    ) -> None: ...
