from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationHealthCheckConfig(_message.Message):
    __slots__ = ("path", "port", "protocol", "interval_seconds", "timeout_seconds", "healthy_threshold", "unhealthy_threshold")
    PATH_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    path: str
    port: int
    protocol: str
    interval_seconds: int
    timeout_seconds: int
    healthy_threshold: int
    unhealthy_threshold: int
    def __init__(self, path: _Optional[str] = ..., port: _Optional[int] = ..., protocol: _Optional[str] = ..., interval_seconds: _Optional[int] = ..., timeout_seconds: _Optional[int] = ..., healthy_threshold: _Optional[int] = ..., unhealthy_threshold: _Optional[int] = ...) -> None: ...
