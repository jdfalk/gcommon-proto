from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMultipleResponse(_message.Message):
    __slots__ = ("values", "missing_keys", "error")
    class ValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[bytes] = ...
        ) -> None: ...

    VALUES_FIELD_NUMBER: _ClassVar[int]
    MISSING_KEYS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    values: _containers.ScalarMap[str, bytes]
    missing_keys: _containers.RepeatedScalarFieldContainer[str]
    error: _error_pb2.Error
    def __init__(
        self,
        values: _Optional[_Mapping[str, bytes]] = ...,
        missing_keys: _Optional[_Iterable[str]] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
    ) -> None: ...
