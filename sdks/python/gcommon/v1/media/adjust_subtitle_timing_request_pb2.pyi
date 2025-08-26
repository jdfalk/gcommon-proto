from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AdjustSubtitleTimingRequest(_message.Message):
    __slots__ = ("subtitle_file_id", "time_offset_ms", "preserve_duration")
    SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_DURATION_FIELD_NUMBER: _ClassVar[int]
    subtitle_file_id: str
    time_offset_ms: int
    preserve_duration: bool
    def __init__(self, subtitle_file_id: _Optional[str] = ..., time_offset_ms: _Optional[int] = ..., preserve_duration: _Optional[bool] = ...) -> None: ...
