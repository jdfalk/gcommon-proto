from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class NumericFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NUMERIC_FORMAT_UNSPECIFIED: _ClassVar[NumericFormat]
    NUMERIC_FORMAT_DEFAULT: _ClassVar[NumericFormat]
    NUMERIC_FORMAT_SCIENTIFIC: _ClassVar[NumericFormat]
    NUMERIC_FORMAT_ENGINEERING: _ClassVar[NumericFormat]
    NUMERIC_FORMAT_PERCENTAGE: _ClassVar[NumericFormat]
NUMERIC_FORMAT_UNSPECIFIED: NumericFormat
NUMERIC_FORMAT_DEFAULT: NumericFormat
NUMERIC_FORMAT_SCIENTIFIC: NumericFormat
NUMERIC_FORMAT_ENGINEERING: NumericFormat
NUMERIC_FORMAT_PERCENTAGE: NumericFormat
