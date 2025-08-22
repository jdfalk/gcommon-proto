from gcommon.v1.common import update_strategy_pb2 as _update_strategy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateOptions(_message.Message):
    __slots__ = ("validate_config", "dry_run", "restart_if_needed", "backup_config", "strategy")
    VALIDATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    RESTART_IF_NEEDED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    validate_config: bool
    dry_run: bool
    restart_if_needed: bool
    backup_config: bool
    strategy: _update_strategy_pb2.UpdateStrategy
    def __init__(self, validate_config: bool = ..., dry_run: bool = ..., restart_if_needed: bool = ..., backup_config: bool = ..., strategy: _Optional[_Union[_update_strategy_pb2.UpdateStrategy, str]] = ...) -> None: ...
