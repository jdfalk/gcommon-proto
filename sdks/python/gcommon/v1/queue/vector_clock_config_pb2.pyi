from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VectorClockConfig(_message.Message):
    __slots__ = ("enabled", "precision", "max_drift_ms")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    MAX_DRIFT_MS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    precision: str
    max_drift_ms: int
    def __init__(self, enabled: _Optional[bool] = ..., precision: _Optional[str] = ..., max_drift_ms: _Optional[int] = ...) -> None: ...
