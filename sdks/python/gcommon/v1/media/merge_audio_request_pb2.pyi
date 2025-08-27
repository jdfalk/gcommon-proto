from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MergeAudioRequest(_message.Message):
    __slots__ = ("audio_file_ids", "output_format")
    AUDIO_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    audio_file_ids: _containers.RepeatedScalarFieldContainer[str]
    output_format: str
    def __init__(self, audio_file_ids: _Optional[_Iterable[str]] = ..., output_format: _Optional[str] = ...) -> None: ...
