from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrependRequest(_message.Message):
    __slots__ = ("key", "value", "namespace", "metadata")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _any_pb2.Any
    namespace: str
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., namespace: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
