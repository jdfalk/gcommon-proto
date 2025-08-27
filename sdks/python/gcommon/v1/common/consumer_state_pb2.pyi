from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSUMER_STATE_UNSPECIFIED: _ClassVar[ConsumerState]
    CONSUMER_STATE_ACTIVE: _ClassVar[ConsumerState]
    CONSUMER_STATE_IDLE: _ClassVar[ConsumerState]
    CONSUMER_STATE_PAUSED: _ClassVar[ConsumerState]
    CONSUMER_STATE_STOPPED: _ClassVar[ConsumerState]
    CONSUMER_STATE_ERROR: _ClassVar[ConsumerState]
    CONSUMER_STATE_CONNECTING: _ClassVar[ConsumerState]
    CONSUMER_STATE_DISCONNECTED: _ClassVar[ConsumerState]

CONSUMER_STATE_UNSPECIFIED: ConsumerState
CONSUMER_STATE_ACTIVE: ConsumerState
CONSUMER_STATE_IDLE: ConsumerState
CONSUMER_STATE_PAUSED: ConsumerState
CONSUMER_STATE_STOPPED: ConsumerState
CONSUMER_STATE_ERROR: ConsumerState
CONSUMER_STATE_CONNECTING: ConsumerState
CONSUMER_STATE_DISCONNECTED: ConsumerState
