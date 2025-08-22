from gcommon.v1.common import comparison_operator_pb2 as _comparison_operator_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertingCondition(_message.Message):
    __slots__ = ("operator", "metric", "threshold", "duration_seconds")
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    operator: _comparison_operator_pb2.ComparisonOperator
    metric: str
    threshold: float
    duration_seconds: int
    def __init__(self, operator: _Optional[_Union[_comparison_operator_pb2.ComparisonOperator, str]] = ..., metric: _Optional[str] = ..., threshold: _Optional[float] = ..., duration_seconds: _Optional[int] = ...) -> None: ...
