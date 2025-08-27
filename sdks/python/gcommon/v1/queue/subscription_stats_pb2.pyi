from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionStats(_message.Message):
    __slots__ = (
        "subscription_id",
        "messages_consumed",
        "messages_acknowledged",
        "messages_rejected",
        "consumer_lag",
        "consumption_rate",
        "avg_processing_time_ms",
        "active_consumers",
        "last_activity_time",
    )
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_REJECTED_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_LAG_FIELD_NUMBER: _ClassVar[int]
    CONSUMPTION_RATE_FIELD_NUMBER: _ClassVar[int]
    AVG_PROCESSING_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_TIME_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    messages_consumed: int
    messages_acknowledged: int
    messages_rejected: int
    consumer_lag: int
    consumption_rate: float
    avg_processing_time_ms: float
    active_consumers: int
    last_activity_time: int
    def __init__(
        self,
        subscription_id: _Optional[str] = ...,
        messages_consumed: _Optional[int] = ...,
        messages_acknowledged: _Optional[int] = ...,
        messages_rejected: _Optional[int] = ...,
        consumer_lag: _Optional[int] = ...,
        consumption_rate: _Optional[float] = ...,
        avg_processing_time_ms: _Optional[float] = ...,
        active_consumers: _Optional[int] = ...,
        last_activity_time: _Optional[int] = ...,
    ) -> None: ...
