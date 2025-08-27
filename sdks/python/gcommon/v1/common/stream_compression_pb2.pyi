from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StreamCompression(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAM_COMPRESSION_UNSPECIFIED: _ClassVar[StreamCompression]
    STREAM_COMPRESSION_NONE: _ClassVar[StreamCompression]
    STREAM_COMPRESSION_GZIP: _ClassVar[StreamCompression]
    STREAM_COMPRESSION_SNAPPY: _ClassVar[StreamCompression]
    STREAM_COMPRESSION_LZ4: _ClassVar[StreamCompression]

STREAM_COMPRESSION_UNSPECIFIED: StreamCompression
STREAM_COMPRESSION_NONE: StreamCompression
STREAM_COMPRESSION_GZIP: StreamCompression
STREAM_COMPRESSION_SNAPPY: StreamCompression
STREAM_COMPRESSION_LZ4: StreamCompression
