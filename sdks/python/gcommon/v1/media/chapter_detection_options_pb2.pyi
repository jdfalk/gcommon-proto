from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

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
