from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResumeQueueRequest(_message.Message):
    __slots__ = (
        "queue_name",
        "reason",
        "metadata",
        "partition_ids",
        "resume_from_last_position",
    )
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PARTITION_IDS_FIELD_NUMBER: _ClassVar[int]
    RESUME_FROM_LAST_POSITION_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    reason: str
    metadata: _request_metadata_pb2.RequestMetadata
    partition_ids: _containers.RepeatedScalarFieldContainer[int]
    resume_from_last_position: bool
    def __init__(
        self,
        queue_name: _Optional[str] = ...,
        reason: _Optional[str] = ...,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
        partition_ids: _Optional[_Iterable[int]] = ...,
        resume_from_last_position: _Optional[bool] = ...,
    ) -> None: ...
