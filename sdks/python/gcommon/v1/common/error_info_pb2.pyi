from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorInfo(_message.Message):
    __slots__ = ("message", "type", "stack_trace", "code", "context", "causes")
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CAUSES_FIELD_NUMBER: _ClassVar[int]
    message: str
    type: str
    stack_trace: str
    code: str
    context: _containers.ScalarMap[str, str]
    causes: _containers.RepeatedCompositeFieldContainer[ErrorInfo]
    def __init__(self, message: _Optional[str] = ..., type: _Optional[str] = ..., stack_trace: _Optional[str] = ..., code: _Optional[str] = ..., context: _Optional[_Mapping[str, str]] = ..., causes: _Optional[_Iterable[_Union[ErrorInfo, _Mapping]]] = ...) -> None: ...
