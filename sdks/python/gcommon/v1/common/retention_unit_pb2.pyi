from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RetentionUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RETENTION_UNIT_UNSPECIFIED: _ClassVar[RetentionUnit]
    RETENTION_UNIT_MINUTES: _ClassVar[RetentionUnit]
    RETENTION_UNIT_HOURS: _ClassVar[RetentionUnit]
    RETENTION_UNIT_DAYS: _ClassVar[RetentionUnit]
    RETENTION_UNIT_WEEKS: _ClassVar[RetentionUnit]
    RETENTION_UNIT_MONTHS: _ClassVar[RetentionUnit]
    RETENTION_UNIT_YEARS: _ClassVar[RetentionUnit]
    RETENTION_UNIT_FOREVER: _ClassVar[RetentionUnit]
    RETENTION_UNIT_CUSTOM: _ClassVar[RetentionUnit]
RETENTION_UNIT_UNSPECIFIED: RetentionUnit
RETENTION_UNIT_MINUTES: RetentionUnit
RETENTION_UNIT_HOURS: RetentionUnit
RETENTION_UNIT_DAYS: RetentionUnit
RETENTION_UNIT_WEEKS: RetentionUnit
RETENTION_UNIT_MONTHS: RetentionUnit
RETENTION_UNIT_YEARS: RetentionUnit
RETENTION_UNIT_FOREVER: RetentionUnit
RETENTION_UNIT_CUSTOM: RetentionUnit
