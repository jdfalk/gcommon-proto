from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.media import normalization_options_pb2 as _normalization_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NormalizeAudioRequest(_message.Message):
    __slots__ = ("audio_file_id", "options")
    AUDIO_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    audio_file_id: str
    options: _normalization_options_pb2.NormalizationOptions
    def __init__(self, audio_file_id: _Optional[str] = ..., options: _Optional[_Union[_normalization_options_pb2.NormalizationOptions, _Mapping]] = ...) -> None: ...
