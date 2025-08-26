from gcommon.v1.database import database_info_pb2 as _database_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDatabaseInfoResponse(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _database_info_pb2.DatabaseInfo
    def __init__(self, info: _Optional[_Union[_database_info_pb2.DatabaseInfo, _Mapping]] = ...) -> None: ...
