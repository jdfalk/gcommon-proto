from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConvertSubtitleFormatResponse(_message.Message):
    __slots__ = ("converted_subtitle_file_id", "success", "error_message", "output_format")
    CONVERTED_SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    converted_subtitle_file_id: str
    success: bool
    error_message: str
    output_format: str
    def __init__(self, converted_subtitle_file_id: _Optional[str] = ..., success: bool = ..., error_message: _Optional[str] = ..., output_format: _Optional[str] = ...) -> None: ...
