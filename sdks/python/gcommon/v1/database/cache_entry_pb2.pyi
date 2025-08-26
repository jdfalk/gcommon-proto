from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheEntry(_message.Message):
    __slots__ = ("key", "value", "created_at", "last_accessed_at", "expires_at", "access_count", "size_bytes", "metadata", "namespace")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _any_pb2.Any
    created_at: _timestamp_pb2.Timestamp
    last_accessed_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    access_count: int
    size_bytes: int
    metadata: _containers.ScalarMap[str, str]
    namespace: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_accessed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., access_count: _Optional[int] = ..., size_bytes: _Optional[int] = ..., metadata: _Optional[_Mapping[str, str]] = ..., namespace: _Optional[str] = ...) -> None: ...
