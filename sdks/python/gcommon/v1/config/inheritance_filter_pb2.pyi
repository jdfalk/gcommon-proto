from gcommon.v1.common import filter_type_pb2 as _filter_type_pb2
from gcommon.v1.config import filter_action_pb2 as _filter_action_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InheritanceFilter(_message.Message):
    __slots__ = ("type", "expression", "action", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    type: _filter_type_pb2.LogFilterType
    expression: str
    action: _filter_action_pb2.FilterAction
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[_Union[_filter_type_pb2.LogFilterType, str]] = ..., expression: _Optional[str] = ..., action: _Optional[_Union[_filter_action_pb2.FilterAction, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
