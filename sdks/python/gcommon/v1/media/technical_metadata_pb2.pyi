from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.media import audio_stream_info_pb2 as _audio_stream_info_pb2
from gcommon.v1.media import subtitle_stream_info_pb2 as _subtitle_stream_info_pb2
from gcommon.v1.media import video_stream_info_pb2 as _video_stream_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
    video: _video_stream_info_pb2.VideoStreamInfo
    audio_streams: _containers.RepeatedCompositeFieldContainer[_audio_stream_info_pb2.AudioStreamInfo]
    subtitle_streams: _containers.RepeatedCompositeFieldContainer[_subtitle_stream_info_pb2.SubtitleStreamInfo]
    def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., file_size: _Optional[int] = ..., bitrate: _Optional[int] = ..., container_format: _Optional[str] = ..., video: _Optional[_Union[_video_stream_info_pb2.VideoStreamInfo, _Mapping]] = ..., audio_streams: _Optional[_Iterable[_Union[_audio_stream_info_pb2.AudioStreamInfo, _Mapping]]] = ..., subtitle_streams: _Optional[_Iterable[_Union[_subtitle_stream_info_pb2.SubtitleStreamInfo, _Mapping]]] = ...) -> None: ...
