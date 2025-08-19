from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ComparisonOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPARISON_OPERATOR_UNSPECIFIED: _ClassVar[ComparisonOperator]
    COMPARISON_OPERATOR_EQUAL: _ClassVar[ComparisonOperator]
    COMPARISON_OPERATOR_NOT_EQUAL: _ClassVar[ComparisonOperator]
    COMPARISON_OPERATOR_GREATER_THAN: _ClassVar[ComparisonOperator]
    COMPARISON_OPERATOR_GREATER_THAN_OR_EQUAL: _ClassVar[ComparisonOperator]
    COMPARISON_OPERATOR_LESS_THAN: _ClassVar[ComparisonOperator]
    COMPARISON_OPERATOR_LESS_THAN_OR_EQUAL: _ClassVar[ComparisonOperator]
COMPARISON_OPERATOR_UNSPECIFIED: ComparisonOperator
COMPARISON_OPERATOR_EQUAL: ComparisonOperator
COMPARISON_OPERATOR_NOT_EQUAL: ComparisonOperator
COMPARISON_OPERATOR_GREATER_THAN: ComparisonOperator
COMPARISON_OPERATOR_GREATER_THAN_OR_EQUAL: ComparisonOperator
COMPARISON_OPERATOR_LESS_THAN: ComparisonOperator
COMPARISON_OPERATOR_LESS_THAN_OR_EQUAL: ComparisonOperator
