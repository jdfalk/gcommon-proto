from gcommon.v1.common.enums import check_type_pb2 as _check_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthCheckAllRequest(_message.Message):
    __slots__ = ("types", "include_details", "timeout_seconds")
    TYPES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedScalarFieldContainer[_check_type_pb2.CheckType]
    include_details: bool
    timeout_seconds: int
    def __init__(self, types: _Optional[_Iterable[_Union[_check_type_pb2.CheckType, str]]] = ..., include_details: bool = ..., timeout_seconds: _Optional[int] = ...) -> None: ...
