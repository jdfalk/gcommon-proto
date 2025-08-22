from gcommon.v1.common import resolution_strategy_pb2 as _resolution_strategy_pb2
from gcommon.v1.queue import custom_resolution_pb2 as _custom_resolution_pb2
from gcommon.v1.queue import last_writer_wins_pb2 as _last_writer_wins_pb2
from gcommon.v1.queue import multi_value_config_pb2 as _multi_value_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueConflictResolution(_message.Message):
    __slots__ = ("strategy", "custom_resolution", "lww_config", "multi_value")
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    LWW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MULTI_VALUE_FIELD_NUMBER: _ClassVar[int]
    strategy: _resolution_strategy_pb2.ResolutionStrategy
    custom_resolution: _custom_resolution_pb2.CustomResolution
    lww_config: _last_writer_wins_pb2.LastWriterWins
    multi_value: _multi_value_config_pb2.MultiValueConfig
    def __init__(self, strategy: _Optional[_Union[_resolution_strategy_pb2.ResolutionStrategy, str]] = ..., custom_resolution: _Optional[_Union[_custom_resolution_pb2.CustomResolution, _Mapping]] = ..., lww_config: _Optional[_Union[_last_writer_wins_pb2.LastWriterWins, _Mapping]] = ..., multi_value: _Optional[_Union[_multi_value_config_pb2.MultiValueConfig, _Mapping]] = ...) -> None: ...
