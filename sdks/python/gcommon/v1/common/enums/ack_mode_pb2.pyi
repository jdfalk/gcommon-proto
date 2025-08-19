from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AckMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACK_MODE_UNSPECIFIED: _ClassVar[AckMode]
    ACK_MODE_MANUAL: _ClassVar[AckMode]
    ACK_MODE_AUTO: _ClassVar[AckMode]
    ACK_MODE_CLIENT: _ClassVar[AckMode]
ACK_MODE_UNSPECIFIED: AckMode
ACK_MODE_MANUAL: AckMode
ACK_MODE_AUTO: AckMode
ACK_MODE_CLIENT: AckMode
