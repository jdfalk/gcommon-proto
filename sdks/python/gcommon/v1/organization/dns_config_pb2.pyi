from gcommon.v1.organization import dns_record_pb2 as _dns_record_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DNSConfig(_message.Message):
    __slots__ = ("provider", "zone_id", "records", "ttl")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    provider: str
    zone_id: str
    records: _containers.RepeatedCompositeFieldContainer[_dns_record_pb2.DNSRecord]
    ttl: int
    def __init__(
        self,
        provider: _Optional[str] = ...,
        zone_id: _Optional[str] = ...,
        records: _Optional[
            _Iterable[_Union[_dns_record_pb2.DNSRecord, _Mapping]]
        ] = ...,
        ttl: _Optional[int] = ...,
    ) -> None: ...
