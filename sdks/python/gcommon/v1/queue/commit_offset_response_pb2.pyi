import datetime

from gcommon.v1.queue import partition_commit_result_pb2 as _partition_commit_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommitOffsetResponse(_message.Message):
    __slots__ = ("success", "error_message", "error_code", "partition_results", "committed_count", "failed_count", "commit_timestamp", "consumer_generation", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GENERATION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    error_code: str
    partition_results: _containers.RepeatedCompositeFieldContainer[_partition_commit_result_pb2.PartitionCommitResult]
    committed_count: int
    failed_count: int
    commit_timestamp: _timestamp_pb2.Timestamp
    consumer_generation: int
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, success: _Optional[bool] = ..., error_message: _Optional[str] = ..., error_code: _Optional[str] = ..., partition_results: _Optional[_Iterable[_Union[_partition_commit_result_pb2.PartitionCommitResult, _Mapping]]] = ..., committed_count: _Optional[int] = ..., failed_count: _Optional[int] = ..., commit_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., consumer_generation: _Optional[int] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
