from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class NackErrorCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NACK_ERROR_CATEGORY_UNSPECIFIED: _ClassVar[NackErrorCategory]
    NACK_ERROR_CATEGORY_TEMPORARY: _ClassVar[NackErrorCategory]
    NACK_ERROR_CATEGORY_PERMANENT: _ClassVar[NackErrorCategory]
    NACK_ERROR_CATEGORY_CONFIGURATION: _ClassVar[NackErrorCategory]
    NACK_ERROR_CATEGORY_NETWORK: _ClassVar[NackErrorCategory]
    NACK_ERROR_CATEGORY_AUTH: _ClassVar[NackErrorCategory]
    NACK_ERROR_CATEGORY_RATE_LIMIT: _ClassVar[NackErrorCategory]
NACK_ERROR_CATEGORY_UNSPECIFIED: NackErrorCategory
NACK_ERROR_CATEGORY_TEMPORARY: NackErrorCategory
NACK_ERROR_CATEGORY_PERMANENT: NackErrorCategory
NACK_ERROR_CATEGORY_CONFIGURATION: NackErrorCategory
NACK_ERROR_CATEGORY_NETWORK: NackErrorCategory
NACK_ERROR_CATEGORY_AUTH: NackErrorCategory
NACK_ERROR_CATEGORY_RATE_LIMIT: NackErrorCategory
