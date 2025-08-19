from gcommon.v1.common.messages import config_value_pb2 as _config_value_pb2
from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetConfigRequest(_message.Message):
    __slots__ = ("key", "value", "namespace", "metadata", "encrypt", "tags", "request_metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ENCRYPT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _config_value_pb2.ConfigValue
    namespace: str
    metadata: _containers.ScalarMap[str, str]
    encrypt: bool
    tags: _containers.RepeatedScalarFieldContainer[str]
    request_metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_config_value_pb2.ConfigValue, _Mapping]] = ..., namespace: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., encrypt: bool = ..., tags: _Optional[_Iterable[str]] = ..., request_metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
