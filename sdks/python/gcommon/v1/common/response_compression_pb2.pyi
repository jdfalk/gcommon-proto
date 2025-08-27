from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseCompression(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESPONSE_COMPRESSION_UNSPECIFIED: _ClassVar[ResponseCompression]
    RESPONSE_COMPRESSION_NONE: _ClassVar[ResponseCompression]
    RESPONSE_COMPRESSION_GZIP: _ClassVar[ResponseCompression]
    RESPONSE_COMPRESSION_SNAPPY: _ClassVar[ResponseCompression]

RESPONSE_COMPRESSION_UNSPECIFIED: ResponseCompression
RESPONSE_COMPRESSION_NONE: ResponseCompression
RESPONSE_COMPRESSION_GZIP: ResponseCompression
RESPONSE_COMPRESSION_SNAPPY: ResponseCompression
