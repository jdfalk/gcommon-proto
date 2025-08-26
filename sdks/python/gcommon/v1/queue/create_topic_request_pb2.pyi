from gcommon.v1.queue import topic_config_pb2 as _topic_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTopicRequest(_message.Message):
    __slots__ = ("topic_name", "config", "durable", "auto_delete", "arguments")
    class ArgumentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    topic_name: str
    config: _topic_config_pb2.TopicConfig
    durable: bool
    auto_delete: bool
    arguments: _containers.ScalarMap[str, str]
    def __init__(self, topic_name: _Optional[str] = ..., config: _Optional[_Union[_topic_config_pb2.TopicConfig, _Mapping]] = ..., durable: _Optional[bool] = ..., auto_delete: _Optional[bool] = ..., arguments: _Optional[_Mapping[str, str]] = ...) -> None: ...
