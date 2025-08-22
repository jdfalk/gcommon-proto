from gcommon.v1.queue import publish_result_pb2 as _publish_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchPublishResponse(_message.Message):
    __slots__ = ("results", "total_attempted", "successful_count", "failed_count", "error")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ATTEMPTED_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_publish_result_pb2.PublishResult]
    total_attempted: int
    successful_count: int
    failed_count: int
    error: str
    def __init__(self, results: _Optional[_Iterable[_Union[_publish_result_pb2.PublishResult, _Mapping]]] = ..., total_attempted: _Optional[int] = ..., successful_count: _Optional[int] = ..., failed_count: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...
