from gcommon.v1.health.messages import health_result_pb2 as _health_result_pb2
from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthCheckResponse(_message.Message):
    __slots__ = ("results", "summary", "total_checks", "healthy_checks", "unhealthy_checks", "metadata", "all_checks_completed", "warnings")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHECKS_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ALL_CHECKS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_health_result_pb2.HealthResult]
    summary: str
    total_checks: int
    healthy_checks: int
    unhealthy_checks: int
    metadata: _response_metadata_pb2.ResponseMetadata
    all_checks_completed: bool
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, results: _Optional[_Iterable[_Union[_health_result_pb2.HealthResult, _Mapping]]] = ..., summary: _Optional[str] = ..., total_checks: _Optional[int] = ..., healthy_checks: _Optional[int] = ..., unhealthy_checks: _Optional[int] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ..., all_checks_completed: _Optional[bool] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...
