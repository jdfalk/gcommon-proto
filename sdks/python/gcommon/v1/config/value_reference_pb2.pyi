from gcommon.v1.common import reference_type_pb2 as _reference_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValueReference(_message.Message):
    __slots__ = ("type", "referenced_key", "path", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_KEY_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    type: _reference_type_pb2.ReferenceType
    referenced_key: str
    path: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[_Union[_reference_type_pb2.ReferenceType, str]] = ..., referenced_key: _Optional[str] = ..., path: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
