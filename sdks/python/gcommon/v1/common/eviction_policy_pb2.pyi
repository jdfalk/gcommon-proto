from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EvictionPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVICTION_POLICY_UNSPECIFIED: _ClassVar[EvictionPolicy]
    EVICTION_POLICY_LRU: _ClassVar[EvictionPolicy]
    EVICTION_POLICY_LFU: _ClassVar[EvictionPolicy]
    EVICTION_POLICY_FIFO: _ClassVar[EvictionPolicy]
    EVICTION_POLICY_RANDOM: _ClassVar[EvictionPolicy]
EVICTION_POLICY_UNSPECIFIED: EvictionPolicy
EVICTION_POLICY_LRU: EvictionPolicy
EVICTION_POLICY_LFU: EvictionPolicy
EVICTION_POLICY_FIFO: EvictionPolicy
EVICTION_POLICY_RANDOM: EvictionPolicy
