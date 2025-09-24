# Media Services Documentation

[← Back to Index](./README.md)

## Module Overview

- **Proto Files**: 4
- **Services**: 4

## Table of Contents

### Services

- [`AudioService`](#audio_service) - from audio_service.proto
- [`MediaProcessingService`](#media_processing_service) - from media_processing_service.proto
- [`MediaService`](#media_service) - from media_service.proto
- [`SubtitleService`](#subtitle_service) - from subtitle_service.proto

### Files in this Module

- [audio_service.proto](#audio_service)
- [media_processing_service.proto](#media_processing_service)
- [media_service.proto](#media_service)
- [subtitle_service.proto](#subtitle_service)

---


## Services Documentation

### audio_service.proto {#audio_service}

**Path**: `gcommon/v1/media/audio_service.proto` **Package**: `gcommon.v1.media` **Lines**: 43

**Services** (1): `AudioService`

**Imports** (11):

- `gcommon/v1/media/analyze_audio_quality_request.proto`
- `gcommon/v1/media/analyze_audio_quality_response.proto`
- `gcommon/v1/media/detect_chapters_request.proto`
- `gcommon/v1/media/detect_chapters_response.proto`
- `gcommon/v1/media/merge_audio_request.proto`
- `gcommon/v1/media/merge_audio_response.proto`
- `gcommon/v1/media/normalize_audio_request.proto`
- `gcommon/v1/media/normalize_audio_response.proto`
- `gcommon/v1/media/split_audio_request.proto`
- `gcommon/v1/media/split_audio_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/audio_service.proto
// version: 1.0.1
// guid: 0123456-789a-bcde-e7f8-a9b0c1d2e3f4

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/analyze_audio_quality_request.proto";
import "gcommon/v1/media/analyze_audio_quality_response.proto";
import "gcommon/v1/media/detect_chapters_request.proto";
import "gcommon/v1/media/detect_chapters_response.proto";
import "gcommon/v1/media/merge_audio_request.proto";
import "gcommon/v1/media/merge_audio_response.proto";
import "gcommon/v1/media/normalize_audio_request.proto";
import "gcommon/v1/media/normalize_audio_response.proto";
import "gcommon/v1/media/split_audio_request.proto";
import "gcommon/v1/media/split_audio_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

/**
 * AudioService provides audio-specific operations including
 * chapter detection, audio processing, and quality analysis.
 */
service AudioService {
  // Detect chapters in audiobook files
  rpc DetectChapters(DetectChaptersRequest) returns (DetectChaptersResponse);

  // Normalize audio levels
  rpc NormalizeAudio(NormalizeAudioRequest) returns (NormalizeAudioResponse);

  // Split audio file into segments
  rpc SplitAudio(SplitAudioRequest) returns (SplitAudioResponse);

  // Merge multiple audio files
  rpc MergeAudio(MergeAudioRequest) returns (MergeAudioResponse);

  // Analyze audio quality metrics
  rpc AnalyzeAudioQuality(AnalyzeAudioQualityRequest) returns (AnalyzeAudioQualityResponse);
}
```

---

### media_processing_service.proto {#media_processing_service}

**Path**: `gcommon/v1/media/media_processing_service.proto` **Package**: `gcommon.v1.media` **Lines**: 43

**Services** (1): `MediaProcessingService`

**Imports** (11):

- `gcommon/v1/media/analyze_media_request.proto`
- `gcommon/v1/media/analyze_media_response.proto`
- `gcommon/v1/media/extract_audio_request.proto`
- `gcommon/v1/media/extract_audio_response.proto`
- `gcommon/v1/media/extract_subtitles_request.proto`
- `gcommon/v1/media/extract_subtitles_response.proto`
- `gcommon/v1/media/get_processing_status_request.proto`
- `gcommon/v1/media/get_processing_status_response.proto`
- `gcommon/v1/media/transcode_media_request.proto`
- `gcommon/v1/media/transcode_media_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/media_processing_service.proto
// version: 1.0.1
// guid: 789abcd-ef01-2345-d2e3-f4a5b6c7d8e9

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/analyze_media_request.proto";
import "gcommon/v1/media/analyze_media_response.proto";
import "gcommon/v1/media/extract_audio_request.proto";
import "gcommon/v1/media/extract_audio_response.proto";
import "gcommon/v1/media/extract_subtitles_request.proto";
import "gcommon/v1/media/extract_subtitles_response.proto";
import "gcommon/v1/media/get_processing_status_request.proto";
import "gcommon/v1/media/get_processing_status_response.proto";
import "gcommon/v1/media/transcode_media_request.proto";
import "gcommon/v1/media/transcode_media_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

/**
 * MediaProcessingService provides media transcoding, analysis, and
 * content extraction operations.
 */
service MediaProcessingService {
  // Transcode media to different formats
  rpc TranscodeMedia(TranscodeMediaRequest) returns (TranscodeMediaResponse);

  // Analyze media content for quality, metadata extraction
  rpc AnalyzeMedia(AnalyzeMediaRequest) returns (AnalyzeMediaResponse);

  // Extract audio tracks from media
  rpc ExtractAudio(ExtractAudioRequest) returns (ExtractAudioResponse);

  // Extract subtitle tracks from media
  rpc ExtractSubtitles(ExtractSubtitlesRequest) returns (ExtractSubtitlesResponse);

  // Get processing job status
  rpc GetProcessingStatus(GetProcessingStatusRequest) returns (GetProcessingStatusResponse);
}
```

---

### media_service.proto {#media_service}

**Path**: `gcommon/v1/media/media_service.proto` **Package**: `gcommon.v1.media` **Lines**: 53

**Services** (1): `MediaService`

**Imports** (15):

- `gcommon/v1/media/create_media_file_request.proto`
- `gcommon/v1/media/create_media_file_response.proto`
- `gcommon/v1/media/delete_media_file_request.proto`
- `gcommon/v1/media/delete_media_file_response.proto`
- `gcommon/v1/media/get_media_file_request.proto`
- `gcommon/v1/media/get_media_file_response.proto`
- `gcommon/v1/media/list_media_files_request.proto`
- `gcommon/v1/media/list_media_files_response.proto`
- `gcommon/v1/media/search_media_request.proto`
- `gcommon/v1/media/search_media_response.proto`
- `gcommon/v1/media/update_media_file_request.proto`
- `gcommon/v1/media/update_media_file_response.proto`
- `gcommon/v1/media/upload_media_request.proto`
- `gcommon/v1/media/upload_media_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/media_service.proto
// version: 1.0.1
// guid: 8a9b0c1d-2e3f-4506-a7b8-9c0d1e2f3a4b

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/create_media_file_request.proto";
import "gcommon/v1/media/create_media_file_response.proto";
import "gcommon/v1/media/delete_media_file_request.proto";
import "gcommon/v1/media/delete_media_file_response.proto";
import "gcommon/v1/media/get_media_file_request.proto";
import "gcommon/v1/media/get_media_file_response.proto";
import "gcommon/v1/media/list_media_files_request.proto";
import "gcommon/v1/media/list_media_files_response.proto";
import "gcommon/v1/media/search_media_request.proto";
import "gcommon/v1/media/search_media_response.proto";
import "gcommon/v1/media/update_media_file_request.proto";
import "gcommon/v1/media/update_media_file_response.proto";
import "gcommon/v1/media/upload_media_request.proto";
import "gcommon/v1/media/upload_media_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

/**
 * MediaService provides core media file management operations including
 * upload, storage, retrieval, and basic metadata management.
 */
service MediaService {
  // Upload a new media file
  rpc UploadMedia(stream UploadMediaRequest) returns (UploadMediaResponse);

  // Create a media file record
  rpc CreateMediaFile(CreateMediaFileRequest) returns (CreateMediaFileResponse);

  // Get a specific media file
  rpc GetMediaFile(GetMediaFileRequest) returns (GetMediaFileResponse);

  // Update media file information
  rpc UpdateMediaFile(UpdateMediaFileRequest) returns (UpdateMediaFileResponse);

  // Delete a media file
  rpc DeleteMediaFile(DeleteMediaFileRequest) returns (DeleteMediaFileResponse);

  // List media files with filtering
  rpc ListMediaFiles(ListMediaFilesRequest) returns (ListMediaFilesResponse);

  // Search media files
  rpc SearchMedia(SearchMediaRequest) returns (SearchMediaResponse);
}
```

---

### subtitle_service.proto {#subtitle_service}

**Path**: `gcommon/v1/media/subtitle_service.proto` **Package**: `gcommon.v1.media` **Lines**: 43

**Services** (1): `SubtitleService`

**Imports** (11):

- `gcommon/v1/media/adjust_subtitle_timing_request.proto`
- `gcommon/v1/media/adjust_subtitle_timing_response.proto`
- `gcommon/v1/media/convert_subtitle_format_request.proto`
- `gcommon/v1/media/convert_subtitle_format_response.proto`
- `gcommon/v1/media/merge_subtitles_request.proto`
- `gcommon/v1/media/merge_subtitles_response.proto`
- `gcommon/v1/media/sync_subtitles_request.proto`
- `gcommon/v1/media/sync_subtitles_response.proto`
- `gcommon/v1/media/validate_subtitles_request.proto`
- `gcommon/v1/media/validate_subtitles_response.proto`
- `google/protobuf/go_features.proto`

#### Source Code

```protobuf
// file: proto/gcommon/v1/media/subtitle_service.proto
// version: 1.0.1
// guid: 3456789-abcd-ef01-d4e5-f6a7b8c9d0e1

edition = "2023";

package gcommon.v1.media;

import "gcommon/v1/media/adjust_subtitle_timing_request.proto";
import "gcommon/v1/media/adjust_subtitle_timing_response.proto";
import "gcommon/v1/media/convert_subtitle_format_request.proto";
import "gcommon/v1/media/convert_subtitle_format_response.proto";
import "gcommon/v1/media/merge_subtitles_request.proto";
import "gcommon/v1/media/merge_subtitles_response.proto";
import "gcommon/v1/media/sync_subtitles_request.proto";
import "gcommon/v1/media/sync_subtitles_response.proto";
import "gcommon/v1/media/validate_subtitles_request.proto";
import "gcommon/v1/media/validate_subtitles_response.proto";
import "google/protobuf/go_features.proto";

option features.(pb.go).api_level = API_OPAQUE;
option go_package = "github.com/jdfalk/gcommon/sdks/go/v1/media";

/**
 * SubtitleService provides subtitle management, synchronization,
 * and processing operations.
 */
service SubtitleService {
  // Merge multiple subtitle files
  rpc MergeSubtitles(MergeSubtitlesRequest) returns (MergeSubtitlesResponse);

  // Synchronize subtitles with media
  rpc SyncSubtitles(SyncSubtitlesRequest) returns (SyncSubtitlesResponse);

  // Adjust subtitle timing
  rpc AdjustSubtitleTiming(AdjustSubtitleTimingRequest) returns (AdjustSubtitleTimingResponse);

  // Convert subtitle format
  rpc ConvertSubtitleFormat(ConvertSubtitleFormatRequest) returns (ConvertSubtitleFormatResponse);

  // Validate subtitle file
  rpc ValidateSubtitles(ValidateSubtitlesRequest) returns (ValidateSubtitlesResponse);
}
```

---

