from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANGE_TYPE_UNSPECIFIED: _ClassVar[MetricsChangeType]
    CHANGE_TYPE_ADDED: _ClassVar[MetricsChangeType]
    CHANGE_TYPE_UPDATED: _ClassVar[MetricsChangeType]
    CHANGE_TYPE_REMOVED: _ClassVar[MetricsChangeType]
    CHANGE_TYPE_REPLACED: _ClassVar[MetricsChangeType]

CHANGE_TYPE_UNSPECIFIED: MetricsChangeType
CHANGE_TYPE_ADDED: MetricsChangeType
CHANGE_TYPE_UPDATED: MetricsChangeType
CHANGE_TYPE_REMOVED: MetricsChangeType
CHANGE_TYPE_REPLACED: MetricsChangeType
