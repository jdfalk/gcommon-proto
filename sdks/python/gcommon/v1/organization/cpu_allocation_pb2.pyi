from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CPUAllocation(_message.Message):
    __slots__ = ("cores", "frequency_mhz", "usage_limit_percent", "priority")
    CORES_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_MHZ_FIELD_NUMBER: _ClassVar[int]
    USAGE_LIMIT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    cores: int
    frequency_mhz: int
    usage_limit_percent: int
    priority: int
    def __init__(self, cores: _Optional[int] = ..., frequency_mhz: _Optional[int] = ..., usage_limit_percent: _Optional[int] = ..., priority: _Optional[int] = ...) -> None: ...
