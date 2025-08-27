from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPLATE_FORMAT_UNSPECIFIED: _ClassVar[TemplateFormat]
    TEMPLATE_FORMAT_JSON: _ClassVar[TemplateFormat]
    TEMPLATE_FORMAT_YAML: _ClassVar[TemplateFormat]
    TEMPLATE_FORMAT_TOML: _ClassVar[TemplateFormat]
    TEMPLATE_FORMAT_XML: _ClassVar[TemplateFormat]
    TEMPLATE_FORMAT_PROPERTIES: _ClassVar[TemplateFormat]
    TEMPLATE_FORMAT_INI: _ClassVar[TemplateFormat]
    TEMPLATE_FORMAT_CUSTOM: _ClassVar[TemplateFormat]

TEMPLATE_FORMAT_UNSPECIFIED: TemplateFormat
TEMPLATE_FORMAT_JSON: TemplateFormat
TEMPLATE_FORMAT_YAML: TemplateFormat
TEMPLATE_FORMAT_TOML: TemplateFormat
TEMPLATE_FORMAT_XML: TemplateFormat
TEMPLATE_FORMAT_PROPERTIES: TemplateFormat
TEMPLATE_FORMAT_INI: TemplateFormat
TEMPLATE_FORMAT_CUSTOM: TemplateFormat
