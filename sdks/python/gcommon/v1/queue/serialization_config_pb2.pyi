from gcommon.v1.common import compression_algorithm_pb2 as _compression_algorithm_pb2
from gcommon.v1.common import serialization_format_pb2 as _serialization_format_pb2
from gcommon.v1.queue import format_options_pb2 as _format_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SerializationConfig(_message.Message):
    __slots__ = (
        "default_format",
        "supported_formats",
        "auto_detect_format",
        "default_compression",
        "supported_compressions",
        "auto_detect_compression",
        "format_options",
        "validate_on_deserialize",
        "max_message_size",
        "backwards_compatible",
    )
    class FormatOptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _format_options_pb2.FormatOptions
        def __init__(
            self,
            key: _Optional[str] = ...,
            value: _Optional[_Union[_format_options_pb2.FormatOptions, _Mapping]] = ...,
        ) -> None: ...

    DEFAULT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_FORMATS_FIELD_NUMBER: _ClassVar[int]
    AUTO_DETECT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_COMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_DETECT_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    FORMAT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ON_DESERIALIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKWARDS_COMPATIBLE_FIELD_NUMBER: _ClassVar[int]
    default_format: _serialization_format_pb2.SerializationFormat
    supported_formats: _containers.RepeatedScalarFieldContainer[
        _serialization_format_pb2.SerializationFormat
    ]
    auto_detect_format: bool
    default_compression: _compression_algorithm_pb2.CompressionAlgorithm
    supported_compressions: _containers.RepeatedScalarFieldContainer[
        _compression_algorithm_pb2.CompressionAlgorithm
    ]
    auto_detect_compression: bool
    format_options: _containers.MessageMap[str, _format_options_pb2.FormatOptions]
    validate_on_deserialize: bool
    max_message_size: int
    backwards_compatible: bool
    def __init__(
        self,
        default_format: _Optional[
            _Union[_serialization_format_pb2.SerializationFormat, str]
        ] = ...,
        supported_formats: _Optional[
            _Iterable[_Union[_serialization_format_pb2.SerializationFormat, str]]
        ] = ...,
        auto_detect_format: _Optional[bool] = ...,
        default_compression: _Optional[
            _Union[_compression_algorithm_pb2.CompressionAlgorithm, str]
        ] = ...,
        supported_compressions: _Optional[
            _Iterable[_Union[_compression_algorithm_pb2.CompressionAlgorithm, str]]
        ] = ...,
        auto_detect_compression: _Optional[bool] = ...,
        format_options: _Optional[
            _Mapping[str, _format_options_pb2.FormatOptions]
        ] = ...,
        validate_on_deserialize: _Optional[bool] = ...,
        max_message_size: _Optional[int] = ...,
        backwards_compatible: _Optional[bool] = ...,
    ) -> None: ...
