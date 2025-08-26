from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BillingSettings(_message.Message):
    __slots__ = ("billing_email", "billing_address", "tax_id", "currency", "billing_cycle")
    BILLING_EMAIL_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TAX_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    BILLING_CYCLE_FIELD_NUMBER: _ClassVar[int]
    billing_email: str
    billing_address: str
    tax_id: str
    currency: str
    billing_cycle: str
    def __init__(self, billing_email: _Optional[str] = ..., billing_address: _Optional[str] = ..., tax_id: _Optional[str] = ..., currency: _Optional[str] = ..., billing_cycle: _Optional[str] = ...) -> None: ...
