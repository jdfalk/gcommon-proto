from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SameSitePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAME_SITE_POLICY_UNSPECIFIED: _ClassVar[SameSitePolicy]
    SAME_SITE_POLICY_NONE: _ClassVar[SameSitePolicy]
    SAME_SITE_POLICY_LAX: _ClassVar[SameSitePolicy]
    SAME_SITE_POLICY_STRICT: _ClassVar[SameSitePolicy]
SAME_SITE_POLICY_UNSPECIFIED: SameSitePolicy
SAME_SITE_POLICY_NONE: SameSitePolicy
SAME_SITE_POLICY_LAX: SameSitePolicy
SAME_SITE_POLICY_STRICT: SameSitePolicy
