from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CircuitBreakerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CIRCUIT_BREAKER_STATE_UNSPECIFIED: _ClassVar[CircuitBreakerState]
    CIRCUIT_BREAKER_STATE_CLOSED: _ClassVar[CircuitBreakerState]
    CIRCUIT_BREAKER_STATE_OPEN: _ClassVar[CircuitBreakerState]
    CIRCUIT_BREAKER_STATE_HALF_OPEN: _ClassVar[CircuitBreakerState]
CIRCUIT_BREAKER_STATE_UNSPECIFIED: CircuitBreakerState
CIRCUIT_BREAKER_STATE_CLOSED: CircuitBreakerState
CIRCUIT_BREAKER_STATE_OPEN: CircuitBreakerState
CIRCUIT_BREAKER_STATE_HALF_OPEN: CircuitBreakerState
