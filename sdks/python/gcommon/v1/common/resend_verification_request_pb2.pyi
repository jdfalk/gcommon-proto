from gcommon.v1.common import verification_type_pb2 as _verification_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResendVerificationRequest(_message.Message):
    __slots__ = ("identifier", "type")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    type: _verification_type_pb2.AuthVerificationType
    def __init__(self, identifier: _Optional[str] = ..., type: _Optional[_Union[_verification_type_pb2.AuthVerificationType, str]] = ...) -> None: ...
