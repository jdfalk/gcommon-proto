from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CheckType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHECK_TYPE_UNSPECIFIED: _ClassVar[CheckType]
    CHECK_TYPE_LIVENESS: _ClassVar[CheckType]
    CHECK_TYPE_READINESS: _ClassVar[CheckType]
    CHECK_TYPE_STARTUP: _ClassVar[CheckType]
    CHECK_TYPE_COMPONENT: _ClassVar[CheckType]
    CHECK_TYPE_DEPENDENCY: _ClassVar[CheckType]

CHECK_TYPE_UNSPECIFIED: CheckType
CHECK_TYPE_LIVENESS: CheckType
CHECK_TYPE_READINESS: CheckType
CHECK_TYPE_STARTUP: CheckType
CHECK_TYPE_COMPONENT: CheckType
CHECK_TYPE_DEPENDENCY: CheckType
