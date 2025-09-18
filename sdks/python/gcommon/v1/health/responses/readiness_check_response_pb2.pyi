from gcommon.v1.health.enums import health_status_pb2 as _health_status_pb2
from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadinessCheckResponse(_message.Message):
    __slots__ = ("status", "ready", "reason", "health_score", "dependency_status", "metadata", "details")
    class DependencyStatusEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _health_status_pb2.HealthStatus
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ...) -> None: ...
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    HEALTH_SCORE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    status: _health_status_pb2.HealthStatus
    ready: bool
    reason: str
    health_score: int
    dependency_status: _containers.ScalarMap[str, _health_status_pb2.HealthStatus]
    metadata: _response_metadata_pb2.ResponseMetadata
    details: _containers.ScalarMap[str, str]
    def __init__(self, status: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ..., ready: _Optional[bool] = ..., reason: _Optional[str] = ..., health_score: _Optional[int] = ..., dependency_status: _Optional[_Mapping[str, _health_status_pb2.HealthStatus]] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ..., details: _Optional[_Mapping[str, str]] = ...) -> None: ...
