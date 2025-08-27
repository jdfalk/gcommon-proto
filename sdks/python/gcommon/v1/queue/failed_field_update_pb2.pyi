from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FailedFieldUpdate(_message.Message):
    __slots__ = ("field_name", "failure_reason", "error_code", "original_value", "attempted_value")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    failure_reason: str
    error_code: str
    original_value: str
    attempted_value: str
    def __init__(self, field_name: _Optional[str] = ..., failure_reason: _Optional[str] = ..., error_code: _Optional[str] = ..., original_value: _Optional[str] = ..., attempted_value: _Optional[str] = ...) -> None: ...
