from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigDiffEntry(_message.Message):
    __slots__ = ("key", "old_value", "new_value", "change_type", "namespace")
    KEY_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    key: str
    old_value: _any_pb2.Any
    new_value: _any_pb2.Any
    change_type: str
    namespace: str
    def __init__(self, key: _Optional[str] = ..., old_value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., new_value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., change_type: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...
