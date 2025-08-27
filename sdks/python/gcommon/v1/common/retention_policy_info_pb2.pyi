from gcommon.v1.common import (
    metrics_retention_policy_config_pb2 as _metrics_retention_policy_config_pb2,
)
from gcommon.v1.common import retention_policy_pb2 as _retention_policy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetentionPolicyInfo(_message.Message):
    __slots__ = ("policy", "config")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    policy: _retention_policy_pb2.MetricsRetentionPolicy
    config: _metrics_retention_policy_config_pb2.MetricsRetentionPolicyConfig
    def __init__(
        self,
        policy: _Optional[
            _Union[_retention_policy_pb2.MetricsRetentionPolicy, str]
        ] = ...,
        config: _Optional[
            _Union[
                _metrics_retention_policy_config_pb2.MetricsRetentionPolicyConfig,
                _Mapping,
            ]
        ] = ...,
    ) -> None: ...
