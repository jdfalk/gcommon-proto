from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnalyzeMediaRequest(_message.Message):
    __slots__ = ("media_file_id", "options")
    MEDIA_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    media_file_id: str
    options: AnalysisOptions
    def __init__(self, media_file_id: _Optional[str] = ..., options: _Optional[_Union[AnalysisOptions, _Mapping]] = ...) -> None: ...

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
    def __init__(self, extract_metadata: _Optional[bool] = ..., analyze_quality: _Optional[bool] = ..., detect_scenes: _Optional[bool] = ..., extract_thumbnails: _Optional[bool] = ..., analyze_audio: _Optional[bool] = ...) -> None: ...
