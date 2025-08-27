from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseStatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_STATUS_CODE_UNSPECIFIED: _ClassVar[DatabaseStatusCode]
    DATABASE_STATUS_CODE_OK: _ClassVar[DatabaseStatusCode]
    DATABASE_STATUS_CODE_ERROR: _ClassVar[DatabaseStatusCode]

DATABASE_STATUS_CODE_UNSPECIFIED: DatabaseStatusCode
DATABASE_STATUS_CODE_OK: DatabaseStatusCode
DATABASE_STATUS_CODE_ERROR: DatabaseStatusCode
