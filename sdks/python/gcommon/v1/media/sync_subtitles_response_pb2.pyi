from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SyncSubtitlesResponse(_message.Message):
    __slots__ = ("synchronized_subtitle_file_id", "success", "error_message", "adjustments_made")
    SYNCHRONIZED_SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENTS_MADE_FIELD_NUMBER: _ClassVar[int]
    synchronized_subtitle_file_id: str
    success: bool
    error_message: str
    adjustments_made: int
    def __init__(self, synchronized_subtitle_file_id: _Optional[str] = ..., success: bool = ..., error_message: _Optional[str] = ..., adjustments_made: _Optional[int] = ...) -> None: ...
