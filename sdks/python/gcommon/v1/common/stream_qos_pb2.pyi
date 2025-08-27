from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StreamQOS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAM_QOS_UNSPECIFIED: _ClassVar[StreamQOS]
    STREAM_QOS_BEST_EFFORT: _ClassVar[StreamQOS]
    STREAM_QOS_AT_LEAST_ONCE: _ClassVar[StreamQOS]
    STREAM_QOS_EXACTLY_ONCE: _ClassVar[StreamQOS]

STREAM_QOS_UNSPECIFIED: StreamQOS
STREAM_QOS_BEST_EFFORT: StreamQOS
STREAM_QOS_AT_LEAST_ONCE: StreamQOS
STREAM_QOS_EXACTLY_ONCE: StreamQOS
