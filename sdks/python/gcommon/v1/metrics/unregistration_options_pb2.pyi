from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnregistrationOptions(_message.Message):
    __slots__ = ("delete_data", "delete_indices", "remove_alerts", "stop_exports", "grace_period", "dry_run", "force", "create_backup")
    DELETE_DATA_FIELD_NUMBER: _ClassVar[int]
    DELETE_INDICES_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ALERTS_FIELD_NUMBER: _ClassVar[int]
    STOP_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    GRACE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    CREATE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    delete_data: bool
    delete_indices: bool
    remove_alerts: bool
    stop_exports: bool
    grace_period: str
    dry_run: bool
    force: bool
    create_backup: bool
    def __init__(self, delete_data: bool = ..., delete_indices: bool = ..., remove_alerts: bool = ..., stop_exports: bool = ..., grace_period: _Optional[str] = ..., dry_run: bool = ..., force: bool = ..., create_backup: bool = ...) -> None: ...
