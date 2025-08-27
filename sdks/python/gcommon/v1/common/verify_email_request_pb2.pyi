from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyEmailRequest(_message.Message):
    __slots__ = ("identifier", "verification_token")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    verification_token: str
    def __init__(
        self, identifier: _Optional[str] = ..., verification_token: _Optional[str] = ...
    ) -> None: ...
