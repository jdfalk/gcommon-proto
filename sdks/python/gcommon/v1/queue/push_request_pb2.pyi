from gcommon.v1.queue import batch_settings_pb2 as _batch_settings_pb2
from gcommon.v1.queue import publish_config_pb2 as _publish_config_pb2
from gcommon.v1.queue import queue_message_pb2 as _queue_message_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PushRequest(_message.Message):
    __slots__ = ("topic", "messages", "publish_config", "batch_settings", "transaction_id", "producer_id", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BATCH_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    topic: str
    messages: _containers.RepeatedCompositeFieldContainer[_queue_message_pb2.QueueMessage]
    publish_config: _publish_config_pb2.PublishConfig
    batch_settings: _batch_settings_pb2.BatchSettings
    transaction_id: str
    producer_id: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, topic: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[_queue_message_pb2.QueueMessage, _Mapping]]] = ..., publish_config: _Optional[_Union[_publish_config_pb2.PublishConfig, _Mapping]] = ..., batch_settings: _Optional[_Union[_batch_settings_pb2.BatchSettings, _Mapping]] = ..., transaction_id: _Optional[str] = ..., producer_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
