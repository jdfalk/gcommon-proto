from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NormalizeAudioRequest(_message.Message):
    __slots__ = ("audio_file_id", "options")
    AUDIO_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    audio_file_id: str
    options: NormalizationOptions
    def __init__(self, audio_file_id: _Optional[str] = ..., options: _Optional[_Union[NormalizationOptions, _Mapping]] = ...) -> None: ...

class NormalizationOptions(_message.Message):
    __slots__ = ("target_lufs", "max_peak_db", "enable_limiter")
    TARGET_LUFS_FIELD_NUMBER: _ClassVar[int]
    MAX_PEAK_DB_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LIMITER_FIELD_NUMBER: _ClassVar[int]
    target_lufs: float
    max_peak_db: float
    enable_limiter: bool
    def __init__(self, target_lufs: _Optional[float] = ..., max_peak_db: _Optional[float] = ..., enable_limiter: bool = ...) -> None: ...
