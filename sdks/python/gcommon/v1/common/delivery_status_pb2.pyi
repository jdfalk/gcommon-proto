from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DELIVERY_STATUS_UNSPECIFIED: _ClassVar[DeliveryStatus]
    DELIVERY_STATUS_PENDING: _ClassVar[DeliveryStatus]
    DELIVERY_STATUS_SENT: _ClassVar[DeliveryStatus]
    DELIVERY_STATUS_FAILED: _ClassVar[DeliveryStatus]
    DELIVERY_STATUS_ACKNOWLEDGED: _ClassVar[DeliveryStatus]
DELIVERY_STATUS_UNSPECIFIED: DeliveryStatus
DELIVERY_STATUS_PENDING: DeliveryStatus
DELIVERY_STATUS_SENT: DeliveryStatus
DELIVERY_STATUS_FAILED: DeliveryStatus
DELIVERY_STATUS_ACKNOWLEDGED: DeliveryStatus
