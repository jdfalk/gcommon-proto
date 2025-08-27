from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteMultipleResponse(_message.Message):
    __slots__ = ("deleted_count", "failed_count", "failed_keys", "error")
    DELETED_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_KEYS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    deleted_count: int
    failed_count: int
    failed_keys: _containers.RepeatedScalarFieldContainer[str]
    error: _error_pb2.Error
    def __init__(
        self,
        deleted_count: _Optional[int] = ...,
        failed_count: _Optional[int] = ...,
        failed_keys: _Optional[_Iterable[str]] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
    ) -> None: ...
