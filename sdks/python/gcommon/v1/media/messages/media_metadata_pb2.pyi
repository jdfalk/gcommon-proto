from gcommon.v1.media.messages import movie_info_pb2 as _movie_info_pb2
from gcommon.v1.media.messages import series_info_pb2 as _series_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaMetadata(_message.Message):
    __slots__ = ("title", "original_title", "year", "plot", "genres", "imdb_id", "tmdb_id", "rating", "languages", "actors", "directors", "series_info", "movie_info")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    PLOT_FIELD_NUMBER: _ClassVar[int]
    GENRES_FIELD_NUMBER: _ClassVar[int]
    IMDB_ID_FIELD_NUMBER: _ClassVar[int]
    TMDB_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    DIRECTORS_FIELD_NUMBER: _ClassVar[int]
    SERIES_INFO_FIELD_NUMBER: _ClassVar[int]
    MOVIE_INFO_FIELD_NUMBER: _ClassVar[int]
    title: str
    original_title: str
    year: int
    plot: str
    genres: _containers.RepeatedScalarFieldContainer[str]
    imdb_id: str
    tmdb_id: str
    rating: float
    languages: _containers.RepeatedScalarFieldContainer[str]
    actors: _containers.RepeatedScalarFieldContainer[str]
    directors: _containers.RepeatedScalarFieldContainer[str]
    series_info: _series_info_pb2.SeriesInfo
    movie_info: _movie_info_pb2.MovieInfo
    def __init__(self, title: _Optional[str] = ..., original_title: _Optional[str] = ..., year: _Optional[int] = ..., plot: _Optional[str] = ..., genres: _Optional[_Iterable[str]] = ..., imdb_id: _Optional[str] = ..., tmdb_id: _Optional[str] = ..., rating: _Optional[float] = ..., languages: _Optional[_Iterable[str]] = ..., actors: _Optional[_Iterable[str]] = ..., directors: _Optional[_Iterable[str]] = ..., series_info: _Optional[_Union[_series_info_pb2.SeriesInfo, _Mapping]] = ..., movie_info: _Optional[_Union[_movie_info_pb2.MovieInfo, _Mapping]] = ...) -> None: ...
