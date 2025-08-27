from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ColumnMetadata(_message.Message):
    __slots__ = ("name", "type", "nullable", "size", "scale", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    nullable: bool
    size: int
    scale: int
    metadata: _containers.ScalarMap[str, str]
    def __init__(
        self,
        name: _Optional[str] = ...,
        type: _Optional[str] = ...,
        nullable: _Optional[bool] = ...,
        size: _Optional[int] = ...,
        scale: _Optional[int] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
