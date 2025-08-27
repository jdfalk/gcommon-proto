import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebTimeoutConfig(_message.Message):
    __slots__ = ("read_timeout", "write_timeout", "idle_timeout", "request_timeout", "shutdown_timeout")
    READ_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    WRITE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    read_timeout: _duration_pb2.Duration
    write_timeout: _duration_pb2.Duration
    idle_timeout: _duration_pb2.Duration
    request_timeout: _duration_pb2.Duration
    shutdown_timeout: _duration_pb2.Duration
    def __init__(self, read_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., write_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., idle_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., request_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., shutdown_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
