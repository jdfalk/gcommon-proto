from gcommon.v1.queue.messages import batch_delivery_config_pb2 as _batch_delivery_config_pb2
from gcommon.v1.queue.messages import delivery_retry_config_pb2 as _delivery_retry_config_pb2
from gcommon.v1.queue.messages import flow_control_settings_pb2 as _flow_control_settings_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryConfiguration(_message.Message):
    __slots__ = ("push_endpoint", "delivery_timeout_ms", "retry_config", "batch_config", "flow_control", "enable_compression", "auth_headers")
    class AuthHeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PUSH_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    RETRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BATCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FLOW_CONTROL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    AUTH_HEADERS_FIELD_NUMBER: _ClassVar[int]
    push_endpoint: str
    delivery_timeout_ms: int
    retry_config: _delivery_retry_config_pb2.DeliveryRetryConfig
    batch_config: _batch_delivery_config_pb2.BatchDeliveryConfig
    flow_control: _flow_control_settings_pb2.FlowControlSettings
    enable_compression: bool
    auth_headers: _containers.ScalarMap[str, str]
    def __init__(self, push_endpoint: _Optional[str] = ..., delivery_timeout_ms: _Optional[int] = ..., retry_config: _Optional[_Union[_delivery_retry_config_pb2.DeliveryRetryConfig, _Mapping]] = ..., batch_config: _Optional[_Union[_batch_delivery_config_pb2.BatchDeliveryConfig, _Mapping]] = ..., flow_control: _Optional[_Union[_flow_control_settings_pb2.FlowControlSettings, _Mapping]] = ..., enable_compression: bool = ..., auth_headers: _Optional[_Mapping[str, str]] = ...) -> None: ...
