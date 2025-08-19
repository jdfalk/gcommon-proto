from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorTypeStat(_message.Message):
    __slots__ = ("error_type", "count", "rate", "last_occurrence")
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    LAST_OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
    error_type: str
    count: int
    rate: float
    last_occurrence: str
    def __init__(self, error_type: _Optional[str] = ..., count: _Optional[int] = ..., rate: _Optional[float] = ..., last_occurrence: _Optional[str] = ...) -> None: ...
