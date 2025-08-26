from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMultipleConfigResponse(_message.Message):
    __slots__ = ("results", "error")
    class ResultsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.ScalarMap[str, bool]
    error: _error_pb2.Error
    def __init__(self, results: _Optional[_Mapping[str, bool]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
