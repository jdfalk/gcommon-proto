from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetSubscriptionInfoRequest(_message.Message):
    __slots__ = (
        "subscription_id",
        "include_metrics",
        "include_consumer_details",
        "include_partitions",
        "timeout_ms",
    )
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METRICS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CONSUMER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    include_metrics: bool
    include_consumer_details: bool
    include_partitions: bool
    timeout_ms: int
    def __init__(
        self,
        subscription_id: _Optional[str] = ...,
        include_metrics: _Optional[bool] = ...,
        include_consumer_details: _Optional[bool] = ...,
        include_partitions: _Optional[bool] = ...,
        timeout_ms: _Optional[int] = ...,
    ) -> None: ...
