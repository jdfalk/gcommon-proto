from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MessageState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_STATE_UNSPECIFIED: _ClassVar[MessageState]
    MESSAGE_STATE_PENDING: _ClassVar[MessageState]
    MESSAGE_STATE_DELIVERED: _ClassVar[MessageState]
    MESSAGE_STATE_ACKNOWLEDGED: _ClassVar[MessageState]
    MESSAGE_STATE_FAILED: _ClassVar[MessageState]
    MESSAGE_STATE_DEAD_LETTER: _ClassVar[MessageState]
    MESSAGE_STATE_EXPIRED: _ClassVar[MessageState]

MESSAGE_STATE_UNSPECIFIED: MessageState
MESSAGE_STATE_PENDING: MessageState
MESSAGE_STATE_DELIVERED: MessageState
MESSAGE_STATE_ACKNOWLEDGED: MessageState
MESSAGE_STATE_FAILED: MessageState
MESSAGE_STATE_DEAD_LETTER: MessageState
MESSAGE_STATE_EXPIRED: MessageState
