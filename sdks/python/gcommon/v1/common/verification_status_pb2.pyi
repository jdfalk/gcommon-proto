from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerificationStatus(_message.Message):
    __slots__ = ("email_verified", "phone_verified", "identity_verified", "email_verified_at", "phone_verified_at", "identity_verified_at")
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    PHONE_VERIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_VERIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    email_verified: bool
    phone_verified: bool
    identity_verified: bool
    email_verified_at: _timestamp_pb2.Timestamp
    phone_verified_at: _timestamp_pb2.Timestamp
    identity_verified_at: _timestamp_pb2.Timestamp
    def __init__(self, email_verified: bool = ..., phone_verified: bool = ..., identity_verified: bool = ..., email_verified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., phone_verified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., identity_verified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
