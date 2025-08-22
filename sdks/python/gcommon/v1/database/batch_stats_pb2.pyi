from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseBatchStats(_message.Message):
    __slots__ = ("total_time", "successful_operations", "failed_operations", "total_affected_rows")
    TOTAL_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    FAILED_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AFFECTED_ROWS_FIELD_NUMBER: _ClassVar[int]
    total_time: _duration_pb2.Duration
    successful_operations: int
    failed_operations: int
    total_affected_rows: int
    def __init__(self, total_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., successful_operations: _Optional[int] = ..., failed_operations: _Optional[int] = ..., total_affected_rows: _Optional[int] = ...) -> None: ...
