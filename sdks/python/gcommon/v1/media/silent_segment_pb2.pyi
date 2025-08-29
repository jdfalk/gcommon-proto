from gcommon.v1.media import media_quality_pb2 as _media_quality_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SilentSegment(_message.Message):
    __slots__ = ("start_time", "end_time", "threshold_db")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_DB_FIELD_NUMBER: _ClassVar[int]
    start_time: _duration_pb2.Duration
    end_time: _duration_pb2.Duration
    threshold_db: float
    def __init__(self, start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., threshold_db: _Optional[float] = ...) -> None: ...
