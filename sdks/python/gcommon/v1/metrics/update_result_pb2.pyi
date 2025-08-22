from gcommon.v1.common import update_action_pb2 as _update_action_pb2
from gcommon.v1.metrics import config_change_pb2 as _config_change_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateResult(_message.Message):
    __slots__ = ("action", "config_changes", "updated_settings", "removed_settings", "restarted", "strategy_used", "update_duration")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_CHANGES_FIELD_NUMBER: _ClassVar[int]
    UPDATED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RESTARTED_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_USED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DURATION_FIELD_NUMBER: _ClassVar[int]
    action: _update_action_pb2.UpdateAction
    config_changes: _containers.RepeatedCompositeFieldContainer[_config_change_pb2.MetricsConfigChange]
    updated_settings: _containers.RepeatedScalarFieldContainer[str]
    removed_settings: _containers.RepeatedScalarFieldContainer[str]
    restarted: bool
    strategy_used: str
    update_duration: str
    def __init__(self, action: _Optional[_Union[_update_action_pb2.UpdateAction, str]] = ..., config_changes: _Optional[_Iterable[_Union[_config_change_pb2.MetricsConfigChange, _Mapping]]] = ..., updated_settings: _Optional[_Iterable[str]] = ..., removed_settings: _Optional[_Iterable[str]] = ..., restarted: bool = ..., strategy_used: _Optional[str] = ..., update_duration: _Optional[str] = ...) -> None: ...
