from gcommon.v1.common import ack_level_pb2 as _ack_level_pb2
from gcommon.v1.common import delivery_mode_pb2 as _delivery_mode_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionConfiguration(_message.Message):
    __slots__ = (
        "ack_level",
        "delivery_mode",
        "max_unacked_messages",
        "ack_timeout_ms",
        "min_priority",
        "ordered_delivery",
        "auto_acknowledge",
        "expiration_seconds",
        "duplicate_detection",
        "max_message_age_seconds",
    )
    ACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_UNACKED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ACK_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    MIN_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ORDERED_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    AUTO_ACKNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_DETECTION_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGE_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ack_level: _ack_level_pb2.AckLevel
    delivery_mode: _delivery_mode_pb2.DeliveryMode
    max_unacked_messages: int
    ack_timeout_ms: int
    min_priority: int
    ordered_delivery: bool
    auto_acknowledge: bool
    expiration_seconds: int
    duplicate_detection: bool
    max_message_age_seconds: int
    def __init__(
        self,
        ack_level: _Optional[_Union[_ack_level_pb2.AckLevel, str]] = ...,
        delivery_mode: _Optional[_Union[_delivery_mode_pb2.DeliveryMode, str]] = ...,
        max_unacked_messages: _Optional[int] = ...,
        ack_timeout_ms: _Optional[int] = ...,
        min_priority: _Optional[int] = ...,
        ordered_delivery: _Optional[bool] = ...,
        auto_acknowledge: _Optional[bool] = ...,
        expiration_seconds: _Optional[int] = ...,
        duplicate_detection: _Optional[bool] = ...,
        max_message_age_seconds: _Optional[int] = ...,
    ) -> None: ...
