# media Module

[← Back to Index](./index.md)

## Module Overview

- **Proto Files**: 10
- **Messages**: 7
- **Services**: 0
- **Enums**: 3

## Files in this Module

- [audio_track.proto](#audio_track)
- [media_file.proto](#media_file)
- [media_metadata.proto](#media_metadata)
- [media_quality.proto](#media_quality)
- [media_type.proto](#media_type)
- [movie_info.proto](#movie_info)
- [quality_score.proto](#quality_score)
- [resolution.proto](#resolution)
- [series_info.proto](#series_info)
- [subtitle_track.proto](#subtitle_track)

---

## Detailed Documentation

### audio_track.proto {#audio_track}

**Path**: `pkg/media/proto/audio_track.proto` **Package**: `gcommon.v1.media` **Lines**: 24

**Messages** (1): `AudioTrack`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/media/proto/messages/audio_track.proto
// version: 1.0.0
// guid: 55a5a263-fb45-49ae-8090-81d826cc0a5f

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/media/proto";

// Audio track information.
message AudioTrack {
  int32 index = 1;
  string language = 2;
  string codec = 3;
  string title = 4;
  int32 channels = 5;
  int32 sample_rate = 6;
  bool default_track = 7;
}

```

---

### media_file.proto {#media_file}

**Path**: `pkg/media/proto/media_file.proto` **Package**: `gcommon.v1.media` **Lines**: 34

**Messages** (1): `MediaFile`

**Imports** (7):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`
- `pkg/media/proto/audio_track.proto`
- `pkg/media/proto/media_metadata.proto`
- `pkg/media/proto/media_quality.proto`
- `pkg/media/proto/media_type.proto`
- `pkg/media/proto/subtitle_track.proto`

#### Source Code

```protobuf
// file: pkg/media/proto/messages/media_file.proto
// version: 1.0.0
// guid: e3bc9175-1261-4755-9d32-d991586e723f

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";
import "pkg/media/proto/audio_track.proto";
import "pkg/media/proto/media_metadata.proto";
import "pkg/media/proto/media_quality.proto";
import "pkg/media/proto/media_type.proto";
import "pkg/media/proto/subtitle_track.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/media/proto";

// Media file representation with associated metadata and tracks.
message MediaFile {
  string id = 1;
  string path = 2;
  string filename = 3;
  MediaType type = 4;
  int64 size_bytes = 5;
  google.protobuf.Timestamp created_at = 6 [lazy = true];
  google.protobuf.Timestamp modified_at = 7 [lazy = true];
  MediaMetadata metadata = 8;
  repeated SubtitleTrack subtitle_tracks = 9;
  repeated AudioTrack audio_tracks = 10;
  MediaQuality quality = 11;
}

```

---

### media_metadata.proto {#media_metadata}

**Path**: `pkg/media/proto/media_metadata.proto` **Package**: `gcommon.v1.media` **Lines**: 32

**Messages** (1): `MediaMetadata`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/media/proto/movie_info.proto`
- `pkg/media/proto/series_info.proto`

#### Source Code

```protobuf
// file: pkg/media/proto/messages/media_metadata.proto
// version: 1.0.0
// guid: e5b804c2-185f-402f-8edb-b3c390406e52

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "pkg/media/proto/movie_info.proto";
import "pkg/media/proto/series_info.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/media/proto";

// Metadata information for a media file from external sources.
message MediaMetadata {
  string title = 1;
  string original_title = 2;
  int32 year = 3;
  string plot = 4;
  repeated string genres = 5;
  string imdb_id = 6;
  string tmdb_id = 7;
  float rating = 8;
  repeated string languages = 9;
  repeated string actors = 10;
  repeated string directors = 11;
  SeriesInfo series_info = 12;
  MovieInfo movie_info = 13;
}

```

---

### media_quality.proto {#media_quality}

**Path**: `pkg/media/proto/media_quality.proto` **Package**: `gcommon.v1.media` **Lines**: 24

**Messages** (1): `MediaQuality`

**Imports** (3):

- `google/protobuf/go_features.proto`
- `pkg/media/proto/quality_score.proto`
- `pkg/media/proto/resolution.proto`

#### Source Code

```protobuf
// file: pkg/media/proto/messages/media_quality.proto
// version: 1.0.0
// guid: 62c527ab-9d69-4c5c-af80-64aa0657f948

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "pkg/media/proto/quality_score.proto";
import "pkg/media/proto/resolution.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/media/proto";

// Media quality assessment.
message MediaQuality {
  Resolution resolution = 1;
  string video_codec = 2;
  int32 bitrate_kbps = 3;
  float duration_seconds = 4;
  QualityScore quality_score = 5;
}

```

---

### media_type.proto {#media_type}

**Path**: `pkg/media/proto/media_type.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Enums** (1): `MediaType`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/media/proto/enums/media_type.proto
// version: 1.0.0
// guid: d13c4939-a91b-4cb8-85e6-09ddda85220e

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/media/proto";

// Media type classification for library items.
enum MediaType {
  MEDIA_TYPE_UNSPECIFIED = 0;
  MEDIA_TYPE_MOVIE = 1;
  MEDIA_TYPE_TV_EPISODE = 2;
  MEDIA_TYPE_DOCUMENTARY = 3;
  MEDIA_TYPE_ANIME = 4;
}

```

---

### movie_info.proto {#movie_info}

**Path**: `pkg/media/proto/movie_info.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Messages** (1): `MovieInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/media/proto/messages/movie_info.proto
// version: 1.0.0
// guid: fc3b809f-03e7-4446-b355-e7482000e343

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/media/proto";

// Movie specific information.
message MovieInfo {
  google.protobuf.Timestamp release_date = 1;
  int64 budget = 2;
  int64 revenue = 3;
  int32 runtime_minutes = 4;
}

```

---

### quality_score.proto {#quality_score}

**Path**: `pkg/media/proto/quality_score.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Enums** (1): `QualityScore`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/media/proto/enums/quality_score.proto
// version: 1.0.0
// guid: 3d37a954-484a-4beb-acc4-7ec2fd05bf7d

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/media/proto";

// Overall media quality rating.
enum QualityScore {
  QUALITY_SCORE_UNSPECIFIED = 0;
  QUALITY_SCORE_LOW = 1;
  QUALITY_SCORE_MEDIUM = 2;
  QUALITY_SCORE_HIGH = 3;
  QUALITY_SCORE_EXCELLENT = 4;
}

```

---

### resolution.proto {#resolution}

**Path**: `pkg/media/proto/resolution.proto` **Package**: `gcommon.v1.media` **Lines**: 22

**Enums** (1): `Resolution`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/media/proto/enums/resolution.proto
// version: 1.0.0
// guid: 2901b257-89ea-43db-8650-a3b6b48acfdb

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/media/proto";

// Media resolution enumeration.
enum Resolution {
  RESOLUTION_UNSPECIFIED = 0;
  RESOLUTION_480P = 1;
  RESOLUTION_720P = 2;
  RESOLUTION_1080P = 3;
  RESOLUTION_4K = 4;
}

```

---

### series_info.proto {#series_info}

**Path**: `pkg/media/proto/series_info.proto` **Package**: `gcommon.v1.media` **Lines**: 23

**Messages** (1): `SeriesInfo`

**Imports** (2):

- `google/protobuf/go_features.proto`
- `google/protobuf/timestamp.proto`

#### Source Code

```protobuf
// file: pkg/media/proto/messages/series_info.proto
// version: 1.0.0
// guid: 1ff30d9b-8171-4cb2-885c-0ae98bd2ad17

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";
import "google/protobuf/timestamp.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/media/proto";

// TV series specific information.
message SeriesInfo {
  int32 season = 1;
  int32 episode = 2;
  string series_name = 3;
  string episode_title = 4;
  google.protobuf.Timestamp air_date = 5;
}

```

---

### subtitle_track.proto {#subtitle_track}

**Path**: `pkg/media/proto/subtitle_track.proto` **Package**: `gcommon.v1.media` **Lines**: 24

**Messages** (1): `SubtitleTrack`

**Imports** (1):

- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: pkg/media/proto/messages/subtitle_track.proto
// version: 1.0.0
// guid: 2c899982-81d3-43b7-a542-24361cdef856

edition = "2023";

package gcommon.v1.media;

import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/pkg/media/proto";

// Subtitle track information.
message SubtitleTrack {
  int32 index = 1;
  string language = 2;
  string codec = 3;
  string title = 4;
  bool forced = 5;
  bool hearing_impaired = 6;
  bool default_track = 7;
}

```

---
