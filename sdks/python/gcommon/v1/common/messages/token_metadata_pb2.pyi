from gcommon.v1.common.enums import token_type_pb2 as _token_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenMetadata(_message.Message):
    __slots__ = ("token_id", "type", "subject", "audience", "scopes", "issued_at", "expires_at", "not_before", "issuer")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    NOT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    type: _token_type_pb2.TokenType
    subject: str
    audience: _containers.RepeatedScalarFieldContainer[str]
    scopes: _containers.RepeatedScalarFieldContainer[str]
    issued_at: int
    expires_at: int
    not_before: int
    issuer: str
    def __init__(self, token_id: _Optional[str] = ..., type: _Optional[_Union[_token_type_pb2.TokenType, str]] = ..., subject: _Optional[str] = ..., audience: _Optional[_Iterable[str]] = ..., scopes: _Optional[_Iterable[str]] = ..., issued_at: _Optional[int] = ..., expires_at: _Optional[int] = ..., not_before: _Optional[int] = ..., issuer: _Optional[str] = ...) -> None: ...
