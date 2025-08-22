from gcommon.v1.queue import conflict_strategy_pb2 as _conflict_strategy_pb2
from gcommon.v1.queue import timestamp_config_pb2 as _timestamp_config_pb2
from gcommon.v1.queue import vector_clock_config_pb2 as _vector_clock_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConflictDetection(_message.Message):
    __slots__ = ("enabled", "strategy", "vector_clock", "timestamp_config")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    VECTOR_CLOCK_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    strategy: _conflict_strategy_pb2.ConflictStrategy
    vector_clock: _vector_clock_config_pb2.VectorClockConfig
    timestamp_config: _timestamp_config_pb2.TimestampConfig
    def __init__(self, enabled: bool = ..., strategy: _Optional[_Union[_conflict_strategy_pb2.ConflictStrategy, str]] = ..., vector_clock: _Optional[_Union[_vector_clock_config_pb2.VectorClockConfig, _Mapping]] = ..., timestamp_config: _Optional[_Union[_timestamp_config_pb2.TimestampConfig, _Mapping]] = ...) -> None: ...
