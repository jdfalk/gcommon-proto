from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StatsDSettings(_message.Message):
    __slots__ = ("address", "protocol", "prefix", "sample_rate", "buffer_size")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    address: str
    protocol: str
    prefix: str
    sample_rate: float
    buffer_size: int
    def __init__(
        self,
        address: _Optional[str] = ...,
        protocol: _Optional[str] = ...,
        prefix: _Optional[str] = ...,
        sample_rate: _Optional[float] = ...,
        buffer_size: _Optional[int] = ...,
    ) -> None: ...
