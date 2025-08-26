from gcommon.v1.common import metrics_api_key_config_pb2 as _metrics_api_key_config_pb2
from gcommon.v1.organization import integration_pb2 as _integration_pb2
from gcommon.v1.organization import o_auth_app_config_pb2 as _o_auth_app_config_pb2
from gcommon.v1.organization import webhook_config_pb2 as _webhook_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IntegrationSettings(_message.Message):
    __slots__ = ("enabled_integrations", "webhooks", "api_keys", "oauth_apps")
    ENABLED_INTEGRATIONS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
    API_KEYS_FIELD_NUMBER: _ClassVar[int]
    OAUTH_APPS_FIELD_NUMBER: _ClassVar[int]
    enabled_integrations: _containers.RepeatedCompositeFieldContainer[_integration_pb2.Integration]
    webhooks: _containers.RepeatedCompositeFieldContainer[_webhook_config_pb2.WebhookConfig]
    api_keys: _containers.RepeatedCompositeFieldContainer[_metrics_api_key_config_pb2.MetricsAPIKeyConfig]
    oauth_apps: _containers.RepeatedCompositeFieldContainer[_o_auth_app_config_pb2.OAuthAppConfig]
    def __init__(self, enabled_integrations: _Optional[_Iterable[_Union[_integration_pb2.Integration, _Mapping]]] = ..., webhooks: _Optional[_Iterable[_Union[_webhook_config_pb2.WebhookConfig, _Mapping]]] = ..., api_keys: _Optional[_Iterable[_Union[_metrics_api_key_config_pb2.MetricsAPIKeyConfig, _Mapping]]] = ..., oauth_apps: _Optional[_Iterable[_Union[_o_auth_app_config_pb2.OAuthAppConfig, _Mapping]]] = ...) -> None: ...
