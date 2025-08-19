from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTopicInfoRequest(_message.Message):
    __slots__ = ("topic_name", "include_stats", "include_partitions", "include_consumer_groups", "metadata")
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STATS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CONSUMER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    topic_name: str
    include_stats: bool
    include_partitions: bool
    include_consumer_groups: bool
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, topic_name: _Optional[str] = ..., include_stats: bool = ..., include_partitions: bool = ..., include_consumer_groups: bool = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
