from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HTTPStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HTTP_STATUS_UNSPECIFIED: _ClassVar[HTTPStatus]
    HTTP_STATUS_OK: _ClassVar[HTTPStatus]
    HTTP_STATUS_BAD_REQUEST: _ClassVar[HTTPStatus]
    HTTP_STATUS_UNAUTHORIZED: _ClassVar[HTTPStatus]
    HTTP_STATUS_FORBIDDEN: _ClassVar[HTTPStatus]
    HTTP_STATUS_NOT_FOUND: _ClassVar[HTTPStatus]
    HTTP_STATUS_INTERNAL_ERROR: _ClassVar[HTTPStatus]

HTTP_STATUS_UNSPECIFIED: HTTPStatus
HTTP_STATUS_OK: HTTPStatus
HTTP_STATUS_BAD_REQUEST: HTTPStatus
HTTP_STATUS_UNAUTHORIZED: HTTPStatus
HTTP_STATUS_FORBIDDEN: HTTPStatus
HTTP_STATUS_NOT_FOUND: HTTPStatus
HTTP_STATUS_INTERNAL_ERROR: HTTPStatus
