from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PauseQueueRequest(_message.Message):
    __slots__ = ("queue_name", "reason", "graceful", "timeout_ms", "metadata", "partition_ids")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    GRACEFUL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PARTITION_IDS_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    reason: str
    graceful: bool
    timeout_ms: int
    metadata: _request_metadata_pb2.RequestMetadata
    partition_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, queue_name: _Optional[str] = ..., reason: _Optional[str] = ..., graceful: _Optional[bool] = ..., timeout_ms: _Optional[int] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., partition_ids: _Optional[_Iterable[int]] = ...) -> None: ...
