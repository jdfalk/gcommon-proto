from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExtractAudioRequest(_message.Message):
    __slots__ = ("media_file_id", "track_indices", "options")
    MEDIA_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    TRACK_INDICES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    media_file_id: str
    track_indices: _containers.RepeatedScalarFieldContainer[int]
    options: AudioExtractionOptions
    def __init__(self, media_file_id: _Optional[str] = ..., track_indices: _Optional[_Iterable[int]] = ..., options: _Optional[_Union[AudioExtractionOptions, _Mapping]] = ...) -> None: ...

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
    def __init__(self, output_format: _Optional[str] = ..., bitrate: _Optional[int] = ..., sample_rate: _Optional[int] = ..., normalize_audio: _Optional[bool] = ...) -> None: ...
