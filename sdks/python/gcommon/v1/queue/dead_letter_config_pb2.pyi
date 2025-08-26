from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeadLetterConfig(_message.Message):
    __slots__ = ("enabled", "dead_letter_queue_name", "max_delivery_attempts", "ttl", "preserve_headers", "additional_metadata")
    class AdditionalMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_DELIVERY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    dead_letter_queue_name: str
    max_delivery_attempts: int
    ttl: _duration_pb2.Duration
    preserve_headers: bool
    additional_metadata: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., dead_letter_queue_name: _Optional[str] = ..., max_delivery_attempts: _Optional[int] = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., preserve_headers: bool = ..., additional_metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
