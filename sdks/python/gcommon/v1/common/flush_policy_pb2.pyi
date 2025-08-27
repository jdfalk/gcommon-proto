from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FlushPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FLUSH_POLICY_UNSPECIFIED: _ClassVar[FlushPolicy]
    FLUSH_POLICY_IMMEDIATE: _ClassVar[FlushPolicy]
    FLUSH_POLICY_BATCH: _ClassVar[FlushPolicy]
    FLUSH_POLICY_TIMED: _ClassVar[FlushPolicy]
    FLUSH_POLICY_BUFFER_FULL: _ClassVar[FlushPolicy]
    FLUSH_POLICY_MANUAL: _ClassVar[FlushPolicy]

FLUSH_POLICY_UNSPECIFIED: FlushPolicy
FLUSH_POLICY_IMMEDIATE: FlushPolicy
FLUSH_POLICY_BATCH: FlushPolicy
FLUSH_POLICY_TIMED: FlushPolicy
FLUSH_POLICY_BUFFER_FULL: FlushPolicy
FLUSH_POLICY_MANUAL: FlushPolicy
