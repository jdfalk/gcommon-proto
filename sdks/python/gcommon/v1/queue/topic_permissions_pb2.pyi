from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TopicPermissions(_message.Message):
    __slots__ = ("can_read", "can_write", "can_configure", "can_delete", "can_manage_permissions", "can_view_stats")
    CAN_READ_FIELD_NUMBER: _ClassVar[int]
    CAN_WRITE_FIELD_NUMBER: _ClassVar[int]
    CAN_CONFIGURE_FIELD_NUMBER: _ClassVar[int]
    CAN_DELETE_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CAN_VIEW_STATS_FIELD_NUMBER: _ClassVar[int]
    can_read: bool
    can_write: bool
    can_configure: bool
    can_delete: bool
    can_manage_permissions: bool
    can_view_stats: bool
    def __init__(self, can_read: _Optional[bool] = ..., can_write: _Optional[bool] = ..., can_configure: _Optional[bool] = ..., can_delete: _Optional[bool] = ..., can_manage_permissions: _Optional[bool] = ..., can_view_stats: _Optional[bool] = ...) -> None: ...
