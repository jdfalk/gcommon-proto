from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UISettings(_message.Message):
    __slots__ = ("primary_color", "secondary_color", "logo_url", "favicon_url", "custom_css", "default_locale", "default_timezone", "date_format", "time_format", "dark_mode_default")
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    FAVICON_URL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CSS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCALE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    DATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TIME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DARK_MODE_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    primary_color: str
    secondary_color: str
    logo_url: str
    favicon_url: str
    custom_css: str
    default_locale: str
    default_timezone: str
    date_format: str
    time_format: str
    dark_mode_default: bool
    def __init__(self, primary_color: _Optional[str] = ..., secondary_color: _Optional[str] = ..., logo_url: _Optional[str] = ..., favicon_url: _Optional[str] = ..., custom_css: _Optional[str] = ..., default_locale: _Optional[str] = ..., default_timezone: _Optional[str] = ..., date_format: _Optional[str] = ..., time_format: _Optional[str] = ..., dark_mode_default: _Optional[bool] = ...) -> None: ...
