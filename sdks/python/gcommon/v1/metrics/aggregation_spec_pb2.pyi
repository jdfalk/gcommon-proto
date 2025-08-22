from gcommon.v1.metrics import aggregation_type_pb2 as _aggregation_type_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AggregationSpec(_message.Message):
    __slots__ = ("aggregation_type", "field", "window", "step", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AGGREGATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    aggregation_type: _aggregation_type_pb2.AggregationType
    field: str
    window: _duration_pb2.Duration
    step: _duration_pb2.Duration
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, aggregation_type: _Optional[_Union[_aggregation_type_pb2.AggregationType, str]] = ..., field: _Optional[str] = ..., window: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., step: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...
