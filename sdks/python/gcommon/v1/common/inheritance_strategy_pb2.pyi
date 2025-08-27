from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class InheritanceStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INHERITANCE_STRATEGY_UNSPECIFIED: _ClassVar[InheritanceStrategy]
    INHERITANCE_STRATEGY_OVERRIDE: _ClassVar[InheritanceStrategy]
    INHERITANCE_STRATEGY_MERGE: _ClassVar[InheritanceStrategy]
    INHERITANCE_STRATEGY_FALLBACK: _ClassVar[InheritanceStrategy]
    INHERITANCE_STRATEGY_PRIORITY: _ClassVar[InheritanceStrategy]
    INHERITANCE_STRATEGY_WEIGHTED: _ClassVar[InheritanceStrategy]

INHERITANCE_STRATEGY_UNSPECIFIED: InheritanceStrategy
INHERITANCE_STRATEGY_OVERRIDE: InheritanceStrategy
INHERITANCE_STRATEGY_MERGE: InheritanceStrategy
INHERITANCE_STRATEGY_FALLBACK: InheritanceStrategy
INHERITANCE_STRATEGY_PRIORITY: InheritanceStrategy
INHERITANCE_STRATEGY_WEIGHTED: InheritanceStrategy
