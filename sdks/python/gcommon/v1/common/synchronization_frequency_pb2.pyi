from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SynchronizationFrequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYNCHRONIZATION_FREQUENCY_UNSPECIFIED: _ClassVar[SynchronizationFrequency]
    SYNCHRONIZATION_FREQUENCY_REAL_TIME: _ClassVar[SynchronizationFrequency]
    SYNCHRONIZATION_FREQUENCY_HOURLY: _ClassVar[SynchronizationFrequency]
    SYNCHRONIZATION_FREQUENCY_DAILY: _ClassVar[SynchronizationFrequency]
    SYNCHRONIZATION_FREQUENCY_WEEKLY: _ClassVar[SynchronizationFrequency]
    SYNCHRONIZATION_FREQUENCY_ON_CHANGE: _ClassVar[SynchronizationFrequency]

SYNCHRONIZATION_FREQUENCY_UNSPECIFIED: SynchronizationFrequency
SYNCHRONIZATION_FREQUENCY_REAL_TIME: SynchronizationFrequency
SYNCHRONIZATION_FREQUENCY_HOURLY: SynchronizationFrequency
SYNCHRONIZATION_FREQUENCY_DAILY: SynchronizationFrequency
SYNCHRONIZATION_FREQUENCY_WEEKLY: SynchronizationFrequency
SYNCHRONIZATION_FREQUENCY_ON_CHANGE: SynchronizationFrequency
