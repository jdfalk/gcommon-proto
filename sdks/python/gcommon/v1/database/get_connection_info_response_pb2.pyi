from gcommon.v1.database import connection_pool_info_pb2 as _connection_pool_info_pb2
from gcommon.v1.database import database_info_pb2 as _database_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConnectionInfoResponse(_message.Message):
    __slots__ = ("pool_info", "database_info")
    POOL_INFO_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INFO_FIELD_NUMBER: _ClassVar[int]
    pool_info: _connection_pool_info_pb2.ConnectionPoolInfo
    database_info: _database_info_pb2.DatabaseInfo
    def __init__(
        self,
        pool_info: _Optional[
            _Union[_connection_pool_info_pb2.ConnectionPoolInfo, _Mapping]
        ] = ...,
        database_info: _Optional[
            _Union[_database_info_pb2.DatabaseInfo, _Mapping]
        ] = ...,
    ) -> None: ...
