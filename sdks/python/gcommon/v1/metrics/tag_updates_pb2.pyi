from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TagUpdates(_message.Message):
    __slots__ = ("tag_updates", "tag_removes")
    class TagUpdatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    TAG_UPDATES_FIELD_NUMBER: _ClassVar[int]
    TAG_REMOVES_FIELD_NUMBER: _ClassVar[int]
    tag_updates: _containers.ScalarMap[str, str]
    tag_removes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        tag_updates: _Optional[_Mapping[str, str]] = ...,
        tag_removes: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
