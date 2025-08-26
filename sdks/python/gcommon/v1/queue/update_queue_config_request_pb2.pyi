from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.queue import queue_config_pb2 as _queue_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateQueueConfigRequest(_message.Message):
    __slots__ = ("queue_name", "config", "update_mask", "metadata", "force", "reason")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    config: _queue_config_pb2.QueueConfig
    update_mask: _containers.RepeatedScalarFieldContainer[str]
    metadata: _request_metadata_pb2.RequestMetadata
    force: bool
    reason: str
    def __init__(self, queue_name: _Optional[str] = ..., config: _Optional[_Union[_queue_config_pb2.QueueConfig, _Mapping]] = ..., update_mask: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., force: _Optional[bool] = ..., reason: _Optional[str] = ...) -> None: ...
