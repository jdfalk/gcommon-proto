from gcommon.v1.database.enums import database_status_code_pb2 as _database_status_code_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseStatus(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: _database_status_code_pb2.DatabaseStatusCode
    message: str
    def __init__(self, code: _Optional[_Union[_database_status_code_pb2.DatabaseStatusCode, str]] = ..., message: _Optional[str] = ...) -> None: ...
