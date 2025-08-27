from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RollbackMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROLLBACK_METHOD_UNSPECIFIED: _ClassVar[RollbackMethod]
    ROLLBACK_METHOD_VALUE_RESTORE: _ClassVar[RollbackMethod]
    ROLLBACK_METHOD_VERSION_RESTORE: _ClassVar[RollbackMethod]
    ROLLBACK_METHOD_SNAPSHOT_RESTORE: _ClassVar[RollbackMethod]
    ROLLBACK_METHOD_MANUAL: _ClassVar[RollbackMethod]

ROLLBACK_METHOD_UNSPECIFIED: RollbackMethod
ROLLBACK_METHOD_VALUE_RESTORE: RollbackMethod
ROLLBACK_METHOD_VERSION_RESTORE: RollbackMethod
ROLLBACK_METHOD_SNAPSHOT_RESTORE: RollbackMethod
ROLLBACK_METHOD_MANUAL: RollbackMethod
