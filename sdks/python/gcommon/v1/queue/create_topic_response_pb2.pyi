from gcommon.v1.queue import topic_config_pb2 as _topic_config_pb2
from gcommon.v1.queue import topic_info_pb2 as _topic_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTopicResponse(_message.Message):
    __slots__ = ("topic_info", "created", "created_at", "warnings", "applied_config")
    TOPIC_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    topic_info: _topic_info_pb2.TopicInfo
    created: bool
    created_at: _timestamp_pb2.Timestamp
    warnings: _containers.RepeatedScalarFieldContainer[str]
    applied_config: _topic_config_pb2.TopicConfig
    def __init__(self, topic_info: _Optional[_Union[_topic_info_pb2.TopicInfo, _Mapping]] = ..., created: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ..., applied_config: _Optional[_Union[_topic_config_pb2.TopicConfig, _Mapping]] = ...) -> None: ...
