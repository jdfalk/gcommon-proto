from gcommon.v1.organization import cdn_config_pb2 as _cdn_config_pb2
from gcommon.v1.organization import domain_config_pb2 as _domain_config_pb2
from gcommon.v1.organization import load_balancer_config_pb2 as _load_balancer_config_pb2
from gcommon.v1.organization import network_acl_rule_pb2 as _network_acl_rule_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkIsolation(_message.Message):
    __slots__ = ("vpc_id", "subnet_id", "security_group_ids", "acl_rules", "dedicated_network", "load_balancer", "cdn", "domain")
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    ACL_RULES_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_NETWORK_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_FIELD_NUMBER: _ClassVar[int]
    CDN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    vpc_id: str
    subnet_id: str
    security_group_ids: _containers.RepeatedScalarFieldContainer[str]
    acl_rules: _containers.RepeatedCompositeFieldContainer[_network_acl_rule_pb2.NetworkACLRule]
    dedicated_network: bool
    load_balancer: _load_balancer_config_pb2.OrganizationLoadBalancerConfig
    cdn: _cdn_config_pb2.CDNConfig
    domain: _domain_config_pb2.DomainConfig
    def __init__(self, vpc_id: _Optional[str] = ..., subnet_id: _Optional[str] = ..., security_group_ids: _Optional[_Iterable[str]] = ..., acl_rules: _Optional[_Iterable[_Union[_network_acl_rule_pb2.NetworkACLRule, _Mapping]]] = ..., dedicated_network: bool = ..., load_balancer: _Optional[_Union[_load_balancer_config_pb2.OrganizationLoadBalancerConfig, _Mapping]] = ..., cdn: _Optional[_Union[_cdn_config_pb2.CDNConfig, _Mapping]] = ..., domain: _Optional[_Union[_domain_config_pb2.DomainConfig, _Mapping]] = ...) -> None: ...
