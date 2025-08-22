from gcommon.v1.common import health_status_pb2 as _health_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsHealthInfo(_message.Message):
    __slots__ = ("overall_status", "health_checks", "warnings", "last_check")
    OVERALL_STATUS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECKS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECK_FIELD_NUMBER: _ClassVar[int]
    overall_status: _health_status_pb2.CommonHealthStatus
    health_checks: _containers.RepeatedScalarFieldContainer[str]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    last_check: _timestamp_pb2.Timestamp
    def __init__(self, overall_status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., health_checks: _Optional[_Iterable[str]] = ..., warnings: _Optional[_Iterable[str]] = ..., last_check: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
