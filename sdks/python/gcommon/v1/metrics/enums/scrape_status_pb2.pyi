from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ScrapeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCRAPE_STATUS_UNSPECIFIED: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_SUCCESS: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_NETWORK_ERROR: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_AUTH_ERROR: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_TIMEOUT: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_PARSE_ERROR: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_TARGET_DOWN: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_HTTP_ERROR: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_CANCELLED: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_RATE_LIMITED: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_CONFIG_ERROR: _ClassVar[ScrapeStatus]
    SCRAPE_STATUS_IN_PROGRESS: _ClassVar[ScrapeStatus]
SCRAPE_STATUS_UNSPECIFIED: ScrapeStatus
SCRAPE_STATUS_SUCCESS: ScrapeStatus
SCRAPE_STATUS_NETWORK_ERROR: ScrapeStatus
SCRAPE_STATUS_AUTH_ERROR: ScrapeStatus
SCRAPE_STATUS_TIMEOUT: ScrapeStatus
SCRAPE_STATUS_PARSE_ERROR: ScrapeStatus
SCRAPE_STATUS_TARGET_DOWN: ScrapeStatus
SCRAPE_STATUS_HTTP_ERROR: ScrapeStatus
SCRAPE_STATUS_CANCELLED: ScrapeStatus
SCRAPE_STATUS_RATE_LIMITED: ScrapeStatus
SCRAPE_STATUS_CONFIG_ERROR: ScrapeStatus
SCRAPE_STATUS_IN_PROGRESS: ScrapeStatus
