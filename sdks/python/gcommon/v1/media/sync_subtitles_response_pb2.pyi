from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncSubtitlesResponse(_message.Message):
    __slots__ = ("synced_subtitle_file_id", "statistics")
    SYNCED_SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    synced_subtitle_file_id: str
    statistics: SyncStatistics
    def __init__(self, synced_subtitle_file_id: _Optional[str] = ..., statistics: _Optional[_Union[SyncStatistics, _Mapping]] = ...) -> None: ...

class SyncStatistics(_message.Message):
    __slots__ = ("applied_offset", "applied_speed_factor", "adjustments_made", "confidence_score")
    APPLIED_OFFSET_FIELD_NUMBER: _ClassVar[int]
    APPLIED_SPEED_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENTS_MADE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    applied_offset: _duration_pb2.Duration
    applied_speed_factor: float
    adjustments_made: int
    confidence_score: float
    def __init__(self, applied_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., applied_speed_factor: _Optional[float] = ..., adjustments_made: _Optional[int] = ..., confidence_score: _Optional[float] = ...) -> None: ...
