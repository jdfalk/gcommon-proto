from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SamlConfig(_message.Message):
    __slots__ = ("idp_metadata_url", "sp_entity_id", "sp_acs_url", "certificate", "private_key", "allowed_domains")
    IDP_METADATA_URL_FIELD_NUMBER: _ClassVar[int]
    SP_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SP_ACS_URL_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    idp_metadata_url: str
    sp_entity_id: str
    sp_acs_url: str
    certificate: str
    private_key: str
    allowed_domains: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, idp_metadata_url: _Optional[str] = ..., sp_entity_id: _Optional[str] = ..., sp_acs_url: _Optional[str] = ..., certificate: _Optional[str] = ..., private_key: _Optional[str] = ..., allowed_domains: _Optional[_Iterable[str]] = ...) -> None: ...
