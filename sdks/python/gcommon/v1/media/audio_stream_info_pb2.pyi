from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

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
