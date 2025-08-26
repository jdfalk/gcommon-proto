from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.database import batch_operation_result_pb2 as _batch_operation_result_pb2
from gcommon.v1.database import batch_stats_pb2 as _batch_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteBatchResponse(_message.Message):
    __slots__ = ("results", "stats", "error")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_batch_operation_result_pb2.BatchOperationResult]
    stats: _batch_stats_pb2.DatabaseBatchStats
    error: _error_pb2.Error
    def __init__(self, results: _Optional[_Iterable[_Union[_batch_operation_result_pb2.BatchOperationResult, _Mapping]]] = ..., stats: _Optional[_Union[_batch_stats_pb2.DatabaseBatchStats, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
