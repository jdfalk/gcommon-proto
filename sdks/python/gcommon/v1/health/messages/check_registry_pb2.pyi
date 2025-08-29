from gcommon.v1.health.messages import health_check_pb2 as _health_check_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckRegistry(_message.Message):
    __slots__ = ("checks", "total_checks", "enabled_checks", "last_updated", "version", "monitored_services")
    class ChecksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _health_check_pb2.HealthCheck
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_health_check_pb2.HealthCheck, _Mapping]] = ...) -> None: ...
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHECKS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_CHECKS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MONITORED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    checks: _containers.MessageMap[str, _health_check_pb2.HealthCheck]
    total_checks: int
    enabled_checks: int
    last_updated: _timestamp_pb2.Timestamp
    version: int
    monitored_services: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, checks: _Optional[_Mapping[str, _health_check_pb2.HealthCheck]] = ..., total_checks: _Optional[int] = ..., enabled_checks: _Optional[int] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ..., monitored_services: _Optional[_Iterable[str]] = ...) -> None: ...
