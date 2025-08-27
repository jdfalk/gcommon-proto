from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AudioTrack(_message.Message):
    __slots__ = (
        "index",
        "language",
        "codec",
        "title",
        "channels",
        "sample_rate",
        "default_track",
    )
    INDEX_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TRACK_FIELD_NUMBER: _ClassVar[int]
    index: int
    language: str
    codec: str
    title: str
    channels: int
    sample_rate: int
    default_track: bool
    def __init__(
        self,
        index: _Optional[int] = ...,
        language: _Optional[str] = ...,
        codec: _Optional[str] = ...,
        title: _Optional[str] = ...,
        channels: _Optional[int] = ...,
        sample_rate: _Optional[int] = ...,
        default_track: _Optional[bool] = ...,
    ) -> None: ...
