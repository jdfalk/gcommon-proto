from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PebbleConfig(_message.Message):
    __slots__ = ("path", "cache_size", "memtable_size", "max_open_files", "compression")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CACHE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MEMTABLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_OPEN_FILES_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    path: str
    cache_size: int
    memtable_size: int
    max_open_files: int
    compression: bool
    def __init__(self, path: _Optional[str] = ..., cache_size: _Optional[int] = ..., memtable_size: _Optional[int] = ..., max_open_files: _Optional[int] = ..., compression: bool = ...) -> None: ...
