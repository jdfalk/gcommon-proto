from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SyncSubtitlesRequest(_message.Message):
    __slots__ = ("subtitle_file_id", "media_file_id", "auto_detect_timing", "sync_points_ms")
    SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_DETECT_TIMING_FIELD_NUMBER: _ClassVar[int]
    SYNC_POINTS_MS_FIELD_NUMBER: _ClassVar[int]
    subtitle_file_id: str
    media_file_id: str
    auto_detect_timing: bool
    sync_points_ms: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, subtitle_file_id: _Optional[str] = ..., media_file_id: _Optional[str] = ..., auto_detect_timing: _Optional[bool] = ..., sync_points_ms: _Optional[_Iterable[int]] = ...) -> None: ...
