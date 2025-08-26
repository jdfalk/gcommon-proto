from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueRetentionPolicy(_message.Message):
    __slots__ = ("max_age", "max_size_bytes", "discard_old")
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISCARD_OLD_FIELD_NUMBER: _ClassVar[int]
    max_age: _duration_pb2.Duration
    max_size_bytes: int
    discard_old: bool
    def __init__(self, max_age: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_size_bytes: _Optional[int] = ..., discard_old: bool = ...) -> None: ...
