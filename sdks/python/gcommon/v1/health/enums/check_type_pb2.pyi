from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CheckType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHECK_TYPE_UNSPECIFIED: _ClassVar[CheckType]
    CHECK_TYPE_HEALTH: _ClassVar[CheckType]
    CHECK_TYPE_READINESS: _ClassVar[CheckType]
    CHECK_TYPE_LIVENESS: _ClassVar[CheckType]
    CHECK_TYPE_DEPENDENCY: _ClassVar[CheckType]
    CHECK_TYPE_RESOURCE: _ClassVar[CheckType]
    CHECK_TYPE_NETWORK: _ClassVar[CheckType]
    CHECK_TYPE_DATABASE: _ClassVar[CheckType]
    CHECK_TYPE_CUSTOM: _ClassVar[CheckType]
CHECK_TYPE_UNSPECIFIED: CheckType
CHECK_TYPE_HEALTH: CheckType
CHECK_TYPE_READINESS: CheckType
CHECK_TYPE_LIVENESS: CheckType
CHECK_TYPE_DEPENDENCY: CheckType
CHECK_TYPE_RESOURCE: CheckType
CHECK_TYPE_NETWORK: CheckType
CHECK_TYPE_DATABASE: CheckType
CHECK_TYPE_CUSTOM: CheckType
