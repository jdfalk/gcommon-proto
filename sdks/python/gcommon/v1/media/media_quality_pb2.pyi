from gcommon.v1.media import quality_score_pb2 as _quality_score_pb2
from gcommon.v1.media import resolution_pb2 as _resolution_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaQuality(_message.Message):
    __slots__ = ("resolution", "video_codec", "bitrate_kbps", "duration_seconds", "quality_score")
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CODEC_FIELD_NUMBER: _ClassVar[int]
    BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    resolution: _resolution_pb2.Resolution
    video_codec: str
    bitrate_kbps: int
    duration_seconds: float
    quality_score: _quality_score_pb2.QualityScore
    def __init__(self, resolution: _Optional[_Union[_resolution_pb2.Resolution, str]] = ..., video_codec: _Optional[str] = ..., bitrate_kbps: _Optional[int] = ..., duration_seconds: _Optional[float] = ..., quality_score: _Optional[_Union[_quality_score_pb2.QualityScore, str]] = ...) -> None: ...
