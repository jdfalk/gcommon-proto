from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TopMetrics(_message.Message):
    __slots__ = ("most_active", "largest_by_volume", "highest_errors", "most_queried", "slowest_performing", "most_resource_intensive")
    MOST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LARGEST_BY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_ERRORS_FIELD_NUMBER: _ClassVar[int]
    MOST_QUERIED_FIELD_NUMBER: _ClassVar[int]
    SLOWEST_PERFORMING_FIELD_NUMBER: _ClassVar[int]
    MOST_RESOURCE_INTENSIVE_FIELD_NUMBER: _ClassVar[int]
    most_active: _containers.RepeatedScalarFieldContainer[str]
    largest_by_volume: _containers.RepeatedScalarFieldContainer[str]
    highest_errors: _containers.RepeatedScalarFieldContainer[str]
    most_queried: _containers.RepeatedScalarFieldContainer[str]
    slowest_performing: _containers.RepeatedScalarFieldContainer[str]
    most_resource_intensive: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, most_active: _Optional[_Iterable[str]] = ..., largest_by_volume: _Optional[_Iterable[str]] = ..., highest_errors: _Optional[_Iterable[str]] = ..., most_queried: _Optional[_Iterable[str]] = ..., slowest_performing: _Optional[_Iterable[str]] = ..., most_resource_intensive: _Optional[_Iterable[str]] = ...) -> None: ...
