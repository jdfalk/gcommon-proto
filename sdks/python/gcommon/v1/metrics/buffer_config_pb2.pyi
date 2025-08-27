from gcommon.v1.common import buffer_overflow_strategy_pb2 as _buffer_overflow_strategy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BufferConfig(_message.Message):
    __slots__ = ("max_buffer_size", "overflow_strategy", "persist_buffer", "max_memory_bytes")
    MAX_BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    OVERFLOW_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    PERSIST_BUFFER_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    max_buffer_size: int
    overflow_strategy: _buffer_overflow_strategy_pb2.BufferOverflowStrategy
    persist_buffer: bool
    max_memory_bytes: int
    def __init__(self, max_buffer_size: _Optional[int] = ..., overflow_strategy: _Optional[_Union[_buffer_overflow_strategy_pb2.BufferOverflowStrategy, str]] = ..., persist_buffer: _Optional[bool] = ..., max_memory_bytes: _Optional[int] = ...) -> None: ...
