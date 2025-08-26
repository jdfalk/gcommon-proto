from gcommon.v1.database import migration_info_pb2 as _migration_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMigrationsResponse(_message.Message):
    __slots__ = ("migrations",)
    MIGRATIONS_FIELD_NUMBER: _ClassVar[int]
    migrations: _containers.RepeatedCompositeFieldContainer[_migration_info_pb2.MigrationInfo]
    def __init__(self, migrations: _Optional[_Iterable[_Union[_migration_info_pb2.MigrationInfo, _Mapping]]] = ...) -> None: ...
