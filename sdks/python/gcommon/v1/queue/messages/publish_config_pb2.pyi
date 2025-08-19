from gcommon.v1.metrics.messages import export_config_pb2 as _export_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PublishConfig(_message.Message):
    __slots__ = ("wait_for_ack", "ack_timeout_ms", "duplicate_detection", "enable_compression", "enable_ordering", "retry_config", "persistence_level")
    WAIT_FOR_ACK_FIELD_NUMBER: _ClassVar[int]
    ACK_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_DETECTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ORDERING_FIELD_NUMBER: _ClassVar[int]
    RETRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    wait_for_ack: bool
    ack_timeout_ms: int
    duplicate_detection: bool
    enable_compression: bool
    enable_ordering: bool
    retry_config: _export_config_pb2.MetricsRetryConfig
    persistence_level: str
    def __init__(self, wait_for_ack: bool = ..., ack_timeout_ms: _Optional[int] = ..., duplicate_detection: bool = ..., enable_compression: bool = ..., enable_ordering: bool = ..., retry_config: _Optional[_Union[_export_config_pb2.MetricsRetryConfig, _Mapping]] = ..., persistence_level: _Optional[str] = ...) -> None: ...
