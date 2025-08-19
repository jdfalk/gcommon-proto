from gcommon.v1.common.enums import two_fa_type_pb2 as _two_fa_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Verify2FaRequest(_message.Message):
    __slots__ = ("user_id", "code", "type")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    code: str
    type: _two_fa_type_pb2.AuthTwoFaType
    def __init__(self, user_id: _Optional[str] = ..., code: _Optional[str] = ..., type: _Optional[_Union[_two_fa_type_pb2.AuthTwoFaType, str]] = ...) -> None: ...
