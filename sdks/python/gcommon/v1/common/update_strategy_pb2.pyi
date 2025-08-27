from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_STRATEGY_UNSPECIFIED: _ClassVar[UpdateStrategy]
    UPDATE_STRATEGY_ROLLING: _ClassVar[UpdateStrategy]
    UPDATE_STRATEGY_BLUE_GREEN: _ClassVar[UpdateStrategy]
    UPDATE_STRATEGY_IMMEDIATE: _ClassVar[UpdateStrategy]
    UPDATE_STRATEGY_SCHEDULED: _ClassVar[UpdateStrategy]

UPDATE_STRATEGY_UNSPECIFIED: UpdateStrategy
UPDATE_STRATEGY_ROLLING: UpdateStrategy
UPDATE_STRATEGY_BLUE_GREEN: UpdateStrategy
UPDATE_STRATEGY_IMMEDIATE: UpdateStrategy
UPDATE_STRATEGY_SCHEDULED: UpdateStrategy
