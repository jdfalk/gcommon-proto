from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PullRequest(_message.Message):
    __slots__ = ("metadata", "queue_name", "visibility_timeout_seconds")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    queue_name: str
    visibility_timeout_seconds: int
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., queue_name: _Optional[str] = ..., visibility_timeout_seconds: _Optional[int] = ...) -> None: ...
