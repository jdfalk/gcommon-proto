from gcommon.v1.common import offset_type_pb2 as _offset_type_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetOffsetRequest(_message.Message):
    __slots__ = ("queue_name", "partition_id", "consumer_group", "consumer_id", "offset_type", "metadata")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    partition_id: int
    consumer_group: str
    consumer_id: str
    offset_type: _offset_type_pb2.OffsetType
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, queue_name: _Optional[str] = ..., partition_id: _Optional[int] = ..., consumer_group: _Optional[str] = ..., consumer_id: _Optional[str] = ..., offset_type: _Optional[_Union[_offset_type_pb2.OffsetType, str]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
