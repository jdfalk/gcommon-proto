from gcommon.v1.queue.messages import subscription_config_update_pb2 as _subscription_config_update_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSubscriptionConfigRequest(_message.Message):
    __slots__ = ("subscription_id", "config_update", "update_fields", "validate_only", "force_update", "immediate_apply", "change_reason", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_UPDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FORCE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_APPLY_FIELD_NUMBER: _ClassVar[int]
    CHANGE_REASON_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    config_update: _subscription_config_update_pb2.SubscriptionConfigUpdate
    update_fields: _containers.RepeatedScalarFieldContainer[str]
    validate_only: bool
    force_update: bool
    immediate_apply: bool
    change_reason: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, subscription_id: _Optional[str] = ..., config_update: _Optional[_Union[_subscription_config_update_pb2.SubscriptionConfigUpdate, _Mapping]] = ..., update_fields: _Optional[_Iterable[str]] = ..., validate_only: bool = ..., force_update: bool = ..., immediate_apply: bool = ..., change_reason: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
