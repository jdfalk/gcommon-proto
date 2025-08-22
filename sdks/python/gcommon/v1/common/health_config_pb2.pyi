from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HealthConfig(_message.Message):
    __slots__ = ("enabled", "endpoint", "liveness_path", "readiness_path", "startup_path", "timeout_seconds", "interval_seconds", "grace_period_seconds", "retries")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_PATH_FIELD_NUMBER: _ClassVar[int]
    READINESS_PATH_FIELD_NUMBER: _ClassVar[int]
    STARTUP_PATH_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    GRACE_PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    RETRIES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    endpoint: str
    liveness_path: str
    readiness_path: str
    startup_path: str
    timeout_seconds: int
    interval_seconds: int
    grace_period_seconds: int
    retries: int
    def __init__(self, enabled: bool = ..., endpoint: _Optional[str] = ..., liveness_path: _Optional[str] = ..., readiness_path: _Optional[str] = ..., startup_path: _Optional[str] = ..., timeout_seconds: _Optional[int] = ..., interval_seconds: _Optional[int] = ..., grace_period_seconds: _Optional[int] = ..., retries: _Optional[int] = ...) -> None: ...
