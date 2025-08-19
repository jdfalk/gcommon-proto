from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MergeStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MERGE_STRATEGY_UNSPECIFIED: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_REPLACE: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_MERGE_DEEP: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_MERGE_SHALLOW: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_ARRAY_CONCAT: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_ARRAY_REPLACE: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_ARRAY_MERGE: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_CUSTOM: _ClassVar[MergeStrategy]
MERGE_STRATEGY_UNSPECIFIED: MergeStrategy
MERGE_STRATEGY_REPLACE: MergeStrategy
MERGE_STRATEGY_MERGE_DEEP: MergeStrategy
MERGE_STRATEGY_MERGE_SHALLOW: MergeStrategy
MERGE_STRATEGY_ARRAY_CONCAT: MergeStrategy
MERGE_STRATEGY_ARRAY_REPLACE: MergeStrategy
MERGE_STRATEGY_ARRAY_MERGE: MergeStrategy
MERGE_STRATEGY_CUSTOM: MergeStrategy
