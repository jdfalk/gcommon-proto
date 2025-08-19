from gcommon.v1.common.enums import resource_status_pb2 as _resource_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OAuthClient(_message.Message):
    __slots__ = ("client_id", "client_secret", "name", "description", "client_type", "redirect_uris", "grant_types", "response_types", "scopes", "created_at", "status", "metadata", "logo_url", "website_url", "owner_user_id")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPES_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_URL_FIELD_NUMBER: _ClassVar[int]
    OWNER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    name: str
    description: str
    client_type: str
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    grant_types: _containers.RepeatedScalarFieldContainer[str]
    response_types: _containers.RepeatedScalarFieldContainer[str]
    scopes: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    status: _resource_status_pb2.ResourceStatus
    metadata: _containers.ScalarMap[str, str]
    logo_url: str
    website_url: str
    owner_user_id: str
    def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., client_type: _Optional[str] = ..., redirect_uris: _Optional[_Iterable[str]] = ..., grant_types: _Optional[_Iterable[str]] = ..., response_types: _Optional[_Iterable[str]] = ..., scopes: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[_resource_status_pb2.ResourceStatus, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., logo_url: _Optional[str] = ..., website_url: _Optional[str] = ..., owner_user_id: _Optional[str] = ...) -> None: ...
