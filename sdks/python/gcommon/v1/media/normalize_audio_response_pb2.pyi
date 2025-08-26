from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NormalizeAudioResponse(_message.Message):
    __slots__ = ("normalized_audio_file_id", "original_lufs", "normalized_lufs", "gain_applied_db", "limiting_applied")
    NORMALIZED_AUDIO_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_LUFS_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_LUFS_FIELD_NUMBER: _ClassVar[int]
    GAIN_APPLIED_DB_FIELD_NUMBER: _ClassVar[int]
    LIMITING_APPLIED_FIELD_NUMBER: _ClassVar[int]
    normalized_audio_file_id: str
    original_lufs: float
    normalized_lufs: float
    gain_applied_db: float
    limiting_applied: bool
    def __init__(self, normalized_audio_file_id: _Optional[str] = ..., original_lufs: _Optional[float] = ..., normalized_lufs: _Optional[float] = ..., gain_applied_db: _Optional[float] = ..., limiting_applied: bool = ...) -> None: ...
