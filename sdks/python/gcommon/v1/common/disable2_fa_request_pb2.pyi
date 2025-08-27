from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Disable2FaRequest(_message.Message):
    __slots__ = ("user_id", "password", "verification_code")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    password: str
    verification_code: str
    def __init__(
        self,
        user_id: _Optional[str] = ...,
        password: _Optional[str] = ...,
        verification_code: _Optional[str] = ...,
    ) -> None: ...
