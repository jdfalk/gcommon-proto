from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SecretStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECRET_STATUS_UNSPECIFIED: _ClassVar[SecretStatus]
    SECRET_STATUS_ACTIVE: _ClassVar[SecretStatus]
    SECRET_STATUS_INACTIVE: _ClassVar[SecretStatus]
    SECRET_STATUS_EXPIRED: _ClassVar[SecretStatus]
    SECRET_STATUS_ROTATED: _ClassVar[SecretStatus]
    SECRET_STATUS_COMPROMISED: _ClassVar[SecretStatus]
    SECRET_STATUS_DELETED: _ClassVar[SecretStatus]
    SECRET_STATUS_ERROR: _ClassVar[SecretStatus]

SECRET_STATUS_UNSPECIFIED: SecretStatus
SECRET_STATUS_ACTIVE: SecretStatus
SECRET_STATUS_INACTIVE: SecretStatus
SECRET_STATUS_EXPIRED: SecretStatus
SECRET_STATUS_ROTATED: SecretStatus
SECRET_STATUS_COMPROMISED: SecretStatus
SECRET_STATUS_DELETED: SecretStatus
SECRET_STATUS_ERROR: SecretStatus
