from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationEncryptionConfig(_message.Message):
    __slots__ = ("encryption_at_rest", "encryption_in_transit", "key_management_service", "customer_key_id", "encryption_algorithm")
    ENCRYPTION_AT_REST_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_IN_TRANSIT_FIELD_NUMBER: _ClassVar[int]
    KEY_MANAGEMENT_SERVICE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    encryption_at_rest: bool
    encryption_in_transit: bool
    key_management_service: str
    customer_key_id: str
    encryption_algorithm: str
    def __init__(self, encryption_at_rest: _Optional[bool] = ..., encryption_in_transit: _Optional[bool] = ..., key_management_service: _Optional[str] = ..., customer_key_id: _Optional[str] = ..., encryption_algorithm: _Optional[str] = ...) -> None: ...
