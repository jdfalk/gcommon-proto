from gcommon.v1.config import config_stats_pb2 as _config_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConfigStatsResponse(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _config_stats_pb2.ConfigStats
    def __init__(self, stats: _Optional[_Union[_config_stats_pb2.ConfigStats, _Mapping]] = ...) -> None: ...
