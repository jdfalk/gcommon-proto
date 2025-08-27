from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LogCompressionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPRESSION_TYPE_UNSPECIFIED: _ClassVar[LogCompressionType]
    COMPRESSION_TYPE_NONE: _ClassVar[LogCompressionType]
    COMPRESSION_TYPE_GZIP: _ClassVar[LogCompressionType]
    COMPRESSION_TYPE_ZIP: _ClassVar[LogCompressionType]
    COMPRESSION_TYPE_BZIP2: _ClassVar[LogCompressionType]
    COMPRESSION_TYPE_TAR_GZ: _ClassVar[LogCompressionType]

COMPRESSION_TYPE_UNSPECIFIED: LogCompressionType
COMPRESSION_TYPE_NONE: LogCompressionType
COMPRESSION_TYPE_GZIP: LogCompressionType
COMPRESSION_TYPE_ZIP: LogCompressionType
COMPRESSION_TYPE_BZIP2: LogCompressionType
COMPRESSION_TYPE_TAR_GZ: LogCompressionType
