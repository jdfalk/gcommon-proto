from gcommon.v1.common import health_state_pb2 as _health_state_pb2
from gcommon.v1.config import health_check_result_pb2 as _health_check_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigHealthStatus(_message.Message):
    __slots__ = ("overall", "components", "health_checks", "last_check", "metrics")
    class ComponentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _health_state_pb2.HealthState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_health_state_pb2.HealthState, str]] = ...) -> None: ...
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    OVERALL_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECKS_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECK_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    overall: _health_state_pb2.HealthState
    components: _containers.ScalarMap[str, _health_state_pb2.HealthState]
    health_checks: _containers.RepeatedCompositeFieldContainer[_health_check_result_pb2.ConfigHealthCheckResult]
    last_check: _timestamp_pb2.Timestamp
    metrics: _containers.ScalarMap[str, float]
    def __init__(self, overall: _Optional[_Union[_health_state_pb2.HealthState, str]] = ..., components: _Optional[_Mapping[str, _health_state_pb2.HealthState]] = ..., health_checks: _Optional[_Iterable[_Union[_health_check_result_pb2.ConfigHealthCheckResult, _Mapping]]] = ..., last_check: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metrics: _Optional[_Mapping[str, float]] = ...) -> None: ...
