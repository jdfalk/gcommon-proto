from gcommon.v1.queue.messages import preserved_stats_pb2 as _preserved_stats_pb2
from gcommon.v1.queue.messages import reset_details_pb2 as _reset_details_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResetQueueStatsResponse(_message.Message):
    __slots__ = ("success", "queue_id", "reset_at", "preserved_stats", "reset_stat_types", "preserved_stat_types", "error_message", "error_code", "warnings", "reset_details", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    RESET_AT_FIELD_NUMBER: _ClassVar[int]
    PRESERVED_STATS_FIELD_NUMBER: _ClassVar[int]
    RESET_STAT_TYPES_FIELD_NUMBER: _ClassVar[int]
    PRESERVED_STAT_TYPES_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    RESET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    queue_id: str
    reset_at: _timestamp_pb2.Timestamp
    preserved_stats: _preserved_stats_pb2.PreservedStats
    reset_stat_types: _containers.RepeatedScalarFieldContainer[str]
    preserved_stat_types: _containers.RepeatedScalarFieldContainer[str]
    error_message: str
    error_code: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    reset_details: _reset_details_pb2.ResetDetails
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, success: bool = ..., queue_id: _Optional[str] = ..., reset_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., preserved_stats: _Optional[_Union[_preserved_stats_pb2.PreservedStats, _Mapping]] = ..., reset_stat_types: _Optional[_Iterable[str]] = ..., preserved_stat_types: _Optional[_Iterable[str]] = ..., error_message: _Optional[str] = ..., error_code: _Optional[str] = ..., warnings: _Optional[_Iterable[str]] = ..., reset_details: _Optional[_Union[_reset_details_pb2.ResetDetails, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
