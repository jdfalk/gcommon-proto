from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SortField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_FIELD_UNSPECIFIED: _ClassVar[SortField]
    SORT_FIELD_NAME: _ClassVar[SortField]
    SORT_FIELD_TYPE: _ClassVar[SortField]
    SORT_FIELD_CREATED_AT: _ClassVar[SortField]
    SORT_FIELD_STATE: _ClassVar[SortField]
    SORT_FIELD_HEALTH: _ClassVar[SortField]
SORT_FIELD_UNSPECIFIED: SortField
SORT_FIELD_NAME: SortField
SORT_FIELD_TYPE: SortField
SORT_FIELD_CREATED_AT: SortField
SORT_FIELD_STATE: SortField
SORT_FIELD_HEALTH: SortField
