from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from gcommon.v1.queue import failed_ack_pb2 as _failed_ack_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchAckResponse(_message.Message):
    __slots__ = ("success", "acknowledged_count", "failed_count", "failed_acks", "metadata", "batch_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_ACKS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    acknowledged_count: int
    failed_count: int
    failed_acks: _containers.RepeatedCompositeFieldContainer[_failed_ack_pb2.FailedAck]
    metadata: _response_metadata_pb2.ResponseMetadata
    batch_id: str
    def __init__(self, success: bool = ..., acknowledged_count: _Optional[int] = ..., failed_count: _Optional[int] = ..., failed_acks: _Optional[_Iterable[_Union[_failed_ack_pb2.FailedAck, _Mapping]]] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ..., batch_id: _Optional[str] = ...) -> None: ...
