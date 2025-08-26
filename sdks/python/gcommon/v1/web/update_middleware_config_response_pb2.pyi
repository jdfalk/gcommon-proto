from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateMiddlewareConfigResponse(_message.Message):
    __slots__ = ("metadata", "updated")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    metadata: _response_metadata_pb2.ResponseMetadata
    updated: bool
    def __init__(self, metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ..., updated: bool = ...) -> None: ...
