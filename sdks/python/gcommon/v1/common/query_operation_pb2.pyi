from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class QueryOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUERY_OPERATION_UNSPECIFIED: _ClassVar[QueryOperation]
    QUERY_OPERATION_SELECT: _ClassVar[QueryOperation]
    QUERY_OPERATION_GROUP_BY: _ClassVar[QueryOperation]
    QUERY_OPERATION_SUM: _ClassVar[QueryOperation]
    QUERY_OPERATION_AVG: _ClassVar[QueryOperation]
    QUERY_OPERATION_MIN: _ClassVar[QueryOperation]
    QUERY_OPERATION_MAX: _ClassVar[QueryOperation]
    QUERY_OPERATION_COUNT: _ClassVar[QueryOperation]
    QUERY_OPERATION_RATE: _ClassVar[QueryOperation]
    QUERY_OPERATION_INCREASE: _ClassVar[QueryOperation]
    QUERY_OPERATION_SORT: _ClassVar[QueryOperation]
    QUERY_OPERATION_LIMIT: _ClassVar[QueryOperation]
    QUERY_OPERATION_JOIN: _ClassVar[QueryOperation]

QUERY_OPERATION_UNSPECIFIED: QueryOperation
QUERY_OPERATION_SELECT: QueryOperation
QUERY_OPERATION_GROUP_BY: QueryOperation
QUERY_OPERATION_SUM: QueryOperation
QUERY_OPERATION_AVG: QueryOperation
QUERY_OPERATION_MIN: QueryOperation
QUERY_OPERATION_MAX: QueryOperation
QUERY_OPERATION_COUNT: QueryOperation
QUERY_OPERATION_RATE: QueryOperation
QUERY_OPERATION_INCREASE: QueryOperation
QUERY_OPERATION_SORT: QueryOperation
QUERY_OPERATION_LIMIT: QueryOperation
QUERY_OPERATION_JOIN: QueryOperation
