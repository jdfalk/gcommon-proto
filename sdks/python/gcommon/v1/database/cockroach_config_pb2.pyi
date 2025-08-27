from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CockroachConfig(_message.Message):
    __slots__ = (
        "host",
        "port",
        "user",
        "password",
        "database",
        "ssl_mode",
        "application_name",
        "retry_backoff_factor",
        "max_retries",
    )
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    RETRY_BACKOFF_FACTOR_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    ssl_mode: str
    application_name: str
    retry_backoff_factor: float
    max_retries: int
    def __init__(
        self,
        host: _Optional[str] = ...,
        port: _Optional[int] = ...,
        user: _Optional[str] = ...,
        password: _Optional[str] = ...,
        database: _Optional[str] = ...,
        ssl_mode: _Optional[str] = ...,
        application_name: _Optional[str] = ...,
        retry_backoff_factor: _Optional[float] = ...,
        max_retries: _Optional[int] = ...,
    ) -> None: ...
