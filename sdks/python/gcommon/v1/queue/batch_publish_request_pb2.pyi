from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.queue import queue_message_pb2 as _queue_message_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchPublishRequest(_message.Message):
    __slots__ = ("queue_name", "messages", "use_transaction", "timeout_ms", "wait_for_all", "metadata", "max_retries", "batch_id")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    USE_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_ALL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    messages: _containers.RepeatedCompositeFieldContainer[_queue_message_pb2.QueueMessage]
    use_transaction: bool
    timeout_ms: int
    wait_for_all: bool
    metadata: _request_metadata_pb2.RequestMetadata
    max_retries: int
    batch_id: str
    def __init__(self, queue_name: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[_queue_message_pb2.QueueMessage, _Mapping]]] = ..., use_transaction: _Optional[bool] = ..., timeout_ms: _Optional[int] = ..., wait_for_all: _Optional[bool] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., max_retries: _Optional[int] = ..., batch_id: _Optional[str] = ...) -> None: ...
