import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ArchiveCriteria(_message.Message):
    __slots__ = ("older_than", "size_threshold_bytes")
    OLDER_THAN_FIELD_NUMBER: _ClassVar[int]
    SIZE_THRESHOLD_BYTES_FIELD_NUMBER: _ClassVar[int]
    older_than: _duration_pb2.Duration
    size_threshold_bytes: int
    def __init__(
        self,
        older_than: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        size_threshold_bytes: _Optional[int] = ...,
    ) -> None: ...
