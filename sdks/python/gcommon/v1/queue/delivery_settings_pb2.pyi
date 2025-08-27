from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeliverySettings(_message.Message):
    __slots__ = (
        "delivery_mode",
        "push_endpoint",
        "delivery_timeout_ms",
        "ordered_delivery",
    )
    DELIVERY_MODE_FIELD_NUMBER: _ClassVar[int]
    PUSH_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    ORDERED_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    delivery_mode: str
    push_endpoint: str
    delivery_timeout_ms: int
    ordered_delivery: bool
    def __init__(
        self,
        delivery_mode: _Optional[str] = ...,
        push_endpoint: _Optional[str] = ...,
        delivery_timeout_ms: _Optional[int] = ...,
        ordered_delivery: _Optional[bool] = ...,
    ) -> None: ...
