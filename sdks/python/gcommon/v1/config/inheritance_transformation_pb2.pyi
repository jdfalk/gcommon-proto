from gcommon.v1.common import transformation_type_pb2 as _transformation_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InheritanceTransformation(_message.Message):
    __slots__ = ("type", "expression", "parameters", "metadata")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    type: _transformation_type_pb2.TransformationType
    expression: str
    parameters: _containers.ScalarMap[str, str]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[_Union[_transformation_type_pb2.TransformationType, str]] = ..., expression: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
