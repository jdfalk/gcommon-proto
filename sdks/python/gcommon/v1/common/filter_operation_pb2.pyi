from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FilterOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILTER_OPERATION_UNSPECIFIED: _ClassVar[FilterOperation]
    FILTER_OPERATION_EQUALS: _ClassVar[FilterOperation]
    FILTER_OPERATION_NOT_EQUALS: _ClassVar[FilterOperation]
    FILTER_OPERATION_GREATER_THAN: _ClassVar[FilterOperation]
    FILTER_OPERATION_LESS_THAN: _ClassVar[FilterOperation]
    FILTER_OPERATION_GREATER_THAN_OR_EQUAL: _ClassVar[FilterOperation]
    FILTER_OPERATION_LESS_THAN_OR_EQUAL: _ClassVar[FilterOperation]
    FILTER_OPERATION_CONTAINS: _ClassVar[FilterOperation]
    FILTER_OPERATION_STARTS_WITH: _ClassVar[FilterOperation]
    FILTER_OPERATION_ENDS_WITH: _ClassVar[FilterOperation]
    FILTER_OPERATION_IN: _ClassVar[FilterOperation]
    FILTER_OPERATION_NOT_IN: _ClassVar[FilterOperation]
FILTER_OPERATION_UNSPECIFIED: FilterOperation
FILTER_OPERATION_EQUALS: FilterOperation
FILTER_OPERATION_NOT_EQUALS: FilterOperation
FILTER_OPERATION_GREATER_THAN: FilterOperation
FILTER_OPERATION_LESS_THAN: FilterOperation
FILTER_OPERATION_GREATER_THAN_OR_EQUAL: FilterOperation
FILTER_OPERATION_LESS_THAN_OR_EQUAL: FilterOperation
FILTER_OPERATION_CONTAINS: FilterOperation
FILTER_OPERATION_STARTS_WITH: FilterOperation
FILTER_OPERATION_ENDS_WITH: FilterOperation
FILTER_OPERATION_IN: FilterOperation
FILTER_OPERATION_NOT_IN: FilterOperation
