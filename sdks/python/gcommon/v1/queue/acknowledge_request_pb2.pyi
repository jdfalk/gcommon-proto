from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcknowledgeRequest(_message.Message):
    __slots__ = ("queue_name", "receipt_handles", "metadata", "consumer_id", "processing_results", "processing_notes", "processing_times_ms", "force_acknowledge", "batch_mode")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_HANDLES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_NOTES_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    FORCE_ACKNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    BATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    receipt_handles: _containers.RepeatedScalarFieldContainer[str]
    metadata: _request_metadata_pb2.RequestMetadata
    consumer_id: str
    processing_results: _containers.RepeatedScalarFieldContainer[str]
    processing_notes: _containers.RepeatedScalarFieldContainer[str]
    processing_times_ms: _containers.RepeatedScalarFieldContainer[int]
    force_acknowledge: bool
    batch_mode: bool
    def __init__(self, queue_name: _Optional[str] = ..., receipt_handles: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., consumer_id: _Optional[str] = ..., processing_results: _Optional[_Iterable[str]] = ..., processing_notes: _Optional[_Iterable[str]] = ..., processing_times_ms: _Optional[_Iterable[int]] = ..., force_acknowledge: _Optional[bool] = ..., batch_mode: _Optional[bool] = ...) -> None: ...
