import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumerErrorStats(_message.Message):
    __slots__ = ("total_errors", "connection_errors", "timeout_errors", "serialization_errors", "last_error")
    TOTAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    total_errors: int
    connection_errors: int
    timeout_errors: int
    serialization_errors: int
    last_error: _timestamp_pb2.Timestamp
    def __init__(self, total_errors: _Optional[int] = ..., connection_errors: _Optional[int] = ..., timeout_errors: _Optional[int] = ..., serialization_errors: _Optional[int] = ..., last_error: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
