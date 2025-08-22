from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RotationFrequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROTATION_FREQUENCY_UNSPECIFIED: _ClassVar[RotationFrequency]
    ROTATION_FREQUENCY_MANUAL: _ClassVar[RotationFrequency]
    ROTATION_FREQUENCY_DAILY: _ClassVar[RotationFrequency]
    ROTATION_FREQUENCY_WEEKLY: _ClassVar[RotationFrequency]
    ROTATION_FREQUENCY_MONTHLY: _ClassVar[RotationFrequency]
    ROTATION_FREQUENCY_QUARTERLY: _ClassVar[RotationFrequency]
    ROTATION_FREQUENCY_YEARLY: _ClassVar[RotationFrequency]
    ROTATION_FREQUENCY_ON_EXPIRY: _ClassVar[RotationFrequency]
ROTATION_FREQUENCY_UNSPECIFIED: RotationFrequency
ROTATION_FREQUENCY_MANUAL: RotationFrequency
ROTATION_FREQUENCY_DAILY: RotationFrequency
ROTATION_FREQUENCY_WEEKLY: RotationFrequency
ROTATION_FREQUENCY_MONTHLY: RotationFrequency
ROTATION_FREQUENCY_QUARTERLY: RotationFrequency
ROTATION_FREQUENCY_YEARLY: RotationFrequency
ROTATION_FREQUENCY_ON_EXPIRY: RotationFrequency
