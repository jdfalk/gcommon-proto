from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WebsocketConfig(_message.Message):
    __slots__ = ("endpoint", "allowed_origins", "enable_compression", "read_buffer_size", "write_buffer_size")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ORIGINS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    READ_BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    WRITE_BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    allowed_origins: _containers.RepeatedScalarFieldContainer[str]
    enable_compression: bool
    read_buffer_size: int
    write_buffer_size: int
    def __init__(self, endpoint: _Optional[str] = ..., allowed_origins: _Optional[_Iterable[str]] = ..., enable_compression: bool = ..., read_buffer_size: _Optional[int] = ..., write_buffer_size: _Optional[int] = ...) -> None: ...
