from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.database import migration_script_pb2 as _migration_script_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunMigrationRequest(_message.Message):
    __slots__ = ("database", "scripts", "metadata")
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    database: str
    scripts: _containers.RepeatedCompositeFieldContainer[_migration_script_pb2.MigrationScript]
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, database: _Optional[str] = ..., scripts: _Optional[_Iterable[_Union[_migration_script_pb2.MigrationScript, _Mapping]]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
