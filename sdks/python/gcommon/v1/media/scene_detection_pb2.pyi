import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneDetection(_message.Message):
    __slots__ = ("start_time", "end_time", "confidence", "scene_type")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    SCENE_TYPE_FIELD_NUMBER: _ClassVar[int]
    start_time: _duration_pb2.Duration
    end_time: _duration_pb2.Duration
    confidence: float
    scene_type: str
    def __init__(self, start_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., end_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., confidence: _Optional[float] = ..., scene_type: _Optional[str] = ...) -> None: ...
