from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeadLetterPolicy(_message.Message):
    __slots__ = ("dead_letter_queue", "max_delivery_attempts", "max_message_age", "include_failure_reason", "dead_letter_metadata", "enabled")
    class DeadLetterMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DEAD_LETTER_QUEUE_FIELD_NUMBER: _ClassVar[int]
    MAX_DELIVERY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGE_AGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_METADATA_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    dead_letter_queue: str
    max_delivery_attempts: int
    max_message_age: _duration_pb2.Duration
    include_failure_reason: bool
    dead_letter_metadata: _containers.ScalarMap[str, str]
    enabled: bool
    def __init__(self, dead_letter_queue: _Optional[str] = ..., max_delivery_attempts: _Optional[int] = ..., max_message_age: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., include_failure_reason: bool = ..., dead_letter_metadata: _Optional[_Mapping[str, str]] = ..., enabled: bool = ...) -> None: ...
