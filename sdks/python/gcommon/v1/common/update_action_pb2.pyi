from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_ACTION_UNSPECIFIED: _ClassVar[UpdateAction]
    UPDATE_ACTION_UPDATED: _ClassVar[UpdateAction]
    UPDATE_ACTION_NO_CHANGE: _ClassVar[UpdateAction]
    UPDATE_ACTION_RESTARTED: _ClassVar[UpdateAction]
    UPDATE_ACTION_RECREATED: _ClassVar[UpdateAction]
UPDATE_ACTION_UNSPECIFIED: UpdateAction
UPDATE_ACTION_UPDATED: UpdateAction
UPDATE_ACTION_NO_CHANGE: UpdateAction
UPDATE_ACTION_RESTARTED: UpdateAction
UPDATE_ACTION_RECREATED: UpdateAction
