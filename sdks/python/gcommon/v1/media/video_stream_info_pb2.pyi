from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

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
