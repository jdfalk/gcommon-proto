from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FormatterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FORMATTER_TYPE_UNSPECIFIED: _ClassVar[FormatterType]
    FORMATTER_TYPE_TEXT: _ClassVar[FormatterType]
    FORMATTER_TYPE_JSON: _ClassVar[FormatterType]
    FORMATTER_TYPE_XML: _ClassVar[FormatterType]
    FORMATTER_TYPE_CUSTOM: _ClassVar[FormatterType]

FORMATTER_TYPE_UNSPECIFIED: FormatterType
FORMATTER_TYPE_TEXT: FormatterType
FORMATTER_TYPE_JSON: FormatterType
FORMATTER_TYPE_XML: FormatterType
FORMATTER_TYPE_CUSTOM: FormatterType
