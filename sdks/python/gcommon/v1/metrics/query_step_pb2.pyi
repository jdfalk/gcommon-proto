import datetime

from gcommon.v1.common import query_operation_pb2 as _query_operation_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryStep(_message.Message):
    __slots__ = ("step_id", "operation", "description", "estimated_duration", "input_step_ids")
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DURATION_FIELD_NUMBER: _ClassVar[int]
    INPUT_STEP_IDS_FIELD_NUMBER: _ClassVar[int]
    step_id: str
    operation: _query_operation_pb2.QueryOperation
    description: str
    estimated_duration: _duration_pb2.Duration
    input_step_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, step_id: _Optional[str] = ..., operation: _Optional[_Union[_query_operation_pb2.QueryOperation, str]] = ..., description: _Optional[str] = ..., estimated_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., input_step_ids: _Optional[_Iterable[str]] = ...) -> None: ...
