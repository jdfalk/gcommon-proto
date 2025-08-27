from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DELIVERY_MODE_UNSPECIFIED: _ClassVar[DeliveryMode]
    DELIVERY_MODE_AT_MOST_ONCE: _ClassVar[DeliveryMode]
    DELIVERY_MODE_AT_LEAST_ONCE: _ClassVar[DeliveryMode]
    DELIVERY_MODE_EXACTLY_ONCE: _ClassVar[DeliveryMode]
    DELIVERY_MODE_BEST_EFFORT: _ClassVar[DeliveryMode]

DELIVERY_MODE_UNSPECIFIED: DeliveryMode
DELIVERY_MODE_AT_MOST_ONCE: DeliveryMode
DELIVERY_MODE_AT_LEAST_ONCE: DeliveryMode
DELIVERY_MODE_EXACTLY_ONCE: DeliveryMode
DELIVERY_MODE_BEST_EFFORT: DeliveryMode
