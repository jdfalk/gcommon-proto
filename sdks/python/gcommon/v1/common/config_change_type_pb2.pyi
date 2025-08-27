from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPLATE_CHANGE_TYPE_UNSPECIFIED: _ClassVar[TemplateChangeType]
    TEMPLATE_CHANGE_TYPE_FEATURE: _ClassVar[TemplateChangeType]
    TEMPLATE_CHANGE_TYPE_BUGFIX: _ClassVar[TemplateChangeType]
    TEMPLATE_CHANGE_TYPE_ENHANCEMENT: _ClassVar[TemplateChangeType]
    TEMPLATE_CHANGE_TYPE_DEPRECATED: _ClassVar[TemplateChangeType]
    TEMPLATE_CHANGE_TYPE_SECURITY: _ClassVar[TemplateChangeType]
    CHANGE_TYPE_BREAKING: _ClassVar[TemplateChangeType]
TEMPLATE_CHANGE_TYPE_UNSPECIFIED: TemplateChangeType
TEMPLATE_CHANGE_TYPE_FEATURE: TemplateChangeType
TEMPLATE_CHANGE_TYPE_BUGFIX: TemplateChangeType
TEMPLATE_CHANGE_TYPE_ENHANCEMENT: TemplateChangeType
TEMPLATE_CHANGE_TYPE_DEPRECATED: TemplateChangeType
TEMPLATE_CHANGE_TYPE_SECURITY: TemplateChangeType
CHANGE_TYPE_BREAKING: TemplateChangeType
