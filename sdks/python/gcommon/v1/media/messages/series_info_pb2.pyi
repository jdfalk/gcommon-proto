from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeriesInfo(_message.Message):
    __slots__ = ("season", "episode", "series_name", "episode_title", "air_date")
    SEASON_FIELD_NUMBER: _ClassVar[int]
    EPISODE_FIELD_NUMBER: _ClassVar[int]
    SERIES_NAME_FIELD_NUMBER: _ClassVar[int]
    EPISODE_TITLE_FIELD_NUMBER: _ClassVar[int]
    AIR_DATE_FIELD_NUMBER: _ClassVar[int]
    season: int
    episode: int
    series_name: str
    episode_title: str
    air_date: _timestamp_pb2.Timestamp
    def __init__(self, season: _Optional[int] = ..., episode: _Optional[int] = ..., series_name: _Optional[str] = ..., episode_title: _Optional[str] = ..., air_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
