from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FilterAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILTER_ACTION_UNSPECIFIED: _ClassVar[FilterAction]
    FILTER_ACTION_INCLUDE: _ClassVar[FilterAction]
    FILTER_ACTION_EXCLUDE: _ClassVar[FilterAction]
    FILTER_ACTION_TRANSFORM: _ClassVar[FilterAction]
    FILTER_ACTION_VALIDATE: _ClassVar[FilterAction]
FILTER_ACTION_UNSPECIFIED: FilterAction
FILTER_ACTION_INCLUDE: FilterAction
FILTER_ACTION_EXCLUDE: FilterAction
FILTER_ACTION_TRANSFORM: FilterAction
FILTER_ACTION_VALIDATE: FilterAction
