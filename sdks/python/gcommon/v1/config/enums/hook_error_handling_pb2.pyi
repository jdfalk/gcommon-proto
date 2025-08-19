from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HookErrorHandling(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HOOK_ERROR_HANDLING_UNSPECIFIED: _ClassVar[HookErrorHandling]
    HOOK_ERROR_HANDLING_IGNORE: _ClassVar[HookErrorHandling]
    HOOK_ERROR_HANDLING_WARN: _ClassVar[HookErrorHandling]
    HOOK_ERROR_HANDLING_FAIL: _ClassVar[HookErrorHandling]
HOOK_ERROR_HANDLING_UNSPECIFIED: HookErrorHandling
HOOK_ERROR_HANDLING_IGNORE: HookErrorHandling
HOOK_ERROR_HANDLING_WARN: HookErrorHandling
HOOK_ERROR_HANDLING_FAIL: HookErrorHandling
