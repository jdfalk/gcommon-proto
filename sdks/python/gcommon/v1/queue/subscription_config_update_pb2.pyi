from gcommon.v1.common import config_retry_settings_pb2 as _config_retry_settings_pb2
from gcommon.v1.queue import delivery_settings_pb2 as _delivery_settings_pb2
from gcommon.v1.queue import filter_settings_pb2 as _filter_settings_pb2
from gcommon.v1.queue import routing_settings_pb2 as _routing_settings_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionConfigUpdate(_message.Message):
    __slots__ = ("name", "delivery_settings", "retry_settings", "filter_settings", "routing_settings", "max_inflight_messages", "ack_timeout_ms", "priority_level")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RETRY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FILTER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ROUTING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MAX_INFLIGHT_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ACK_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    delivery_settings: _delivery_settings_pb2.DeliverySettings
    retry_settings: _config_retry_settings_pb2.ConfigRetrySettings
    filter_settings: _filter_settings_pb2.FilterSettings
    routing_settings: _routing_settings_pb2.RoutingSettings
    max_inflight_messages: int
    ack_timeout_ms: int
    priority_level: int
    def __init__(self, name: _Optional[str] = ..., delivery_settings: _Optional[_Union[_delivery_settings_pb2.DeliverySettings, _Mapping]] = ..., retry_settings: _Optional[_Union[_config_retry_settings_pb2.ConfigRetrySettings, _Mapping]] = ..., filter_settings: _Optional[_Union[_filter_settings_pb2.FilterSettings, _Mapping]] = ..., routing_settings: _Optional[_Union[_routing_settings_pb2.RoutingSettings, _Mapping]] = ..., max_inflight_messages: _Optional[int] = ..., ack_timeout_ms: _Optional[int] = ..., priority_level: _Optional[int] = ...) -> None: ...
