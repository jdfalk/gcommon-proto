from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthAuthorizeResponse(_message.Message):
    __slots__ = ("authorized", "permissions", "denial_reason", "error")
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DENIAL_REASON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    authorized: bool
    permissions: _containers.RepeatedScalarFieldContainer[str]
    denial_reason: str
    error: _error_pb2.Error
    def __init__(self, authorized: bool = ..., permissions: _Optional[_Iterable[str]] = ..., denial_reason: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
