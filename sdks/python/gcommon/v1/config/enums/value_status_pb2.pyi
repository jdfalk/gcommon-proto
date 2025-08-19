from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ValueStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALUE_STATUS_UNSPECIFIED: _ClassVar[ValueStatus]
    VALUE_STATUS_ACTIVE: _ClassVar[ValueStatus]
    VALUE_STATUS_INACTIVE: _ClassVar[ValueStatus]
    VALUE_STATUS_DRAFT: _ClassVar[ValueStatus]
    VALUE_STATUS_DEPRECATED: _ClassVar[ValueStatus]
    VALUE_STATUS_DELETED: _ClassVar[ValueStatus]
    VALUE_STATUS_ERROR: _ClassVar[ValueStatus]
    VALUE_STATUS_PENDING: _ClassVar[ValueStatus]
    VALUE_STATUS_SYNCING: _ClassVar[ValueStatus]
    VALUE_STATUS_VALIDATING: _ClassVar[ValueStatus]
VALUE_STATUS_UNSPECIFIED: ValueStatus
VALUE_STATUS_ACTIVE: ValueStatus
VALUE_STATUS_INACTIVE: ValueStatus
VALUE_STATUS_DRAFT: ValueStatus
VALUE_STATUS_DEPRECATED: ValueStatus
VALUE_STATUS_DELETED: ValueStatus
VALUE_STATUS_ERROR: ValueStatus
VALUE_STATUS_PENDING: ValueStatus
VALUE_STATUS_SYNCING: ValueStatus
VALUE_STATUS_VALIDATING: ValueStatus
