from gcommon.v1.queue import error_type_stat_pb2 as _error_type_stat_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueErrorStats(_message.Message):
    __slots__ = ("total_errors", "error_rate", "error_types", "recent_error_messages")
    TOTAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPES_FIELD_NUMBER: _ClassVar[int]
    RECENT_ERROR_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    total_errors: int
    error_rate: float
    error_types: _containers.RepeatedCompositeFieldContainer[
        _error_type_stat_pb2.ErrorTypeStat
    ]
    recent_error_messages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        total_errors: _Optional[int] = ...,
        error_rate: _Optional[float] = ...,
        error_types: _Optional[
            _Iterable[_Union[_error_type_stat_pb2.ErrorTypeStat, _Mapping]]
        ] = ...,
        recent_error_messages: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
