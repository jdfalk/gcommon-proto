from gcommon.v1.common import serialization_format_pb2 as _serialization_format_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeserializationConfig(_message.Message):
    __slots__ = ("supported_formats", "default_format", "validate_schema", "allow_unknown_fields", "custom_deserializer", "max_message_size")
    SUPPORTED_FORMATS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UNKNOWN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DESERIALIZER_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    supported_formats: _containers.RepeatedScalarFieldContainer[_serialization_format_pb2.SerializationFormat]
    default_format: _serialization_format_pb2.SerializationFormat
    validate_schema: bool
    allow_unknown_fields: bool
    custom_deserializer: str
    max_message_size: int
    def __init__(self, supported_formats: _Optional[_Iterable[_Union[_serialization_format_pb2.SerializationFormat, str]]] = ..., default_format: _Optional[_Union[_serialization_format_pb2.SerializationFormat, str]] = ..., validate_schema: bool = ..., allow_unknown_fields: bool = ..., custom_deserializer: _Optional[str] = ..., max_message_size: _Optional[int] = ...) -> None: ...
