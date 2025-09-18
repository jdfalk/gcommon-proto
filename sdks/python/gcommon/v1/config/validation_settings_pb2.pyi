from gcommon.v1.common import config_retry_settings_pb2 as _config_retry_settings_pb2
from gcommon.v1.config import validation_rule_pb2 as _validation_rule_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationSettings(_message.Message):
    __slots__ = ("enabled", "rules", "validate_on_change", "validate_on_access", "timeout_seconds", "retry", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ON_CHANGE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ON_ACCESS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    RETRY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    rules: _containers.RepeatedCompositeFieldContainer[_validation_rule_pb2.ValidationRule]
    validate_on_change: bool
    validate_on_access: bool
    timeout_seconds: int
    retry: _config_retry_settings_pb2.ConfigRetrySettings
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, enabled: _Optional[bool] = ..., rules: _Optional[_Iterable[_Union[_validation_rule_pb2.ValidationRule, _Mapping]]] = ..., validate_on_change: _Optional[bool] = ..., validate_on_access: _Optional[bool] = ..., timeout_seconds: _Optional[int] = ..., retry: _Optional[_Union[_config_retry_settings_pb2.ConfigRetrySettings, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
