import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ThumbnailInfo(_message.Message):
    __slots__ = ("timestamp", "file_path", "width", "height")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    timestamp: _duration_pb2.Duration
    file_path: str
    width: int
    height: int
    def __init__(self, timestamp: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., file_path: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
