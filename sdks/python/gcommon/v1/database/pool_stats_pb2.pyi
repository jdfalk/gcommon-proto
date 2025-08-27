import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PoolStats(_message.Message):
    __slots__ = (
        "total_created",
        "total_closed",
        "acquisition_failures",
        "avg_acquisition_time",
    )
    TOTAL_CREATED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CLOSED_FIELD_NUMBER: _ClassVar[int]
    ACQUISITION_FAILURES_FIELD_NUMBER: _ClassVar[int]
    AVG_ACQUISITION_TIME_FIELD_NUMBER: _ClassVar[int]
    total_created: int
    total_closed: int
    acquisition_failures: int
    avg_acquisition_time: _duration_pb2.Duration
    def __init__(
        self,
        total_created: _Optional[int] = ...,
        total_closed: _Optional[int] = ...,
        acquisition_failures: _Optional[int] = ...,
        avg_acquisition_time: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
    ) -> None: ...
