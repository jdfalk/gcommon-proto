from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TranscodeOptions(_message.Message):
    __slots__ = (
        "resolution",
        "bitrate",
        "framerate",
        "audio_codec",
        "audio_bitrate",
        "preserve_subtitles",
        "preserve_chapters",
    )
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    FRAMERATE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CODEC_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BITRATE_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_SUBTITLES_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_CHAPTERS_FIELD_NUMBER: _ClassVar[int]
    resolution: str
    bitrate: int
    framerate: int
    audio_codec: str
    audio_bitrate: int
    preserve_subtitles: bool
    preserve_chapters: bool
    def __init__(
        self,
        resolution: _Optional[str] = ...,
        bitrate: _Optional[int] = ...,
        framerate: _Optional[int] = ...,
        audio_codec: _Optional[str] = ...,
        audio_bitrate: _Optional[int] = ...,
        preserve_subtitles: _Optional[bool] = ...,
        preserve_chapters: _Optional[bool] = ...,
    ) -> None: ...
