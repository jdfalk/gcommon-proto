from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RegistrationAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGISTRATION_ACTION_UNSPECIFIED: _ClassVar[RegistrationAction]
    REGISTRATION_ACTION_CREATED: _ClassVar[RegistrationAction]
    REGISTRATION_ACTION_UPDATED: _ClassVar[RegistrationAction]
    REGISTRATION_ACTION_REPLACED: _ClassVar[RegistrationAction]
    REGISTRATION_ACTION_NO_CHANGE: _ClassVar[RegistrationAction]
REGISTRATION_ACTION_UNSPECIFIED: RegistrationAction
REGISTRATION_ACTION_CREATED: RegistrationAction
REGISTRATION_ACTION_UPDATED: RegistrationAction
REGISTRATION_ACTION_REPLACED: RegistrationAction
REGISTRATION_ACTION_NO_CHANGE: RegistrationAction
