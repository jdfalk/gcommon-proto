from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.queue import queue_config_pb2 as _queue_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateQueueRequest(_message.Message):
    __slots__ = ("queue_name", "config", "if_not_exists", "metadata", "tags", "description")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    config: _queue_config_pb2.QueueConfig
    if_not_exists: bool
    metadata: _request_metadata_pb2.RequestMetadata
    tags: _containers.ScalarMap[str, str]
    description: str
    def __init__(self, queue_name: _Optional[str] = ..., config: _Optional[_Union[_queue_config_pb2.QueueConfig, _Mapping]] = ..., if_not_exists: _Optional[bool] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ...) -> None: ...
