from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamStart(_message.Message):
    __slots__ = ("from_timestamp", "from_beginning", "from_now", "from_offset")
    FROM_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FROM_BEGINNING_FIELD_NUMBER: _ClassVar[int]
    FROM_NOW_FIELD_NUMBER: _ClassVar[int]
    FROM_OFFSET_FIELD_NUMBER: _ClassVar[int]
    from_timestamp: _timestamp_pb2.Timestamp
    from_beginning: bool
    from_now: bool
    from_offset: str
    def __init__(self, from_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., from_beginning: bool = ..., from_now: bool = ..., from_offset: _Optional[str] = ...) -> None: ...
