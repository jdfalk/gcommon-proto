from gcommon.v1.common import formatter_type_pb2 as _formatter_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogFormatterConfig(_message.Message):
    __slots__ = ("type", "pattern")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    type: _formatter_type_pb2.FormatterType
    pattern: str
    def __init__(self, type: _Optional[_Union[_formatter_type_pb2.FormatterType, str]] = ..., pattern: _Optional[str] = ...) -> None: ...
