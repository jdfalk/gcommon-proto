from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.config import config_schema_pb2 as _config_schema_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetConfigSchemaRequest(_message.Message):
    __slots__ = ("namespace", "schema", "metadata")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    schema: _config_schema_pb2.ConfigSchema
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, namespace: _Optional[str] = ..., schema: _Optional[_Union[_config_schema_pb2.ConfigSchema, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
