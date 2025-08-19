from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPLATE_STATUS_UNSPECIFIED: _ClassVar[TemplateStatus]
    TEMPLATE_STATUS_DRAFT: _ClassVar[TemplateStatus]
    TEMPLATE_STATUS_ACTIVE: _ClassVar[TemplateStatus]
    TEMPLATE_STATUS_DEPRECATED: _ClassVar[TemplateStatus]
    TEMPLATE_STATUS_ARCHIVED: _ClassVar[TemplateStatus]
    TEMPLATE_STATUS_DELETED: _ClassVar[TemplateStatus]
TEMPLATE_STATUS_UNSPECIFIED: TemplateStatus
TEMPLATE_STATUS_DRAFT: TemplateStatus
TEMPLATE_STATUS_ACTIVE: TemplateStatus
TEMPLATE_STATUS_DEPRECATED: TemplateStatus
TEMPLATE_STATUS_ARCHIVED: TemplateStatus
TEMPLATE_STATUS_DELETED: TemplateStatus
