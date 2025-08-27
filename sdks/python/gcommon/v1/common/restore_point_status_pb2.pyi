from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RestorePointStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTORE_POINT_STATUS_UNSPECIFIED: _ClassVar[RestorePointStatus]
    RESTORE_POINT_STATUS_CREATING: _ClassVar[RestorePointStatus]
    RESTORE_POINT_STATUS_ACTIVE: _ClassVar[RestorePointStatus]
    RESTORE_POINT_STATUS_EXPIRED: _ClassVar[RestorePointStatus]
    RESTORE_POINT_STATUS_DELETED: _ClassVar[RestorePointStatus]
    RESTORE_POINT_STATUS_ERROR: _ClassVar[RestorePointStatus]

RESTORE_POINT_STATUS_UNSPECIFIED: RestorePointStatus
RESTORE_POINT_STATUS_CREATING: RestorePointStatus
RESTORE_POINT_STATUS_ACTIVE: RestorePointStatus
RESTORE_POINT_STATUS_EXPIRED: RestorePointStatus
RESTORE_POINT_STATUS_DELETED: RestorePointStatus
RESTORE_POINT_STATUS_ERROR: RestorePointStatus
