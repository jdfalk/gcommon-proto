import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteStats(_message.Message):
    __slots__ = ("execution_time", "affected_rows", "cost_estimate")
    EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_ROWS_FIELD_NUMBER: _ClassVar[int]
    COST_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    execution_time: _duration_pb2.Duration
    affected_rows: int
    cost_estimate: float
    def __init__(
        self,
        execution_time: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        affected_rows: _Optional[int] = ...,
        cost_estimate: _Optional[float] = ...,
    ) -> None: ...
