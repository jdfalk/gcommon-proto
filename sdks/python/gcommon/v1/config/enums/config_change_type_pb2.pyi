from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFIG_CHANGE_TYPE_UNSPECIFIED: _ClassVar[ConfigChangeType]
    CONFIG_CHANGE_TYPE_CREATED: _ClassVar[ConfigChangeType]
    CONFIG_CHANGE_TYPE_UPDATED: _ClassVar[ConfigChangeType]
    CONFIG_CHANGE_TYPE_DELETED: _ClassVar[ConfigChangeType]
CONFIG_CHANGE_TYPE_UNSPECIFIED: ConfigChangeType
CONFIG_CHANGE_TYPE_CREATED: ConfigChangeType
CONFIG_CHANGE_TYPE_UPDATED: ConfigChangeType
CONFIG_CHANGE_TYPE_DELETED: ConfigChangeType
