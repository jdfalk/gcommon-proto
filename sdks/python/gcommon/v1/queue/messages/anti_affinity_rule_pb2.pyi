from gcommon.v1.queue.enums import anti_affinity_scope_pb2 as _anti_affinity_scope_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AntiAffinityRule(_message.Message):
    __slots__ = ("label_key", "label_values", "scope")
    LABEL_KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_VALUES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    label_key: str
    label_values: _containers.RepeatedScalarFieldContainer[str]
    scope: _anti_affinity_scope_pb2.AntiAffinityScope
    def __init__(self, label_key: _Optional[str] = ..., label_values: _Optional[_Iterable[str]] = ..., scope: _Optional[_Union[_anti_affinity_scope_pb2.AntiAffinityScope, str]] = ...) -> None: ...
