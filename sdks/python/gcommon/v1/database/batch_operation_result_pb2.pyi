from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchOperationResult(_message.Message):
    __slots__ = ("success", "affected_rows", "generated_keys", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_ROWS_FIELD_NUMBER: _ClassVar[int]
    GENERATED_KEYS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    affected_rows: int
    generated_keys: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    error: _error_pb2.Error
    def __init__(self, success: bool = ..., affected_rows: _Optional[int] = ..., generated_keys: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
