from gcommon.v1.common import compression_algorithm_pb2 as _compression_algorithm_pb2
from gcommon.v1.common import serialization_format_pb2 as _serialization_format_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FormatOptions(_message.Message):
    __slots__ = ("format", "options", "enable_compression", "compression_algorithm", "max_message_size")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    format: _serialization_format_pb2.SerializationFormat
    options: _containers.ScalarMap[str, str]
    enable_compression: bool
    compression_algorithm: _compression_algorithm_pb2.CompressionAlgorithm
    max_message_size: int
    def __init__(self, format: _Optional[_Union[_serialization_format_pb2.SerializationFormat, str]] = ..., options: _Optional[_Mapping[str, str]] = ..., enable_compression: _Optional[bool] = ..., compression_algorithm: _Optional[_Union[_compression_algorithm_pb2.CompressionAlgorithm, str]] = ..., max_message_size: _Optional[int] = ...) -> None: ...
