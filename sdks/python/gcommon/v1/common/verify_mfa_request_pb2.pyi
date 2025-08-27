from gcommon.v1.common import mfa_method_pb2 as _mfa_method_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyMfaRequest(_message.Message):
    __slots__ = ("user_id", "code", "method", "context")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    code: str
    method: _mfa_method_pb2.MfaMethod
    context: str
    def __init__(self, user_id: _Optional[str] = ..., code: _Optional[str] = ..., method: _Optional[_Union[_mfa_method_pb2.MfaMethod, str]] = ..., context: _Optional[str] = ...) -> None: ...
