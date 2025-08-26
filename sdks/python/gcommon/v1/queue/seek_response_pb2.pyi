from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeekResponse(_message.Message):
    __slots__ = ("success", "position", "offset", "partition_id", "error_message", "metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    position: int
    offset: int
    partition_id: int
    error_message: str
    metadata: _response_metadata_pb2.ResponseMetadata
    def __init__(self, success: _Optional[bool] = ..., position: _Optional[int] = ..., offset: _Optional[int] = ..., partition_id: _Optional[int] = ..., error_message: _Optional[str] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...
