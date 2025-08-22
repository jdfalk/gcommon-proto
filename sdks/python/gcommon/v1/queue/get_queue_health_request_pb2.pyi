from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetQueueHealthRequest(_message.Message):
    __slots__ = ("queue_names", "include_details")
    QUEUE_NAMES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    queue_names: _containers.RepeatedScalarFieldContainer[str]
    include_details: bool
    def __init__(self, queue_names: _Optional[_Iterable[str]] = ..., include_details: bool = ...) -> None: ...
