from gcommon.v1.common import key_value_pb2 as _key_value_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OriginConfig(_message.Message):
    __slots__ = ("domain_name", "origin_path", "protocol_policy", "custom_headers")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_PATH_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_POLICY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_HEADERS_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    origin_path: str
    protocol_policy: str
    custom_headers: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    def __init__(self, domain_name: _Optional[str] = ..., origin_path: _Optional[str] = ..., protocol_policy: _Optional[str] = ..., custom_headers: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ...) -> None: ...
