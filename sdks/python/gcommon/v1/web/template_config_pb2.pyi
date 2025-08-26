from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateConfig(_message.Message):
    __slots__ = ("directory", "extension", "reload", "functions")
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    RELOAD_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    directory: str
    extension: str
    reload: bool
    functions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, directory: _Optional[str] = ..., extension: _Optional[str] = ..., reload: _Optional[bool] = ..., functions: _Optional[_Iterable[str]] = ...) -> None: ...
