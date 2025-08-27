from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CPUUsage(_message.Message):
    __slots__ = ("current_percent", "avg_percent", "peak_percent")
    CURRENT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    AVG_PERCENT_FIELD_NUMBER: _ClassVar[int]
    PEAK_PERCENT_FIELD_NUMBER: _ClassVar[int]
    current_percent: float
    avg_percent: float
    peak_percent: float
    def __init__(
        self,
        current_percent: _Optional[float] = ...,
        avg_percent: _Optional[float] = ...,
        peak_percent: _Optional[float] = ...,
    ) -> None: ...
