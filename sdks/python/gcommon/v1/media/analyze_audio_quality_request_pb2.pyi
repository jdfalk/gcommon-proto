from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AnalyzeAudioQualityRequest(_message.Message):
    __slots__ = ("audio_file_id",)
    AUDIO_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    audio_file_id: str
    def __init__(self, audio_file_id: _Optional[str] = ...) -> None: ...
