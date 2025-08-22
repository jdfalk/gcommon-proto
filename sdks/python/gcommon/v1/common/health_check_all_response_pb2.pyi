from gcommon.v1.common import health_check_result_pb2 as _health_check_result_pb2
from gcommon.v1.common import serving_status_pb2 as _serving_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthCheckAllResponse(_message.Message):
    __slots__ = ("overall_status", "results", "total_services", "healthy_services", "unhealthy_services", "total_duration_ms", "timestamp")
    OVERALL_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SERVICES_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_SERVICES_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_SERVICES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    overall_status: _serving_status_pb2.ServingStatus
    results: _containers.RepeatedCompositeFieldContainer[_health_check_result_pb2.HealthHealthCheckResult]
    total_services: int
    healthy_services: int
    unhealthy_services: int
    total_duration_ms: int
    timestamp: int
    def __init__(self, overall_status: _Optional[_Union[_serving_status_pb2.ServingStatus, str]] = ..., results: _Optional[_Iterable[_Union[_health_check_result_pb2.HealthHealthCheckResult, _Mapping]]] = ..., total_services: _Optional[int] = ..., healthy_services: _Optional[int] = ..., unhealthy_services: _Optional[int] = ..., total_duration_ms: _Optional[int] = ..., timestamp: _Optional[int] = ...) -> None: ...
