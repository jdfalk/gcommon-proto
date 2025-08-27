from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AckLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACK_LEVEL_UNSPECIFIED: _ClassVar[AckLevel]
    ACK_LEVEL_NONE: _ClassVar[AckLevel]
    ACK_LEVEL_LEADER: _ClassVar[AckLevel]
    ACK_LEVEL_ALL: _ClassVar[AckLevel]
    ACK_LEVEL_MAJORITY: _ClassVar[AckLevel]
ACK_LEVEL_UNSPECIFIED: AckLevel
ACK_LEVEL_NONE: AckLevel
ACK_LEVEL_LEADER: AckLevel
ACK_LEVEL_ALL: AckLevel
ACK_LEVEL_MAJORITY: AckLevel
