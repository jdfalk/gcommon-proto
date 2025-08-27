from gcommon.v1.common import rate_limit_strategy_pb2 as _rate_limit_strategy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebRateLimitConfig(_message.Message):
    __slots__ = (
        "enabled",
        "requests_per_second",
        "burst_size",
        "strategy",
        "key_extractor",
        "skip_conditions",
    )
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    BURST_SIZE_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    KEY_EXTRACTOR_FIELD_NUMBER: _ClassVar[int]
    SKIP_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    requests_per_second: int
    burst_size: int
    strategy: _rate_limit_strategy_pb2.RateLimitStrategy
    key_extractor: str
    skip_conditions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        enabled: _Optional[bool] = ...,
        requests_per_second: _Optional[int] = ...,
        burst_size: _Optional[int] = ...,
        strategy: _Optional[
            _Union[_rate_limit_strategy_pb2.RateLimitStrategy, str]
        ] = ...,
        key_extractor: _Optional[str] = ...,
        skip_conditions: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
