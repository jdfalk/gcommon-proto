from gcommon.v1.common import batch_priority_pb2 as _batch_priority_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsBatchOptions(_message.Message):
    __slots__ = ("parallel_processing", "max_concurrency", "deduplicate", "return_detailed_results", "timeout_seconds", "transactional", "priority")
    PARALLEL_PROCESSING_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATE_FIELD_NUMBER: _ClassVar[int]
    RETURN_DETAILED_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONAL_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    parallel_processing: bool
    max_concurrency: int
    deduplicate: bool
    return_detailed_results: bool
    timeout_seconds: int
    transactional: bool
    priority: _batch_priority_pb2.BatchPriority
    def __init__(self, parallel_processing: _Optional[bool] = ..., max_concurrency: _Optional[int] = ..., deduplicate: _Optional[bool] = ..., return_detailed_results: _Optional[bool] = ..., timeout_seconds: _Optional[int] = ..., transactional: _Optional[bool] = ..., priority: _Optional[_Union[_batch_priority_pb2.BatchPriority, str]] = ...) -> None: ...
