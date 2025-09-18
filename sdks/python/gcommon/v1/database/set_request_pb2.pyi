import datetime

from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetRequest(_message.Message):
    __slots__ = ("key", "value", "namespace", "ttl", "metadata", "overwrite", "entry_metadata")
    class EntryMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_METADATA_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _any_pb2.Any
    namespace: str
    ttl: _duration_pb2.Duration
    metadata: _request_metadata_pb2.RequestMetadata
    overwrite: bool
    entry_metadata: _containers.ScalarMap[str, str]
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., namespace: _Optional[str] = ..., ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., overwrite: _Optional[bool] = ..., entry_metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
