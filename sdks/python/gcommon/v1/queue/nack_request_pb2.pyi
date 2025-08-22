from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.queue import nack_error_pb2 as _nack_error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NackRequest(_message.Message):
    __slots__ = ("ack_token", "requeue", "reason", "error", "requeue_delay_seconds", "max_retries", "metadata")
    ACK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REQUEUE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REQUEUE_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ack_token: str
    requeue: bool
    reason: str
    error: _nack_error_pb2.NackError
    requeue_delay_seconds: int
    max_retries: int
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, ack_token: _Optional[str] = ..., requeue: bool = ..., reason: _Optional[str] = ..., error: _Optional[_Union[_nack_error_pb2.NackError, _Mapping]] = ..., requeue_delay_seconds: _Optional[int] = ..., max_retries: _Optional[int] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
