from gcommon.v1.queue import ack_level_pb2 as _ack_level_pb2
from gcommon.v1.queue import flush_policy_pb2 as _flush_policy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DurabilityConfig(_message.Message):
    __slots__ = ("persistent", "flush_policy", "replication_factor", "ack_level", "durability_timeout", "write_ahead_log", "sync_interval", "verify_checksums")
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    FLUSH_POLICY_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DURABILITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    WRITE_AHEAD_LOG_FIELD_NUMBER: _ClassVar[int]
    SYNC_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    VERIFY_CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    persistent: bool
    flush_policy: _flush_policy_pb2.FlushPolicy
    replication_factor: int
    ack_level: _ack_level_pb2.AckLevel
    durability_timeout: _duration_pb2.Duration
    write_ahead_log: bool
    sync_interval: _duration_pb2.Duration
    verify_checksums: bool
    def __init__(self, persistent: bool = ..., flush_policy: _Optional[_Union[_flush_policy_pb2.FlushPolicy, str]] = ..., replication_factor: _Optional[int] = ..., ack_level: _Optional[_Union[_ack_level_pb2.AckLevel, str]] = ..., durability_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., write_ahead_log: bool = ..., sync_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., verify_checksums: bool = ...) -> None: ...
