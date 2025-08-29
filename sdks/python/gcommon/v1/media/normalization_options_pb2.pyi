from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NormalizationOptions(_message.Message):
    __slots__ = ("target_lufs", "max_peak_db", "enable_limiter")
    TARGET_LUFS_FIELD_NUMBER: _ClassVar[int]
    MAX_PEAK_DB_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LIMITER_FIELD_NUMBER: _ClassVar[int]
    target_lufs: float
    max_peak_db: float
    enable_limiter: bool
    def __init__(self, target_lufs: _Optional[float] = ..., max_peak_db: _Optional[float] = ..., enable_limiter: bool = ...) -> None: ...
