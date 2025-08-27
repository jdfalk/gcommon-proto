from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AntiAffinityScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANTI_AFFINITY_SCOPE_UNSPECIFIED: _ClassVar[AntiAffinityScope]
    ANTI_AFFINITY_SCOPE_NODE: _ClassVar[AntiAffinityScope]
    ANTI_AFFINITY_SCOPE_RACK: _ClassVar[AntiAffinityScope]
    ANTI_AFFINITY_SCOPE_DATACENTER: _ClassVar[AntiAffinityScope]
    ANTI_AFFINITY_SCOPE_REGION: _ClassVar[AntiAffinityScope]

ANTI_AFFINITY_SCOPE_UNSPECIFIED: AntiAffinityScope
ANTI_AFFINITY_SCOPE_NODE: AntiAffinityScope
ANTI_AFFINITY_SCOPE_RACK: AntiAffinityScope
ANTI_AFFINITY_SCOPE_DATACENTER: AntiAffinityScope
ANTI_AFFINITY_SCOPE_REGION: AntiAffinityScope
