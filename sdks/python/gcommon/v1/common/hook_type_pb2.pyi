from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HookType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HOOK_TYPE_UNSPECIFIED: _ClassVar[HookType]
    HOOK_TYPE_PRE_RENDER: _ClassVar[HookType]
    HOOK_TYPE_POST_RENDER: _ClassVar[HookType]
    HOOK_TYPE_PRE_APPLY: _ClassVar[HookType]
    HOOK_TYPE_POST_APPLY: _ClassVar[HookType]
    HOOK_TYPE_PRE_VALIDATE: _ClassVar[HookType]
    HOOK_TYPE_POST_VALIDATE: _ClassVar[HookType]

HOOK_TYPE_UNSPECIFIED: HookType
HOOK_TYPE_PRE_RENDER: HookType
HOOK_TYPE_POST_RENDER: HookType
HOOK_TYPE_PRE_APPLY: HookType
HOOK_TYPE_POST_APPLY: HookType
HOOK_TYPE_PRE_VALIDATE: HookType
HOOK_TYPE_POST_VALIDATE: HookType
