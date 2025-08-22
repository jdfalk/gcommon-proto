from gcommon.v1.common import flush_policy_pb2 as _flush_policy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlushQueueRequest(_message.Message):
    __slots__ = ("queue_id", "flush_policy", "wait_for_completion", "timeout_ms", "flush_until", "partition_ids", "force_flush", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    FLUSH_POLICY_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    FLUSH_UNTIL_FIELD_NUMBER: _ClassVar[int]
    PARTITION_IDS_FIELD_NUMBER: _ClassVar[int]
    FORCE_FLUSH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    flush_policy: _flush_policy_pb2.FlushPolicy
    wait_for_completion: bool
    timeout_ms: int
    flush_until: _timestamp_pb2.Timestamp
    partition_ids: _containers.RepeatedScalarFieldContainer[int]
    force_flush: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, queue_id: _Optional[str] = ..., flush_policy: _Optional[_Union[_flush_policy_pb2.FlushPolicy, str]] = ..., wait_for_completion: bool = ..., timeout_ms: _Optional[int] = ..., flush_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., partition_ids: _Optional[_Iterable[int]] = ..., force_flush: bool = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
