from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartServerRequest(_message.Message):
    __slots__ = ("server_id", "metadata")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, server_id: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
