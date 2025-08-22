from gcommon.v1.common import load_balance_strategy_pb2 as _load_balance_strategy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebLoadBalancerConfig(_message.Message):
    __slots__ = ("strategy", "upstreams", "health_check_path", "timeout")
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    UPSTREAMS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_PATH_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    strategy: _load_balance_strategy_pb2.LoadBalanceStrategy
    upstreams: _containers.RepeatedScalarFieldContainer[str]
    health_check_path: str
    timeout: _duration_pb2.Duration
    def __init__(self, strategy: _Optional[_Union[_load_balance_strategy_pb2.LoadBalanceStrategy, str]] = ..., upstreams: _Optional[_Iterable[str]] = ..., health_check_path: _Optional[str] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
