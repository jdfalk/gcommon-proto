import datetime

from gcommon.v1.metrics import query_step_pb2 as _query_step_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryPlan(_message.Message):
    __slots__ = ("query_id", "estimated_duration", "estimated_data_points", "steps", "storage_backends")
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DURATION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BACKENDS_FIELD_NUMBER: _ClassVar[int]
    query_id: str
    estimated_duration: _duration_pb2.Duration
    estimated_data_points: int
    steps: _containers.RepeatedCompositeFieldContainer[_query_step_pb2.QueryStep]
    storage_backends: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, query_id: _Optional[str] = ..., estimated_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., estimated_data_points: _Optional[int] = ..., steps: _Optional[_Iterable[_Union[_query_step_pb2.QueryStep, _Mapping]]] = ..., storage_backends: _Optional[_Iterable[str]] = ...) -> None: ...
