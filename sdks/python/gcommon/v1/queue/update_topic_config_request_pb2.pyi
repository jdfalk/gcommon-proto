from gcommon.v1.queue import topic_config_pb2 as _topic_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateTopicConfigRequest(_message.Message):
    __slots__ = (
        "topic_name",
        "config",
        "validate_only",
        "incremental_update",
        "timeout_ms",
    )
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_UPDATE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    topic_name: str
    config: _topic_config_pb2.TopicConfig
    validate_only: bool
    incremental_update: bool
    timeout_ms: int
    def __init__(
        self,
        topic_name: _Optional[str] = ...,
        config: _Optional[_Union[_topic_config_pb2.TopicConfig, _Mapping]] = ...,
        validate_only: _Optional[bool] = ...,
        incremental_update: _Optional[bool] = ...,
        timeout_ms: _Optional[int] = ...,
    ) -> None: ...
