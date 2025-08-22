from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AdjustSubtitleTimingResponse(_message.Message):
    __slots__ = ("adjusted_subtitle_file_id", "entries_modified")
    ADJUSTED_SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    adjusted_subtitle_file_id: str
    entries_modified: int
    def __init__(self, adjusted_subtitle_file_id: _Optional[str] = ..., entries_modified: _Optional[int] = ...) -> None: ...
