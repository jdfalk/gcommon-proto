from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ContentFilter(_message.Message):
    __slots__ = ("field_path", "operator", "value", "case_sensitive")
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    field_path: str
    operator: str
    value: str
    case_sensitive: bool
    def __init__(self, field_path: _Optional[str] = ..., operator: _Optional[str] = ..., value: _Optional[str] = ..., case_sensitive: bool = ...) -> None: ...
