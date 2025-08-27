from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class GaugeOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GAUGE_OPERATION_UNSPECIFIED: _ClassVar[GaugeOperation]
    GAUGE_OPERATION_SET: _ClassVar[GaugeOperation]
    GAUGE_OPERATION_ADD: _ClassVar[GaugeOperation]
    GAUGE_OPERATION_SUBTRACT: _ClassVar[GaugeOperation]
    GAUGE_OPERATION_INCREMENT: _ClassVar[GaugeOperation]
    GAUGE_OPERATION_DECREMENT: _ClassVar[GaugeOperation]

GAUGE_OPERATION_UNSPECIFIED: GaugeOperation
GAUGE_OPERATION_SET: GaugeOperation
GAUGE_OPERATION_ADD: GaugeOperation
GAUGE_OPERATION_SUBTRACT: GaugeOperation
GAUGE_OPERATION_INCREMENT: GaugeOperation
GAUGE_OPERATION_DECREMENT: GaugeOperation
