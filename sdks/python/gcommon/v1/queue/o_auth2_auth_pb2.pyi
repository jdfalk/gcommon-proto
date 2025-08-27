from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OAuth2Auth(_message.Message):
    __slots__ = ("token_endpoint", "client_id", "client_secret", "scopes", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    token_endpoint: str
    client_id: str
    client_secret: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    parameters: _containers.ScalarMap[str, str]
    def __init__(
        self,
        token_endpoint: _Optional[str] = ...,
        client_id: _Optional[str] = ...,
        client_secret: _Optional[str] = ...,
        scopes: _Optional[_Iterable[str]] = ...,
        parameters: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
