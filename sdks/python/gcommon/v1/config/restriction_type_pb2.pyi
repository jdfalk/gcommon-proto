from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RestrictionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTRICTION_TYPE_UNSPECIFIED: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_IP_ADDRESS: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_TIME_RANGE: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_LOCATION: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_USER_AGENT: _ClassVar[RestrictionType]
    RESTRICTION_TYPE_CUSTOM: _ClassVar[RestrictionType]
RESTRICTION_TYPE_UNSPECIFIED: RestrictionType
RESTRICTION_TYPE_IP_ADDRESS: RestrictionType
RESTRICTION_TYPE_TIME_RANGE: RestrictionType
RESTRICTION_TYPE_LOCATION: RestrictionType
RESTRICTION_TYPE_USER_AGENT: RestrictionType
RESTRICTION_TYPE_CUSTOM: RestrictionType
