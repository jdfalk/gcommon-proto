from gcommon.v1.common import mfa_method_pb2 as _mfa_method_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisableMfaRequest(_message.Message):
    __slots__ = ("user_id", "password", "verification_code", "methods")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    password: str
    verification_code: str
    methods: _containers.RepeatedScalarFieldContainer[_mfa_method_pb2.MfaMethod]
    def __init__(self, user_id: _Optional[str] = ..., password: _Optional[str] = ..., verification_code: _Optional[str] = ..., methods: _Optional[_Iterable[_Union[_mfa_method_pb2.MfaMethod, str]]] = ...) -> None: ...
