from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdjustSubtitleTimingRequest(_message.Message):
    __slots__ = ("subtitle_file_id", "adjustment")
    SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    subtitle_file_id: str
    adjustment: TimingAdjustment
    def __init__(self, subtitle_file_id: _Optional[str] = ..., adjustment: _Optional[_Union[TimingAdjustment, _Mapping]] = ...) -> None: ...

class TimingAdjustment(_message.Message):
    __slots__ = ("offset", "speed_factor", "start_time", "end_time")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SPEED_FACTOR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    offset: _duration_pb2.Duration
    speed_factor: float
    start_time: _duration_pb2.Duration
    end_time: _duration_pb2.Duration
    def __init__(self, offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., speed_factor: _Optional[float] = ..., start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
