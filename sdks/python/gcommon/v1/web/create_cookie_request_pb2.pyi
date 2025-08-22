from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.common import same_site_policy_pb2 as _same_site_policy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCookieRequest(_message.Message):
    __slots__ = ("name", "value", "domain", "path", "expires", "max_age", "secure", "http_only", "same_site", "metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    SECURE_FIELD_NUMBER: _ClassVar[int]
    HTTP_ONLY_FIELD_NUMBER: _ClassVar[int]
    SAME_SITE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    domain: str
    path: str
    expires: _timestamp_pb2.Timestamp
    max_age: int
    secure: bool
    http_only: bool
    same_site: _same_site_policy_pb2.SameSitePolicy
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., domain: _Optional[str] = ..., path: _Optional[str] = ..., expires: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., max_age: _Optional[int] = ..., secure: bool = ..., http_only: bool = ..., same_site: _Optional[_Union[_same_site_policy_pb2.SameSitePolicy, str]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
