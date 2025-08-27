from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CompressionAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPRESSION_ALGORITHM_UNSPECIFIED: _ClassVar[CompressionAlgorithm]
    COMPRESSION_ALGORITHM_NONE: _ClassVar[CompressionAlgorithm]
    COMPRESSION_ALGORITHM_GZIP: _ClassVar[CompressionAlgorithm]
    COMPRESSION_ALGORITHM_LZ4: _ClassVar[CompressionAlgorithm]
    COMPRESSION_ALGORITHM_SNAPPY: _ClassVar[CompressionAlgorithm]
    COMPRESSION_ALGORITHM_ZSTD: _ClassVar[CompressionAlgorithm]
    COMPRESSION_ALGORITHM_BROTLI: _ClassVar[CompressionAlgorithm]

COMPRESSION_ALGORITHM_UNSPECIFIED: CompressionAlgorithm
COMPRESSION_ALGORITHM_NONE: CompressionAlgorithm
COMPRESSION_ALGORITHM_GZIP: CompressionAlgorithm
COMPRESSION_ALGORITHM_LZ4: CompressionAlgorithm
COMPRESSION_ALGORITHM_SNAPPY: CompressionAlgorithm
COMPRESSION_ALGORITHM_ZSTD: CompressionAlgorithm
COMPRESSION_ALGORITHM_BROTLI: CompressionAlgorithm
