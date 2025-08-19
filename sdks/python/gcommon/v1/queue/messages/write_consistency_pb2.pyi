from gcommon.v1.queue.enums import write_level_pb2 as _write_level_pb2
from gcommon.v1.queue.messages import conflict_detection_pb2 as _conflict_detection_pb2
from gcommon.v1.queue.messages import sync_replication_pb2 as _sync_replication_pb2
from gcommon.v1.queue.messages import write_retry_config_pb2 as _write_retry_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WriteConsistency(_message.Message):
    __slots__ = ("level", "sync_replication", "conflict_detection", "timeout_ms", "retry_config")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SYNC_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_DETECTION_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    RETRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    level: _write_level_pb2.WriteLevel
    sync_replication: _sync_replication_pb2.SyncReplication
    conflict_detection: _conflict_detection_pb2.ConflictDetection
    timeout_ms: int
    retry_config: _write_retry_config_pb2.WriteRetryConfig
    def __init__(self, level: _Optional[_Union[_write_level_pb2.WriteLevel, str]] = ..., sync_replication: _Optional[_Union[_sync_replication_pb2.SyncReplication, _Mapping]] = ..., conflict_detection: _Optional[_Union[_conflict_detection_pb2.ConflictDetection, _Mapping]] = ..., timeout_ms: _Optional[int] = ..., retry_config: _Optional[_Union[_write_retry_config_pb2.WriteRetryConfig, _Mapping]] = ...) -> None: ...
