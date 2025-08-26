from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetadataUpdate(_message.Message):
    __slots__ = ("add_metadata", "remove_metadata", "replace_metadata", "operation_type")
    class AddMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ReplaceMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ADD_METADATA_FIELD_NUMBER: _ClassVar[int]
    REMOVE_METADATA_FIELD_NUMBER: _ClassVar[int]
    REPLACE_METADATA_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    add_metadata: _containers.ScalarMap[str, str]
    remove_metadata: _containers.RepeatedScalarFieldContainer[str]
    replace_metadata: _containers.ScalarMap[str, str]
    operation_type: str
    def __init__(self, add_metadata: _Optional[_Mapping[str, str]] = ..., remove_metadata: _Optional[_Iterable[str]] = ..., replace_metadata: _Optional[_Mapping[str, str]] = ..., operation_type: _Optional[str] = ...) -> None: ...
