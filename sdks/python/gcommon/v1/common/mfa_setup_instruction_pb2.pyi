from gcommon.v1.common import mfa_method_pb2 as _mfa_method_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MfaSetupInstruction(_message.Message):
    __slots__ = ("method", "instruction", "qr_code", "secret_key")
    METHOD_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    QR_CODE_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    method: _mfa_method_pb2.MfaMethod
    instruction: str
    qr_code: str
    secret_key: str
    def __init__(
        self,
        method: _Optional[_Union[_mfa_method_pb2.MfaMethod, str]] = ...,
        instruction: _Optional[str] = ...,
        qr_code: _Optional[str] = ...,
        secret_key: _Optional[str] = ...,
    ) -> None: ...
