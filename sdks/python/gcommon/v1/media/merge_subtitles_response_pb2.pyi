from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MergeSubtitlesResponse(_message.Message):
    __slots__ = ("merged_subtitle_file_id", "success", "error_message")
    MERGED_SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    merged_subtitle_file_id: str
    success: bool
    error_message: str
    def __init__(self, merged_subtitle_file_id: _Optional[str] = ..., success: _Optional[bool] = ..., error_message: _Optional[str] = ...) -> None: ...
