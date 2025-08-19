from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MfaConfig(_message.Message):
    __slots__ = ("enabled", "methods", "totp_period", "totp_digits", "sms_enabled", "email_enabled")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    TOTP_PERIOD_FIELD_NUMBER: _ClassVar[int]
    TOTP_DIGITS_FIELD_NUMBER: _ClassVar[int]
    SMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    methods: _containers.RepeatedScalarFieldContainer[str]
    totp_period: int
    totp_digits: int
    sms_enabled: bool
    email_enabled: bool
    def __init__(self, enabled: bool = ..., methods: _Optional[_Iterable[str]] = ..., totp_period: _Optional[int] = ..., totp_digits: _Optional[int] = ..., sms_enabled: bool = ..., email_enabled: bool = ...) -> None: ...
