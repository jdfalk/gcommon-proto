from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumerClient(_message.Message):
    __slots__ = (
        "client_id",
        "client_host",
        "client_app",
        "client_version",
        "client_rack",
    )
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_HOST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_APP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_RACK_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_host: str
    client_app: str
    client_version: str
    client_rack: str
    def __init__(
        self,
        client_id: _Optional[str] = ...,
        client_host: _Optional[str] = ...,
        client_app: _Optional[str] = ...,
        client_version: _Optional[str] = ...,
        client_rack: _Optional[str] = ...,
    ) -> None: ...
