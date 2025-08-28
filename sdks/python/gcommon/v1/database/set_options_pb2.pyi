from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetOptions(_message.Message):
    __slots__ = ("only_if_absent", "only_if_present", "ttl", "return_previous")
    ONLY_IF_ABSENT_FIELD_NUMBER: _ClassVar[int]
    ONLY_IF_PRESENT_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    RETURN_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    only_if_absent: bool
    only_if_present: bool
    ttl: _duration_pb2.Duration
    return_previous: bool
    def __init__(self, only_if_absent: bool = ..., only_if_present: bool = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., return_previous: bool = ...) -> None: ...
