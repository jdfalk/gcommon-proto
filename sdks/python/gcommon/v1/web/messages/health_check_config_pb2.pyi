from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WebHealthCheckConfig(_message.Message):
    __slots__ = ("path", "interval_seconds", "timeout_seconds", "expected_status", "headers", "enabled")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PATH_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_STATUS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    path: str
    interval_seconds: float
    timeout_seconds: float
    expected_status: int
    headers: _containers.ScalarMap[str, str]
    enabled: bool
    def __init__(self, path: _Optional[str] = ..., interval_seconds: _Optional[float] = ..., timeout_seconds: _Optional[float] = ..., expected_status: _Optional[int] = ..., headers: _Optional[_Mapping[str, str]] = ..., enabled: bool = ...) -> None: ...
