from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CachePublishRequest(_message.Message):
    __slots__ = ("topic", "payload", "metadata")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    topic: str
    payload: _any_pb2.Any
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, topic: _Optional[str] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
