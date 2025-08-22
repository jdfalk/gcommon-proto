from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CookieSameSite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COOKIE_SAME_SITE_UNSPECIFIED: _ClassVar[CookieSameSite]
    COOKIE_SAME_SITE_DEFAULT: _ClassVar[CookieSameSite]
    COOKIE_SAME_SITE_LAX: _ClassVar[CookieSameSite]
    COOKIE_SAME_SITE_STRICT: _ClassVar[CookieSameSite]
    COOKIE_SAME_SITE_NONE: _ClassVar[CookieSameSite]
COOKIE_SAME_SITE_UNSPECIFIED: CookieSameSite
COOKIE_SAME_SITE_DEFAULT: CookieSameSite
COOKIE_SAME_SITE_LAX: CookieSameSite
COOKIE_SAME_SITE_STRICT: CookieSameSite
COOKIE_SAME_SITE_NONE: CookieSameSite
