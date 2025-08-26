from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommitOffsetRequest(_message.Message):
    __slots__ = ("queue_name", "consumer_group", "offset", "metadata")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    consumer_group: str
    offset: int
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, queue_name: _Optional[str] = ..., consumer_group: _Optional[str] = ..., offset: _Optional[int] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
