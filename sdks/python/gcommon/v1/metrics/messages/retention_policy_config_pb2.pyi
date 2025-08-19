from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetentionPolicyConfig(_message.Message):
    __slots__ = ("duration", "storage_tier", "compression")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TIER_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    storage_tier: str
    compression: str
    def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., storage_tier: _Optional[str] = ..., compression: _Optional[str] = ...) -> None: ...
