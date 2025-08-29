from gcommon.v1.media import media_quality_pb2 as _media_quality_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

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
