from gcommon.v1.queue import ack_level_pb2 as _ack_level_pb2
from gcommon.v1.queue import message_filter_pb2 as _message_filter_pb2
from gcommon.v1.queue import offset_config_pb2 as _offset_config_pb2
from gcommon.v1.queue import stream_config_pb2 as _stream_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamMessagesRequest(_message.Message):
    __slots__ = ("topic", "consumer_group_id", "consumer_id", "offset_config", "max_messages", "stream_timeout_ms", "ack_level", "batch_size", "filter", "auto_acknowledge", "pause_on_error", "include_metadata", "partition_ids", "stream_config")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    STREAM_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    ACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    AUTO_ACKNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    PAUSE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    PARTITION_IDS_FIELD_NUMBER: _ClassVar[int]
    STREAM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    topic: str
    consumer_group_id: str
    consumer_id: str
    offset_config: _offset_config_pb2.OffsetConfig
    max_messages: int
    stream_timeout_ms: int
    ack_level: _ack_level_pb2.AckLevel
    batch_size: int
    filter: _message_filter_pb2.MessageFilter
    auto_acknowledge: bool
    pause_on_error: bool
    include_metadata: bool
    partition_ids: _containers.RepeatedScalarFieldContainer[int]
    stream_config: _stream_config_pb2.StreamConfig
    def __init__(self, topic: _Optional[str] = ..., consumer_group_id: _Optional[str] = ..., consumer_id: _Optional[str] = ..., offset_config: _Optional[_Union[_offset_config_pb2.OffsetConfig, _Mapping]] = ..., max_messages: _Optional[int] = ..., stream_timeout_ms: _Optional[int] = ..., ack_level: _Optional[_Union[_ack_level_pb2.AckLevel, str]] = ..., batch_size: _Optional[int] = ..., filter: _Optional[_Union[_message_filter_pb2.MessageFilter, _Mapping]] = ..., auto_acknowledge: bool = ..., pause_on_error: bool = ..., include_metadata: bool = ..., partition_ids: _Optional[_Iterable[int]] = ..., stream_config: _Optional[_Union[_stream_config_pb2.StreamConfig, _Mapping]] = ...) -> None: ...
