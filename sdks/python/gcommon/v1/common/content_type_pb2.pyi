from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_TYPE_UNSPECIFIED: _ClassVar[ContentType]
    CONTENT_TYPE_HTML: _ClassVar[ContentType]
    CONTENT_TYPE_JSON: _ClassVar[ContentType]
    CONTENT_TYPE_XML: _ClassVar[ContentType]
    CONTENT_TYPE_TEXT: _ClassVar[ContentType]
    CONTENT_TYPE_BINARY: _ClassVar[ContentType]
CONTENT_TYPE_UNSPECIFIED: ContentType
CONTENT_TYPE_HTML: ContentType
CONTENT_TYPE_JSON: ContentType
CONTENT_TYPE_XML: ContentType
CONTENT_TYPE_TEXT: ContentType
CONTENT_TYPE_BINARY: ContentType
