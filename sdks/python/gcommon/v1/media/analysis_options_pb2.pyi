from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AnalysisOptions(_message.Message):
    __slots__ = ("extract_metadata", "analyze_quality", "detect_scenes", "extract_thumbnails", "analyze_audio")
    EXTRACT_METADATA_FIELD_NUMBER: _ClassVar[int]
    ANALYZE_QUALITY_FIELD_NUMBER: _ClassVar[int]
    DETECT_SCENES_FIELD_NUMBER: _ClassVar[int]
    EXTRACT_THUMBNAILS_FIELD_NUMBER: _ClassVar[int]
    ANALYZE_AUDIO_FIELD_NUMBER: _ClassVar[int]
    extract_metadata: bool
    analyze_quality: bool
    detect_scenes: bool
    extract_thumbnails: bool
    analyze_audio: bool
    def __init__(self, extract_metadata: bool = ..., analyze_quality: bool = ..., detect_scenes: bool = ..., extract_thumbnails: bool = ..., analyze_audio: bool = ...) -> None: ...
