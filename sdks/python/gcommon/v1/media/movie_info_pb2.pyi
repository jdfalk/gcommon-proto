import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MovieInfo(_message.Message):
    __slots__ = ("release_date", "budget", "revenue", "runtime_minutes")
    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    REVENUE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_MINUTES_FIELD_NUMBER: _ClassVar[int]
    release_date: _timestamp_pb2.Timestamp
    budget: int
    revenue: int
    runtime_minutes: int
    def __init__(self, release_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., budget: _Optional[int] = ..., revenue: _Optional[int] = ..., runtime_minutes: _Optional[int] = ...) -> None: ...
