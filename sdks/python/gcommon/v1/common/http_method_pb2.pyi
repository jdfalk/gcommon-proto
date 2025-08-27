from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HTTPMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HTTP_METHOD_UNSPECIFIED: _ClassVar[HTTPMethod]
    HTTP_METHOD_GET: _ClassVar[HTTPMethod]
    HTTP_METHOD_POST: _ClassVar[HTTPMethod]
    HTTP_METHOD_PUT: _ClassVar[HTTPMethod]
    HTTP_METHOD_DELETE: _ClassVar[HTTPMethod]
    HTTP_METHOD_PATCH: _ClassVar[HTTPMethod]
    HTTP_METHOD_OPTIONS: _ClassVar[HTTPMethod]
    HTTP_METHOD_HEAD: _ClassVar[HTTPMethod]
HTTP_METHOD_UNSPECIFIED: HTTPMethod
HTTP_METHOD_GET: HTTPMethod
HTTP_METHOD_POST: HTTPMethod
HTTP_METHOD_PUT: HTTPMethod
HTTP_METHOD_DELETE: HTTPMethod
HTTP_METHOD_PATCH: HTTPMethod
HTTP_METHOD_OPTIONS: HTTPMethod
HTTP_METHOD_HEAD: HTTPMethod
