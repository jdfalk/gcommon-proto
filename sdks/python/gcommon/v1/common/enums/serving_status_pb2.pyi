from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ServingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVING_STATUS_UNSPECIFIED: _ClassVar[ServingStatus]
    SERVING_STATUS_SERVING: _ClassVar[ServingStatus]
    SERVING_STATUS_NOT_SERVING: _ClassVar[ServingStatus]
    SERVING_STATUS_SERVING_DEGRADED: _ClassVar[ServingStatus]
SERVING_STATUS_UNSPECIFIED: ServingStatus
SERVING_STATUS_SERVING: ServingStatus
SERVING_STATUS_NOT_SERVING: ServingStatus
SERVING_STATUS_SERVING_DEGRADED: ServingStatus
