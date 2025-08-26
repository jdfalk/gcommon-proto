import datetime

from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DecrementRequest(_message.Message):
    __slots__ = ("key", "delta", "initial_value", "ttl", "namespace", "metadata")
    KEY_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    key: str
    delta: int
    initial_value: int
    ttl: _duration_pb2.Duration
    namespace: str
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, key: _Optional[str] = ..., delta: _Optional[int] = ..., initial_value: _Optional[int] = ..., ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., namespace: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
