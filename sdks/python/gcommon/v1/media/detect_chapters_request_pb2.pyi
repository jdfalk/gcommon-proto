from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectChaptersRequest(_message.Message):
    __slots__ = ("audio_file_id", "options")
    AUDIO_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    audio_file_id: str
    options: ChapterDetectionOptions
    def __init__(self, audio_file_id: _Optional[str] = ..., options: _Optional[_Union[ChapterDetectionOptions, _Mapping]] = ...) -> None: ...

class ChapterDetectionOptions(_message.Message):
    __slots__ = ("silence_threshold_db", "min_chapter_length_seconds", "use_metadata", "use_ai_detection")
    SILENCE_THRESHOLD_DB_FIELD_NUMBER: _ClassVar[int]
    MIN_CHAPTER_LENGTH_SECONDS_FIELD_NUMBER: _ClassVar[int]
    USE_METADATA_FIELD_NUMBER: _ClassVar[int]
    USE_AI_DETECTION_FIELD_NUMBER: _ClassVar[int]
    silence_threshold_db: float
    min_chapter_length_seconds: float
    use_metadata: bool
    use_ai_detection: bool
    def __init__(self, silence_threshold_db: _Optional[float] = ..., min_chapter_length_seconds: _Optional[float] = ..., use_metadata: bool = ..., use_ai_detection: bool = ...) -> None: ...
