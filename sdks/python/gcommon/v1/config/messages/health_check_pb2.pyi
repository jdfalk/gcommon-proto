from gcommon.v1.config.enums import health_check_type_pb2 as _health_check_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthCheck(_message.Message):
    __slots__ = ("name", "type", "endpoint", "interval_seconds", "timeout_seconds", "retries", "conditions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    RETRIES_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _health_check_type_pb2.HealthCheckType
    endpoint: str
    interval_seconds: int
    timeout_seconds: int
    retries: int
    conditions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_health_check_type_pb2.HealthCheckType, str]] = ..., endpoint: _Optional[str] = ..., interval_seconds: _Optional[int] = ..., timeout_seconds: _Optional[int] = ..., retries: _Optional[int] = ..., conditions: _Optional[_Iterable[str]] = ...) -> None: ...
