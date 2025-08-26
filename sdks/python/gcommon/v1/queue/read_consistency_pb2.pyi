from gcommon.v1.common import read_level_pb2 as _read_level_pb2
from gcommon.v1.queue import read_retry_config_pb2 as _read_retry_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadConsistency(_message.Message):
    __slots__ = ("level", "max_staleness_ms", "read_your_writes", "monotonic_reads", "timeout_ms", "retry_config")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_STALENESS_MS_FIELD_NUMBER: _ClassVar[int]
    READ_YOUR_WRITES_FIELD_NUMBER: _ClassVar[int]
    MONOTONIC_READS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    RETRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    level: _read_level_pb2.ReadLevel
    max_staleness_ms: int
    read_your_writes: bool
    monotonic_reads: bool
    timeout_ms: int
    retry_config: _read_retry_config_pb2.ReadRetryConfig
    def __init__(self, level: _Optional[_Union[_read_level_pb2.ReadLevel, str]] = ..., max_staleness_ms: _Optional[int] = ..., read_your_writes: _Optional[bool] = ..., monotonic_reads: _Optional[bool] = ..., timeout_ms: _Optional[int] = ..., retry_config: _Optional[_Union[_read_retry_config_pb2.ReadRetryConfig, _Mapping]] = ...) -> None: ...
