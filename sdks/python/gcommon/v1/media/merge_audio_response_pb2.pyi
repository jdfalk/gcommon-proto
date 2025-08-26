from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MergeAudioResponse(_message.Message):
    __slots__ = ("merged_audio_file_id",)
    MERGED_AUDIO_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    merged_audio_file_id: str
    def __init__(self, merged_audio_file_id: _Optional[str] = ...) -> None: ...
