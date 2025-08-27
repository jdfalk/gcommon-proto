from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class OAuth2FlowType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OAUTH2_FLOW_TYPE_UNSPECIFIED: _ClassVar[OAuth2FlowType]
    OAUTH2_FLOW_TYPE_AUTHORIZATION_CODE: _ClassVar[OAuth2FlowType]
    OAUTH2_FLOW_TYPE_IMPLICIT: _ClassVar[OAuth2FlowType]
    OAUTH2_FLOW_TYPE_CLIENT_CREDENTIALS: _ClassVar[OAuth2FlowType]
    OAUTH2_FLOW_TYPE_DEVICE_CODE: _ClassVar[OAuth2FlowType]

OAUTH2_FLOW_TYPE_UNSPECIFIED: OAuth2FlowType
OAUTH2_FLOW_TYPE_AUTHORIZATION_CODE: OAuth2FlowType
OAUTH2_FLOW_TYPE_IMPLICIT: OAuth2FlowType
OAUTH2_FLOW_TYPE_CLIENT_CREDENTIALS: OAuth2FlowType
OAUTH2_FLOW_TYPE_DEVICE_CODE: OAuth2FlowType
