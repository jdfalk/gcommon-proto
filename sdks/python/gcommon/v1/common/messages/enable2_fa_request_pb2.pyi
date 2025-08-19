from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Enable2FaRequest(_message.Message):
    __slots__ = ("user_id", "phone_number", "use_authenticator", "generate_backup_codes")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    USE_AUTHENTICATOR_FIELD_NUMBER: _ClassVar[int]
    GENERATE_BACKUP_CODES_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    phone_number: str
    use_authenticator: bool
    generate_backup_codes: bool
    def __init__(self, user_id: _Optional[str] = ..., phone_number: _Optional[str] = ..., use_authenticator: bool = ..., generate_backup_codes: bool = ...) -> None: ...
