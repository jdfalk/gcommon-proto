import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartitionCommitResult(_message.Message):
    __slots__ = (
        "partition_id",
        "success",
        "committed_offset",
        "previous_offset",
        "error_message",
        "error_code",
        "commit_timestamp",
        "partition_metadata",
    )
    class PartitionMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_OFFSET_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    COMMIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PARTITION_METADATA_FIELD_NUMBER: _ClassVar[int]
    partition_id: int
    success: bool
    committed_offset: int
    previous_offset: int
    error_message: str
    error_code: str
    commit_timestamp: _timestamp_pb2.Timestamp
    partition_metadata: _containers.ScalarMap[str, str]
    def __init__(
        self,
        partition_id: _Optional[int] = ...,
        success: _Optional[bool] = ...,
        committed_offset: _Optional[int] = ...,
        previous_offset: _Optional[int] = ...,
        error_message: _Optional[str] = ...,
        error_code: _Optional[str] = ...,
        commit_timestamp: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        partition_metadata: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
