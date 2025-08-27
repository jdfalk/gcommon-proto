from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SchemaEvolutionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEMA_EVOLUTION_STRATEGY_UNSPECIFIED: _ClassVar[SchemaEvolutionStrategy]
    SCHEMA_EVOLUTION_STRATEGY_NONE: _ClassVar[SchemaEvolutionStrategy]
    SCHEMA_EVOLUTION_STRATEGY_FORWARD: _ClassVar[SchemaEvolutionStrategy]
    SCHEMA_EVOLUTION_STRATEGY_BACKWARD: _ClassVar[SchemaEvolutionStrategy]
    SCHEMA_EVOLUTION_STRATEGY_FULL: _ClassVar[SchemaEvolutionStrategy]
    SCHEMA_EVOLUTION_STRATEGY_NONE_CHECK: _ClassVar[SchemaEvolutionStrategy]
SCHEMA_EVOLUTION_STRATEGY_UNSPECIFIED: SchemaEvolutionStrategy
SCHEMA_EVOLUTION_STRATEGY_NONE: SchemaEvolutionStrategy
SCHEMA_EVOLUTION_STRATEGY_FORWARD: SchemaEvolutionStrategy
SCHEMA_EVOLUTION_STRATEGY_BACKWARD: SchemaEvolutionStrategy
SCHEMA_EVOLUTION_STRATEGY_FULL: SchemaEvolutionStrategy
SCHEMA_EVOLUTION_STRATEGY_NONE_CHECK: SchemaEvolutionStrategy
