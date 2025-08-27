from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RestorePointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTORE_POINT_TYPE_UNSPECIFIED: _ClassVar[RestorePointType]
    RESTORE_POINT_TYPE_MANUAL: _ClassVar[RestorePointType]
    RESTORE_POINT_TYPE_AUTOMATIC: _ClassVar[RestorePointType]
    RESTORE_POINT_TYPE_SCHEDULED: _ClassVar[RestorePointType]
    RESTORE_POINT_TYPE_PRE_CHANGE: _ClassVar[RestorePointType]
    RESTORE_POINT_TYPE_MILESTONE: _ClassVar[RestorePointType]
    RESTORE_POINT_TYPE_BACKUP: _ClassVar[RestorePointType]
RESTORE_POINT_TYPE_UNSPECIFIED: RestorePointType
RESTORE_POINT_TYPE_MANUAL: RestorePointType
RESTORE_POINT_TYPE_AUTOMATIC: RestorePointType
RESTORE_POINT_TYPE_SCHEDULED: RestorePointType
RESTORE_POINT_TYPE_PRE_CHANGE: RestorePointType
RESTORE_POINT_TYPE_MILESTONE: RestorePointType
RESTORE_POINT_TYPE_BACKUP: RestorePointType
