from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AckRequest(_message.Message):
    __slots__ = ("queue_name", "receipt_handle", "metadata")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    receipt_handle: str
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, queue_name: _Optional[str] = ..., receipt_handle: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
