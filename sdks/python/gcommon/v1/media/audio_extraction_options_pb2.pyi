from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AudioExtractionOptions(_message.Message):
    __slots__ = ("output_format", "bitrate", "sample_rate", "normalize_audio")
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    NORMALIZE_AUDIO_FIELD_NUMBER: _ClassVar[int]
    output_format: str
    bitrate: int
    sample_rate: int
    normalize_audio: bool
    def __init__(self, output_format: _Optional[str] = ..., bitrate: _Optional[int] = ..., sample_rate: _Optional[int] = ..., normalize_audio: bool = ...) -> None: ...
