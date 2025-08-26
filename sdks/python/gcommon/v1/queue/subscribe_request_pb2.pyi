from gcommon.v1.queue import delivery_configuration_pb2 as _delivery_configuration_pb2
from gcommon.v1.queue import error_handling_config_pb2 as _error_handling_config_pb2
from gcommon.v1.queue import message_filter_config_pb2 as _message_filter_config_pb2
from gcommon.v1.queue import subscription_configuration_pb2 as _subscription_configuration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueSubscribeRequest(_message.Message):
    __slots__ = ("topic", "subscription_name", "consumer_group_id", "consumer_id", "config", "filter_config", "delivery_config", "error_handling", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    FILTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERROR_HANDLING_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    topic: str
    subscription_name: str
    consumer_group_id: str
    consumer_id: str
    config: _subscription_configuration_pb2.SubscriptionConfiguration
    filter_config: _message_filter_config_pb2.MessageFilterConfig
    delivery_config: _delivery_configuration_pb2.DeliveryConfiguration
    error_handling: _error_handling_config_pb2.ErrorHandlingConfig
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, topic: _Optional[str] = ..., subscription_name: _Optional[str] = ..., consumer_group_id: _Optional[str] = ..., consumer_id: _Optional[str] = ..., config: _Optional[_Union[_subscription_configuration_pb2.SubscriptionConfiguration, _Mapping]] = ..., filter_config: _Optional[_Union[_message_filter_config_pb2.MessageFilterConfig, _Mapping]] = ..., delivery_config: _Optional[_Union[_delivery_configuration_pb2.DeliveryConfiguration, _Mapping]] = ..., error_handling: _Optional[_Union[_error_handling_config_pb2.ErrorHandlingConfig, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
