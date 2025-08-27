from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RegistrationOptions(_message.Message):
    __slots__ = ("validate_definition", "dry_run", "create_indices", "enable_alerting")
    VALIDATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    CREATE_INDICES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ALERTING_FIELD_NUMBER: _ClassVar[int]
    validate_definition: bool
    dry_run: bool
    create_indices: bool
    enable_alerting: bool
    def __init__(self, validate_definition: _Optional[bool] = ..., dry_run: _Optional[bool] = ..., create_indices: _Optional[bool] = ..., enable_alerting: _Optional[bool] = ...) -> None: ...
