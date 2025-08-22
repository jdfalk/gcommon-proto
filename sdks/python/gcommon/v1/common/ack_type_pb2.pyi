from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AckType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACK_TYPE_UNSPECIFIED: _ClassVar[AckType]
    ACK_TYPE_SUCCESS: _ClassVar[AckType]
    ACK_TYPE_RETRY: _ClassVar[AckType]
    ACK_TYPE_REJECT: _ClassVar[AckType]
    ACK_TYPE_TIMEOUT: _ClassVar[AckType]
ACK_TYPE_UNSPECIFIED: AckType
ACK_TYPE_SUCCESS: AckType
ACK_TYPE_RETRY: AckType
ACK_TYPE_REJECT: AckType
ACK_TYPE_TIMEOUT: AckType
