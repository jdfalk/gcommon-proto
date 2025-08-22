from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncSubtitlesRequest(_message.Message):
    __slots__ = ("subtitle_file_id", "media_file_id", "options")
    SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    subtitle_file_id: str
    media_file_id: str
    options: SyncOptions
    def __init__(self, subtitle_file_id: _Optional[str] = ..., media_file_id: _Optional[str] = ..., options: _Optional[_Union[SyncOptions, _Mapping]] = ...) -> None: ...

class SyncOptions(_message.Message):
    __slots__ = ("offset", "speed_factor", "auto_detect_sync", "sync_points")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SPEED_FACTOR_FIELD_NUMBER: _ClassVar[int]
    AUTO_DETECT_SYNC_FIELD_NUMBER: _ClassVar[int]
    SYNC_POINTS_FIELD_NUMBER: _ClassVar[int]
    offset: _duration_pb2.Duration
    speed_factor: float
    auto_detect_sync: bool
    sync_points: _containers.RepeatedCompositeFieldContainer[SyncPoint]
    def __init__(self, offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., speed_factor: _Optional[float] = ..., auto_detect_sync: bool = ..., sync_points: _Optional[_Iterable[_Union[SyncPoint, _Mapping]]] = ...) -> None: ...

class SyncPoint(_message.Message):
    __slots__ = ("subtitle_time", "media_time")
    SUBTITLE_TIME_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TIME_FIELD_NUMBER: _ClassVar[int]
    subtitle_time: _duration_pb2.Duration
    media_time: _duration_pb2.Duration
    def __init__(self, subtitle_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., media_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
