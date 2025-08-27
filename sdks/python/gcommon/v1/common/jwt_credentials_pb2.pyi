from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JWTCredentials(_message.Message):
    __slots__ = ("token", "issuer")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    token: str
    issuer: str
    def __init__(
        self, token: _Optional[str] = ..., issuer: _Optional[str] = ...
    ) -> None: ...
