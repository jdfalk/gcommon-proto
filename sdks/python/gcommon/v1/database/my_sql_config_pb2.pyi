from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MySQLConfig(_message.Message):
    __slots__ = ("dsn", "max_open_conns", "max_idle_conns", "connect_timeout_seconds")
    DSN_FIELD_NUMBER: _ClassVar[int]
    MAX_OPEN_CONNS_FIELD_NUMBER: _ClassVar[int]
    MAX_IDLE_CONNS_FIELD_NUMBER: _ClassVar[int]
    CONNECT_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    dsn: str
    max_open_conns: int
    max_idle_conns: int
    connect_timeout_seconds: int
    def __init__(
        self,
        dsn: _Optional[str] = ...,
        max_open_conns: _Optional[int] = ...,
        max_idle_conns: _Optional[int] = ...,
        connect_timeout_seconds: _Optional[int] = ...,
    ) -> None: ...
