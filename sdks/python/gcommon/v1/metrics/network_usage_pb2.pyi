from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkUsage(_message.Message):
    __slots__ = ("bytes_in_per_second", "bytes_out_per_second", "packets_in_per_second", "packets_out_per_second")
    BYTES_IN_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    BYTES_OUT_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    PACKETS_IN_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    PACKETS_OUT_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    bytes_in_per_second: int
    bytes_out_per_second: int
    packets_in_per_second: int
    packets_out_per_second: int
    def __init__(self, bytes_in_per_second: _Optional[int] = ..., bytes_out_per_second: _Optional[int] = ..., packets_in_per_second: _Optional[int] = ..., packets_out_per_second: _Optional[int] = ...) -> None: ...
