from gcommon.v1.queue import topic_info_pb2 as _topic_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListTopicsResponse(_message.Message):
    __slots__ = ("topics", "next_page_token", "total_count")
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedCompositeFieldContainer[_topic_info_pb2.TopicInfo]
    next_page_token: str
    total_count: int
    def __init__(
        self,
        topics: _Optional[_Iterable[_Union[_topic_info_pb2.TopicInfo, _Mapping]]] = ...,
        next_page_token: _Optional[str] = ...,
        total_count: _Optional[int] = ...,
    ) -> None: ...
