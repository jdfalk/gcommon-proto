from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecurityPolicy(_message.Message):
    __slots__ = ("min_password_length", "password_ttl", "max_failed_attempts")
    MIN_PASSWORD_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_TTL_FIELD_NUMBER: _ClassVar[int]
    MAX_FAILED_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    min_password_length: int
    password_ttl: _duration_pb2.Duration
    max_failed_attempts: int
    def __init__(self, min_password_length: _Optional[int] = ..., password_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_failed_attempts: _Optional[int] = ...) -> None: ...
