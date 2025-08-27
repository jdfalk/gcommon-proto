from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PasswordPolicy(_message.Message):
    __slots__ = (
        "min_length",
        "require_uppercase",
        "require_lowercase",
        "require_number",
        "require_symbol",
        "max_age_days",
        "history",
        "allow_reuse",
    )
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_UPPERCASE_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_LOWERCASE_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_SYMBOL_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_DAYS_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_REUSE_FIELD_NUMBER: _ClassVar[int]
    min_length: int
    require_uppercase: bool
    require_lowercase: bool
    require_number: bool
    require_symbol: bool
    max_age_days: int
    history: int
    allow_reuse: bool
    def __init__(
        self,
        min_length: _Optional[int] = ...,
        require_uppercase: _Optional[bool] = ...,
        require_lowercase: _Optional[bool] = ...,
        require_number: _Optional[bool] = ...,
        require_symbol: _Optional[bool] = ...,
        max_age_days: _Optional[int] = ...,
        history: _Optional[int] = ...,
        allow_reuse: _Optional[bool] = ...,
    ) -> None: ...
