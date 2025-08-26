from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupBySpec(_message.Message):
    __slots__ = ("label_keys", "time_group", "max_groups")
    LABEL_KEYS_FIELD_NUMBER: _ClassVar[int]
    TIME_GROUP_FIELD_NUMBER: _ClassVar[int]
    MAX_GROUPS_FIELD_NUMBER: _ClassVar[int]
    label_keys: _containers.RepeatedScalarFieldContainer[str]
    time_group: _duration_pb2.Duration
    max_groups: int
    def __init__(self, label_keys: _Optional[_Iterable[str]] = ..., time_group: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_groups: _Optional[int] = ...) -> None: ...
