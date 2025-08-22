from gcommon.v1.media.messages import media_quality_pb2 as _media_quality_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaAnalysis(_message.Message):
    __slots__ = ("technical", "quality_analysis", "scenes", "thumbnails", "audio_analysis")
    TECHNICAL_FIELD_NUMBER: _ClassVar[int]
    QUALITY_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    SCENES_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    technical: TechnicalMetadata
    quality_analysis: _media_quality_pb2.MediaQuality
    scenes: _containers.RepeatedCompositeFieldContainer[SceneDetection]
    thumbnails: _containers.RepeatedCompositeFieldContainer[ThumbnailInfo]
    audio_analysis: AudioAnalysis
    def __init__(self, technical: _Optional[_Union[TechnicalMetadata, _Mapping]] = ..., quality_analysis: _Optional[_Union[_media_quality_pb2.MediaQuality, _Mapping]] = ..., scenes: _Optional[_Iterable[_Union[SceneDetection, _Mapping]]] = ..., thumbnails: _Optional[_Iterable[_Union[ThumbnailInfo, _Mapping]]] = ..., audio_analysis: _Optional[_Union[AudioAnalysis, _Mapping]] = ...) -> None: ...

class TechnicalMetadata(_message.Message):
    __slots__ = ("duration", "file_size", "bitrate", "container_format", "video", "audio_streams", "subtitle_streams")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FORMAT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_STREAMS_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_STREAMS_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    file_size: int
    bitrate: int
    container_format: str
    video: VideoStreamInfo
    audio_streams: _containers.RepeatedCompositeFieldContainer[AudioStreamInfo]
    subtitle_streams: _containers.RepeatedCompositeFieldContainer[SubtitleStreamInfo]
    def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., file_size: _Optional[int] = ..., bitrate: _Optional[int] = ..., container_format: _Optional[str] = ..., video: _Optional[_Union[VideoStreamInfo, _Mapping]] = ..., audio_streams: _Optional[_Iterable[_Union[AudioStreamInfo, _Mapping]]] = ..., subtitle_streams: _Optional[_Iterable[_Union[SubtitleStreamInfo, _Mapping]]] = ...) -> None: ...

class VideoStreamInfo(_message.Message):
    __slots__ = ("codec", "width", "height", "frame_rate", "bitrate", "pixel_format", "color_space")
    CODEC_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    PIXEL_FORMAT_FIELD_NUMBER: _ClassVar[int]
    COLOR_SPACE_FIELD_NUMBER: _ClassVar[int]
    codec: str
    width: int
    height: int
    frame_rate: float
    bitrate: int
    pixel_format: str
    color_space: str
    def __init__(self, codec: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., frame_rate: _Optional[float] = ..., bitrate: _Optional[int] = ..., pixel_format: _Optional[str] = ..., color_space: _Optional[str] = ...) -> None: ...

class AudioStreamInfo(_message.Message):
    __slots__ = ("stream_index", "codec", "sample_rate", "channels", "bitrate", "language", "title")
    STREAM_INDEX_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    stream_index: int
    codec: str
    sample_rate: int
    channels: int
    bitrate: int
    language: str
    title: str
    def __init__(self, stream_index: _Optional[int] = ..., codec: _Optional[str] = ..., sample_rate: _Optional[int] = ..., channels: _Optional[int] = ..., bitrate: _Optional[int] = ..., language: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class SubtitleStreamInfo(_message.Message):
    __slots__ = ("stream_index", "codec", "language", "title", "forced", "hearing_impaired")
    STREAM_INDEX_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FORCED_FIELD_NUMBER: _ClassVar[int]
    HEARING_IMPAIRED_FIELD_NUMBER: _ClassVar[int]
    stream_index: int
    codec: str
    language: str
    title: str
    forced: bool
    hearing_impaired: bool
    def __init__(self, stream_index: _Optional[int] = ..., codec: _Optional[str] = ..., language: _Optional[str] = ..., title: _Optional[str] = ..., forced: bool = ..., hearing_impaired: bool = ...) -> None: ...

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
    def __init__(self, start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., confidence: _Optional[float] = ..., scene_type: _Optional[str] = ...) -> None: ...

class ThumbnailInfo(_message.Message):
    __slots__ = ("timestamp", "file_path", "width", "height")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    timestamp: _duration_pb2.Duration
    file_path: str
    width: int
    height: int
    def __init__(self, timestamp: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., file_path: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class AudioAnalysis(_message.Message):
    __slots__ = ("peak_level", "rms_level", "silent_segments", "dynamic_range")
    PEAK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RMS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SILENT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_RANGE_FIELD_NUMBER: _ClassVar[int]
    peak_level: float
    rms_level: float
    silent_segments: _containers.RepeatedCompositeFieldContainer[SilentSegment]
    dynamic_range: float
    def __init__(self, peak_level: _Optional[float] = ..., rms_level: _Optional[float] = ..., silent_segments: _Optional[_Iterable[_Union[SilentSegment, _Mapping]]] = ..., dynamic_range: _Optional[float] = ...) -> None: ...

class SilentSegment(_message.Message):
    __slots__ = ("start_time", "end_time", "threshold_db")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_DB_FIELD_NUMBER: _ClassVar[int]
    start_time: _duration_pb2.Duration
    end_time: _duration_pb2.Duration
    threshold_db: float
    def __init__(self, start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., threshold_db: _Optional[float] = ...) -> None: ...
