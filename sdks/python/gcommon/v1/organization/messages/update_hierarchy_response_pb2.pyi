from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.organization.messages import organization_hierarchy_pb2 as _organization_hierarchy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateHierarchyResponse(_message.Message):
    __slots__ = ("errors", "success", "hierarchy")
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.Error]
    success: bool
    hierarchy: _organization_hierarchy_pb2.OrganizationHierarchy
    def __init__(self, errors: _Optional[_Iterable[_Union[_error_pb2.Error, _Mapping]]] = ..., success: bool = ..., hierarchy: _Optional[_Union[_organization_hierarchy_pb2.OrganizationHierarchy, _Mapping]] = ...) -> None: ...
