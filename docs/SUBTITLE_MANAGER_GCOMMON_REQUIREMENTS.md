# Subtitle Manager - GCommon Protobuf Requirements Analysis

**Report Date**: July 27, 2025
**Report Author**: GitHub Copilot
**Project**: [subtitle-manager](https://github.com/jdfalk/subtitle-manager)
**Target Repo**: [gcommon](https://github.com/jdfalk/gcommon)

---

## Executive Summary

This comprehensive analysis examines the subtitle-manager project to identify missing protobuf services and message types that need to be implemented in the gcommon repository. Based on the analysis of subtitle-manager's architecture, existing protobuf usage, and business domain requirements, this report provides a detailed roadmap for extending gcommon to fully support subtitle management operations.

**Key Findings:**
- **Current Integration**: Subtitle-manager already uses gcommon for basic types (RequestMetadata, Error)
- **Missing Services**: 8 major service categories need implementation in gcommon
- **Required Messages**: ~150+ new message types across multiple domains
- **Priority Level**: High - subtitle-manager represents a real-world production use case for gcommon

---

## Table of Contents

1. [Current Subtitle Manager Architecture](#current-subtitle-manager-architecture)
2. [Existing GCommon Usage](#existing-gcommon-usage)
3. [Missing Protobuf Services in GCommon](#missing-protobuf-services-in-gcommon)
4. [Required Message Types](#required-message-types)
5. [Service Definitions Needed](#service-definitions-needed)
6. [Implementation Priority Matrix](#implementation-priority-matrix)
7. [Integration Strategy](#integration-strategy)
8. [Migration Roadmap](#migration-roadmap)
9. [Benefits and Impact](#benefits-and-impact)
10. [Recommended Next Steps](#recommended-next-steps)

---

## Current Subtitle Manager Architecture

### Core Domain Areas

Subtitle Manager is a comprehensive subtitle management system with the following key domains:

**1. Core Business Functions:**
- Subtitle format conversion (SRT, VTT, ASS, SSA)
- Translation services (Google Translate, OpenAI GPT)
- Audio transcription (Whisper integration)
- Subtitle synchronization (audio + embedded methods)
- Provider management (40+ subtitle providers)

**2. Media Library Management:**
- Media file scanning and indexing
- Metadata fetching (TheMovieDB integration)
- Library watching and auto-processing
- Sonarr/Radarr integration for media servers

**3. Enterprise Features:**
- User authentication and RBAC
- Session management and API keys
- Audit logging and history tracking
- Notification services (Discord, Telegram, SMTP)
- Webhook system for external integrations

**4. Infrastructure:**
- Multi-database support (SQLite, PebbleDB, PostgreSQL)
- gRPC services for remote operations
- REST API with comprehensive endpoints
- Web UI (React + Vite)
- Container deployment (multi-arch Docker)

### Current Architecture Stats
- **LOC**: ~50,000+ lines of Go code
- **Packages**: 60+ internal packages
- **Dependencies**: Uses gcommon v0.1.0 minimally
- **Database Tables**: 15+ entities with complex relationships
- **API Endpoints**: 50+ REST endpoints
- **Protobuf Files**: 3 existing (basic configuration and translation)

---

## Existing GCommon Usage

### Current Integration Points

Subtitle-manager currently uses gcommon in a minimal capacity:

**1. Protobuf Messages Used:**
```protobuf
// From translator.proto
import "pkg/common/proto/messages/request_metadata.proto";
import "pkg/common/proto/messages/error.proto";

// Usage in services
gcommon.v1.common.RequestMetadata meta = 1;
repeated gcommon.v1.common.Error errors = 2;
```

**2. Go Module Dependency:**
```go
// go.mod
github.com/jdfalk/gcommon v0.1.0
```

**3. Internal Implementations:**
- Authentication: `pkg/gcommonauth/` (local implementation)
- Configuration: `pkg/gcommon/config/` (local wrapper)
- Database: Custom implementations for each backend

### Integration Readiness
- ✅ **Protocol Buffers**: Already using Edition 2023
- ✅ **Import Structure**: Uses direct imports (recommended pattern)
- ✅ **Error Handling**: Basic error types from gcommon
- ⚠️ **Service Integration**: No gRPC services from gcommon yet
- ❌ **Advanced Types**: Missing specialized message types

---

## Missing Protobuf Services in GCommon

Based on subtitle-manager's architecture, the following services are needed in gcommon:

### 1. Media Management Service ⭐ **HIGH PRIORITY**

**Purpose**: Core media file and metadata management
**Current Status in GCommon**: ❌ **Missing**
**Subtitle Manager Usage**: Core business domain

**Required Services:**
```protobuf
service MediaService {
  // Media file operations
  rpc ScanLibrary(ScanLibraryRequest) returns (ScanLibraryResponse);
  rpc GetMediaInfo(GetMediaInfoRequest) returns (GetMediaInfoResponse);
  rpc UpdateMediaMetadata(UpdateMediaMetadataRequest) returns (UpdateMediaMetadataResponse);
  rpc ListMedia(ListMediaRequest) returns (ListMediaResponse);
  rpc DeleteMedia(DeleteMediaRequest) returns (DeleteMediaResponse);

  // Directory operations
  rpc WatchDirectory(WatchDirectoryRequest) returns (stream DirectoryEvent);
  rpc BrowseDirectory(BrowseDirectoryRequest) returns (BrowseDirectoryResponse);

  // Metadata operations
  rpc FetchExternalMetadata(FetchMetadataRequest) returns (FetchMetadataResponse);
  rpc ValidateMediaFile(ValidateMediaRequest) returns (ValidateMediaResponse);
}

service MediaLibraryService {
  // Library management
  rpc CreateLibrary(CreateLibraryRequest) returns (CreateLibraryResponse);
  rpc GetLibraryStatus(GetLibraryStatusRequest) returns (GetLibraryStatusResponse);
  rpc ScanLibraryProgress(ScanProgressRequest) returns (stream ScanProgressEvent);
}
```

### 2. Subtitle Management Service ⭐ **HIGH PRIORITY**

**Purpose**: Subtitle-specific operations and processing
**Current Status in GCommon**: ❌ **Missing**
**Subtitle Manager Usage**: Primary business function

**Required Services:**
```protobuf
service SubtitleService {
  // Core subtitle operations
  rpc ConvertFormat(ConvertFormatRequest) returns (ConvertFormatResponse);
  rpc MergeSubtitles(MergeSubtitlesRequest) returns (MergeSubtitlesResponse);
  rpc SynchronizeSubtitles(SynchronizeRequest) returns (SynchronizeResponse);
  rpc ExtractFromMedia(ExtractRequest) returns (ExtractResponse);

  // Subtitle search and download
  rpc SearchSubtitles(SearchSubtitlesRequest) returns (SearchSubtitlesResponse);
  rpc DownloadSubtitle(DownloadSubtitleRequest) returns (DownloadSubtitleResponse);
  rpc BatchDownload(BatchDownloadRequest) returns (BatchDownloadResponse);

  // Quality and scoring
  rpc ScoreSubtitle(ScoreSubtitleRequest) returns (ScoreSubtitleResponse);
  rpc ValidateSubtitle(ValidateSubtitleRequest) returns (ValidateSubtitleResponse);
}

service SubtitleProviderService {
  // Provider management
  rpc ListProviders(ListProvidersRequest) returns (ListProvidersResponse);
  rpc ConfigureProvider(ConfigureProviderRequest) returns (ConfigureProviderResponse);
  rpc TestProvider(TestProviderRequest) returns (TestProviderResponse);
  rpc GetProviderStatus(ProviderStatusRequest) returns (ProviderStatusResponse);
}
```

### 3. Translation and Transcription Services ⭐ **HIGH PRIORITY**

**Purpose**: Language processing and AI integration
**Current Status in GCommon**: ❌ **Missing**
**Subtitle Manager Usage**: Core feature differentiator

**Required Services:**
```protobuf
service TranslationService {
  // Translation operations
  rpc TranslateText(TranslateTextRequest) returns (TranslateTextResponse);
  rpc TranslateSubtitle(TranslateSubtitleRequest) returns (TranslateSubtitleResponse);
  rpc BatchTranslate(BatchTranslateRequest) returns (BatchTranslateResponse);

  // Language detection and support
  rpc DetectLanguage(DetectLanguageRequest) returns (DetectLanguageResponse);
  rpc ListSupportedLanguages(ListLanguagesRequest) returns (ListLanguagesResponse);
  rpc GetTranslationProviders(TranslationProvidersRequest) returns (TranslationProvidersResponse);
}

service TranscriptionService {
  // Audio transcription
  rpc TranscribeAudio(TranscribeAudioRequest) returns (TranscribeAudioResponse);
  rpc TranscribeFromMedia(TranscribeMediaRequest) returns (TranscribeMediaResponse);
  rpc GetTranscriptionStatus(TranscriptionStatusRequest) returns (TranscriptionStatusResponse);

  // Whisper integration
  rpc ConfigureWhisper(ConfigureWhisperRequest) returns (ConfigureWhisperResponse);
  rpc GetWhisperModels(WhisperModelsRequest) returns (WhisperModelsResponse);
}
```

### 4. Provider Integration Service 🔶 **MEDIUM PRIORITY**

**Purpose**: External service integrations (Sonarr, Radarr, Plex)
**Current Status in GCommon**: ❌ **Missing**
**Subtitle Manager Usage**: Enterprise features

**Required Services:**
```protobuf
service IntegrationService {
  // Media server integration
  rpc ConnectToSonarr(ConnectSonarrRequest) returns (ConnectSonarrResponse);
  rpc SyncWithRadarr(SyncRadarrRequest) returns (SyncRadarrResponse);
  rpc UpdatePlexLibrary(PlexUpdateRequest) returns (PlexUpdateResponse);

  // Webhook management
  rpc RegisterWebhook(RegisterWebhookRequest) returns (RegisterWebhookResponse);
  rpc ProcessWebhookEvent(WebhookEventRequest) returns (WebhookEventResponse);
  rpc GetWebhookStatus(WebhookStatusRequest) returns (WebhookStatusResponse);
}

service ExternalAPIService {
  // External metadata APIs
  rpc FetchFromTMDB(TMDBRequest) returns (TMDBResponse);
  rpc SearchExternalAPI(ExternalSearchRequest) returns (ExternalSearchResponse);
  rpc ValidateAPIKey(ValidateAPIKeyRequest) returns (ValidateAPIKeyResponse);
}
```

### 5. Task and Job Management Service 🔶 **MEDIUM PRIORITY**

**Purpose**: Background job processing and scheduling
**Current Status in GCommon**: 🔶 **Partial** (basic queue module exists)
**Subtitle Manager Usage**: Async operations

**Required Enhancements to Existing Queue Module:**
```protobuf
service TaskService {
  // Specialized task operations
  rpc ScheduleSubtitleJob(ScheduleJobRequest) returns (ScheduleJobResponse);
  rpc GetJobProgress(JobProgressRequest) returns (stream JobProgressEvent);
  rpc CancelJob(CancelJobRequest) returns (CancelJobResponse);
  rpc GetJobHistory(JobHistoryRequest) returns (JobHistoryResponse);

  // Batch operations
  rpc ScheduleBatchOperation(BatchOperationRequest) returns (BatchOperationResponse);
  rpc MonitorBatchProgress(BatchProgressRequest) returns (stream BatchProgressEvent);
}

service SchedulerService {
  // Cron-based scheduling
  rpc CreateSchedule(CreateScheduleRequest) returns (CreateScheduleResponse);
  rpc UpdateSchedule(UpdateScheduleRequest) returns (UpdateScheduleResponse);
  rpc GetScheduledJobs(ScheduledJobsRequest) returns (ScheduledJobsResponse);
  rpc TriggerScheduledJob(TriggerJobRequest) returns (TriggerJobResponse);
}
```

### 6. User Profile and Preference Service 🔶 **MEDIUM PRIORITY**

**Purpose**: User-specific settings and language profiles
**Current Status in GCommon**: 🔶 **Partial** (basic auth exists)
**Subtitle Manager Usage**: User customization

**Required Enhancements to Existing Auth Module:**
```protobuf
service UserProfileService {
  // Profile management
  rpc GetUserProfile(UserProfileRequest) returns (UserProfileResponse);
  rpc UpdateUserProfile(UpdateProfileRequest) returns (UpdateProfileResponse);
  rpc GetUserPreferences(UserPreferencesRequest) returns (UserPreferencesResponse);
  rpc SetUserPreferences(SetPreferencesRequest) returns (SetPreferencesResponse);

  // Language profiles
  rpc CreateLanguageProfile(CreateLanguageProfileRequest) returns (CreateLanguageProfileResponse);
  rpc GetLanguageProfiles(LanguageProfilesRequest) returns (LanguageProfilesResponse);
  rpc UpdateLanguageProfile(UpdateLanguageProfileRequest) returns (UpdateLanguageProfileResponse);
}
```

### 7. Notification and Alert Service 🔴 **LOW PRIORITY**

**Purpose**: Multi-channel notifications
**Current Status in GCommon**: ❌ **Missing**
**Subtitle Manager Usage**: Enterprise alerting

**Required Services:**
```protobuf
service NotificationService {
  // Notification management
  rpc SendNotification(SendNotificationRequest) returns (SendNotificationResponse);
  rpc ConfigureNotificationChannel(ConfigureChannelRequest) returns (ConfigureChannelResponse);
  rpc TestNotificationChannel(TestChannelRequest) returns (TestChannelResponse);
  rpc GetNotificationHistory(NotificationHistoryRequest) returns (NotificationHistoryResponse);

  // Channel-specific operations
  rpc SendDiscordMessage(DiscordMessageRequest) returns (DiscordMessageResponse);
  rpc SendTelegramMessage(TelegramMessageRequest) returns (TelegramMessageResponse);
  rpc SendEmail(EmailRequest) returns (EmailResponse);
}
```

### 8. Analytics and Monitoring Service 🔴 **LOW PRIORITY**

**Purpose**: Usage analytics and system monitoring
**Current Status in GCommon**: 🔶 **Partial** (basic metrics exists)
**Subtitle Manager Usage**: Operational insights

**Required Enhancements to Existing Metrics Module:**
```protobuf
service AnalyticsService {
  // Usage analytics
  rpc RecordSubtitleDownload(DownloadEventRequest) returns (DownloadEventResponse);
  rpc RecordTranslationUsage(TranslationEventRequest) returns (TranslationEventResponse);
  rpc GetUsageStatistics(UsageStatsRequest) returns (UsageStatsResponse);
  rpc GetProviderPerformance(ProviderStatsRequest) returns (ProviderStatsResponse);

  // System monitoring
  rpc GetSystemHealth(SystemHealthRequest) returns (SystemHealthResponse);
  rpc GetPerformanceMetrics(PerformanceMetricsRequest) returns (PerformanceMetricsResponse);
}
```

---

## Required Message Types

### Core Media Types

**File**: `pkg/media/proto/messages/`

```protobuf
// Media file representation
message MediaFile {
  string id = 1;
  string path = 2;
  string filename = 3;
  MediaType type = 4;
  int64 size_bytes = 5;
  google.protobuf.Timestamp created_at = 6;
  google.protobuf.Timestamp modified_at = 7;
  MediaMetadata metadata = 8;
  repeated SubtitleTrack subtitle_tracks = 9;
  repeated AudioTrack audio_tracks = 10;
  MediaQuality quality = 11;
}

// Media metadata from external sources
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
  SeriesInfo series_info = 12; // For TV shows
  MovieInfo movie_info = 13;   // For movies
}

// TV series specific information
message SeriesInfo {
  int32 season = 1;
  int32 episode = 2;
  string series_name = 3;
  string episode_title = 4;
  google.protobuf.Timestamp air_date = 5;
}

// Movie specific information
message MovieInfo {
  google.protobuf.Timestamp release_date = 1;
  int64 budget = 2;
  int64 revenue = 3;
  int32 runtime_minutes = 4;
}

// Subtitle track information
message SubtitleTrack {
  int32 index = 1;
  string language = 2;
  string codec = 3;
  string title = 4;
  bool forced = 5;
  bool hearing_impaired = 6;
  bool default_track = 7;
}

// Audio track information
message AudioTrack {
  int32 index = 1;
  string language = 2;
  string codec = 3;
  string title = 4;
  int32 channels = 5;
  int32 sample_rate = 6;
  bool default_track = 7;
}

// Media quality assessment
message MediaQuality {
  Resolution resolution = 1;
  string video_codec = 2;
  int32 bitrate_kbps = 3;
  float duration_seconds = 4;
  QualityScore quality_score = 5;
}

// Enums
enum MediaType {
  MEDIA_TYPE_UNSPECIFIED = 0;
  MEDIA_TYPE_MOVIE = 1;
  MEDIA_TYPE_TV_EPISODE = 2;
  MEDIA_TYPE_DOCUMENTARY = 3;
  MEDIA_TYPE_ANIME = 4;
}

enum Resolution {
  RESOLUTION_UNSPECIFIED = 0;
  RESOLUTION_480P = 1;
  RESOLUTION_720P = 2;
  RESOLUTION_1080P = 3;
  RESOLUTION_4K = 4;
}

enum QualityScore {
  QUALITY_SCORE_UNSPECIFIED = 0;
  QUALITY_SCORE_LOW = 1;
  QUALITY_SCORE_MEDIUM = 2;
  QUALITY_SCORE_HIGH = 3;
  QUALITY_SCORE_EXCELLENT = 4;
}
```

### Subtitle Management Types

**File**: `pkg/subtitles/proto/messages/`

```protobuf
// Subtitle file representation
message SubtitleFile {
  string id = 1;
  string path = 2;
  string language = 3;
  SubtitleFormat format = 4;
  string encoding = 5;
  int32 subtitle_count = 6;
  google.protobuf.Timestamp created_at = 7;
  SubtitleMetadata metadata = 8;
  SubtitleQuality quality = 9;
  string associated_media_id = 10;
}

// Subtitle metadata and scoring
message SubtitleMetadata {
  string provider = 1;
  string release_group = 2;
  string uploader = 3;
  int32 download_count = 4;
  float rating = 5;
  google.protobuf.Timestamp upload_date = 6;
  bool hearing_impaired = 7;
  bool forced = 8;
  repeated string tags = 9;
}

// Subtitle quality assessment
message SubtitleQuality {
  int32 sync_score = 1;        // 0-100
  int32 translation_score = 2; // 0-100
  int32 format_score = 3;      // 0-100
  int32 overall_score = 4;     // 0-100
  repeated QualityIssue issues = 5;
}

// Quality issues found in subtitle
message QualityIssue {
  QualityIssueType type = 1;
  string description = 2;
  int32 severity = 3; // 1-10
  string context = 4;
}

// Subtitle search result
message SubtitleSearchResult {
  string id = 1;
  string provider = 2;
  string language = 3;
  string release_name = 4;
  SubtitleMetadata metadata = 5;
  string download_url = 6;
  int32 match_score = 7; // 0-100
  bool requires_auth = 8;
}

// Subtitle provider configuration
message ProviderConfig {
  string name = 1;
  bool enabled = 2;
  map<string, string> settings = 3;
  ProviderAuth auth = 4;
  RateLimit rate_limit = 5;
  int32 priority = 6;
  repeated string supported_languages = 7;
}

// Provider authentication
message ProviderAuth {
  AuthType type = 1;
  string username = 2;
  string password = 3;
  string api_key = 4;
  string token = 5;
}

// Rate limiting configuration
message RateLimit {
  int32 requests_per_minute = 1;
  int32 requests_per_hour = 2;
  int32 requests_per_day = 3;
  int32 burst_limit = 4;
}

// Enums
enum SubtitleFormat {
  SUBTITLE_FORMAT_UNSPECIFIED = 0;
  SUBTITLE_FORMAT_SRT = 1;
  SUBTITLE_FORMAT_VTT = 2;
  SUBTITLE_FORMAT_ASS = 3;
  SUBTITLE_FORMAT_SSA = 4;
  SUBTITLE_FORMAT_SUB = 5;
  SUBTITLE_FORMAT_SBV = 6;
}

enum QualityIssueType {
  QUALITY_ISSUE_TYPE_UNSPECIFIED = 0;
  QUALITY_ISSUE_TYPE_TIMING = 1;
  QUALITY_ISSUE_TYPE_ENCODING = 2;
  QUALITY_ISSUE_TYPE_MISSING_TEXT = 3;
  QUALITY_ISSUE_TYPE_FORMAT_ERROR = 4;
  QUALITY_ISSUE_TYPE_SYNC_DRIFT = 5;
}

enum AuthType {
  AUTH_TYPE_UNSPECIFIED = 0;
  AUTH_TYPE_NONE = 1;
  AUTH_TYPE_BASIC = 2;
  AUTH_TYPE_API_KEY = 3;
  AUTH_TYPE_OAUTH = 4;
  AUTH_TYPE_TOKEN = 5;
}
```

### Translation and Transcription Types

**File**: `pkg/translation/proto/messages/`

```protobuf
// Translation request
message Translation {
  string id = 1;
  string source_text = 2;
  string translated_text = 3;
  string source_language = 4;
  string target_language = 5;
  TranslationProvider provider = 6;
  float confidence_score = 7;
  google.protobuf.Timestamp created_at = 8;
  TranslationMetadata metadata = 9;
}

// Translation metadata
message TranslationMetadata {
  string model_version = 1;
  int32 character_count = 2;
  float processing_time_ms = 3;
  map<string, string> provider_metadata = 4;
}

// Language profile for translation preferences
message LanguageProfile {
  string id = 1;
  string name = 2;
  repeated LanguagePreference preferences = 3;
  TranslationProvider default_provider = 4;
  bool auto_translate = 5;
  string user_id = 6;
}

// Individual language preference
message LanguagePreference {
  string language_code = 1;
  int32 priority = 2;
  bool enabled = 3;
  bool hearing_impaired = 4;
  bool forced_only = 5;
}

// Transcription result
message Transcription {
  string id = 1;
  string audio_file_path = 2;
  string transcribed_text = 3;
  string language = 4;
  TranscriptionProvider provider = 5;
  float confidence_score = 6;
  repeated TranscriptionSegment segments = 7;
  google.protobuf.Timestamp created_at = 8;
}

// Individual transcription segment with timing
message TranscriptionSegment {
  string text = 1;
  float start_time_seconds = 2;
  float end_time_seconds = 3;
  float confidence = 4;
  repeated string words = 5;
}

// Whisper configuration
message WhisperConfig {
  WhisperModel model = 1;
  string language = 2;
  bool auto_detect_language = 3;
  float temperature = 4;
  int32 beam_size = 5;
  bool word_timestamps = 6;
  string initial_prompt = 7;
}

// Enums
enum TranslationProvider {
  TRANSLATION_PROVIDER_UNSPECIFIED = 0;
  TRANSLATION_PROVIDER_GOOGLE = 1;
  TRANSLATION_PROVIDER_OPENAI = 2;
  TRANSLATION_PROVIDER_AZURE = 3;
  TRANSLATION_PROVIDER_AMAZON = 4;
}

enum TranscriptionProvider {
  TRANSCRIPTION_PROVIDER_UNSPECIFIED = 0;
  TRANSCRIPTION_PROVIDER_WHISPER = 1;
  TRANSCRIPTION_PROVIDER_OPENAI_WHISPER = 2;
  TRANSCRIPTION_PROVIDER_AZURE_SPEECH = 3;
  TRANSCRIPTION_PROVIDER_GOOGLE_SPEECH = 4;
}

enum WhisperModel {
  WHISPER_MODEL_UNSPECIFIED = 0;
  WHISPER_MODEL_TINY = 1;
  WHISPER_MODEL_BASE = 2;
  WHISPER_MODEL_SMALL = 3;
  WHISPER_MODEL_MEDIUM = 4;
  WHISPER_MODEL_LARGE = 5;
  WHISPER_MODEL_LARGE_V2 = 6;
  WHISPER_MODEL_LARGE_V3 = 7;
}
```

### Integration and Webhook Types

**File**: `pkg/integration/proto/messages/`

```protobuf
// External service integration
message ServiceIntegration {
  string id = 1;
  IntegrationType type = 2;
  string name = 3;
  string base_url = 4;
  string api_key = 5;
  bool enabled = 6;
  IntegrationConfig config = 7;
  google.protobuf.Timestamp last_sync = 8;
  IntegrationStatus status = 9;
}

// Integration configuration
message IntegrationConfig {
  map<string, string> settings = 1;
  repeated PathMapping path_mappings = 2;
  SyncSettings sync_settings = 3;
  repeated string monitored_libraries = 4;
}

// Path mapping for cross-system compatibility
message PathMapping {
  string local_path = 1;
  string remote_path = 2;
  bool enabled = 3;
}

// Synchronization settings
message SyncSettings {
  bool auto_sync = 1;
  int32 sync_interval_minutes = 2;
  bool sync_on_startup = 3;
  repeated string sync_events = 4;
}

// Webhook event
message WebhookEvent {
  string id = 1;
  string source = 2;
  WebhookEventType event_type = 3;
  map<string, string> payload = 4;
  google.protobuf.Timestamp received_at = 5;
  google.protobuf.Timestamp processed_at = 6;
  WebhookProcessingStatus status = 7;
  string error_message = 8;
}

// Webhook configuration
message WebhookConfig {
  string id = 1;
  string url = 2;
  string secret = 3;
  repeated WebhookEventType event_types = 4;
  bool enabled = 5;
  int32 timeout_seconds = 6;
  int32 retry_count = 7;
}

// External API response
message ExternalAPIResponse {
  int32 status_code = 1;
  map<string, string> headers = 2;
  bytes body = 3;
  float response_time_ms = 4;
  string error_message = 5;
}

// Enums
enum IntegrationType {
  INTEGRATION_TYPE_UNSPECIFIED = 0;
  INTEGRATION_TYPE_SONARR = 1;
  INTEGRATION_TYPE_RADARR = 2;
  INTEGRATION_TYPE_PLEX = 3;
  INTEGRATION_TYPE_JELLYFIN = 4;
  INTEGRATION_TYPE_EMBY = 5;
}

enum IntegrationStatus {
  INTEGRATION_STATUS_UNSPECIFIED = 0;
  INTEGRATION_STATUS_CONNECTED = 1;
  INTEGRATION_STATUS_DISCONNECTED = 2;
  INTEGRATION_STATUS_ERROR = 3;
  INTEGRATION_STATUS_SYNCING = 4;
}

enum WebhookEventType {
  WEBHOOK_EVENT_TYPE_UNSPECIFIED = 0;
  WEBHOOK_EVENT_TYPE_MEDIA_ADDED = 1;
  WEBHOOK_EVENT_TYPE_MEDIA_UPDATED = 2;
  WEBHOOK_EVENT_TYPE_MEDIA_DELETED = 3;
  WEBHOOK_EVENT_TYPE_SUBTITLE_DOWNLOADED = 4;
  WEBHOOK_EVENT_TYPE_TRANSLATION_COMPLETED = 5;
  WEBHOOK_EVENT_TYPE_SYNC_COMPLETED = 6;
}

enum WebhookProcessingStatus {
  WEBHOOK_PROCESSING_STATUS_UNSPECIFIED = 0;
  WEBHOOK_PROCESSING_STATUS_PENDING = 1;
  WEBHOOK_PROCESSING_STATUS_PROCESSING = 2;
  WEBHOOK_PROCESSING_STATUS_COMPLETED = 3;
  WEBHOOK_PROCESSING_STATUS_FAILED = 4;
  WEBHOOK_PROCESSING_STATUS_RETRYING = 5;
}
```

### User Profile and Preference Types

**File**: `pkg/profile/proto/messages/`

```protobuf
// User profile extension
message UserProfile {
  string user_id = 1;
  UserPreferences preferences = 2;
  repeated LanguageProfile language_profiles = 3;
  repeated ProviderPreference provider_preferences = 4;
  UserSettings settings = 5;
  google.protobuf.Timestamp created_at = 6;
  google.protobuf.Timestamp updated_at = 7;
}

// User preferences
message UserPreferences {
  string default_language = 1;
  repeated string preferred_languages = 2;
  bool auto_download_subtitles = 3;
  bool prefer_hearing_impaired = 4;
  bool prefer_forced_subtitles = 5;
  SubtitleFormat preferred_format = 6;
  TranslationProvider preferred_translation_provider = 7;
  int32 subtitle_quality_threshold = 8;
}

// Provider preference
message ProviderPreference {
  string provider_name = 1;
  int32 priority = 2;
  bool enabled = 3;
  map<string, string> custom_settings = 4;
}

// User interface settings
message UserSettings {
  string theme = 1;
  string language = 2;
  string timezone = 3;
  NotificationSettings notification_settings = 4;
  DisplaySettings display_settings = 5;
}

// Notification preferences
message NotificationSettings {
  bool email_enabled = 1;
  bool discord_enabled = 2;
  bool telegram_enabled = 3;
  repeated NotificationEvent enabled_events = 4;
  string email_address = 5;
  string discord_webhook_url = 6;
  string telegram_chat_id = 7;
}

// Display preferences
message DisplaySettings {
  int32 items_per_page = 1;
  string date_format = 2;
  string time_format = 3;
  bool show_advanced_options = 4;
  repeated string hidden_columns = 5;
}

// Enums
enum NotificationEvent {
  NOTIFICATION_EVENT_UNSPECIFIED = 0;
  NOTIFICATION_EVENT_DOWNLOAD_COMPLETED = 1;
  NOTIFICATION_EVENT_TRANSLATION_COMPLETED = 2;
  NOTIFICATION_EVENT_SYNC_COMPLETED = 3;
  NOTIFICATION_EVENT_ERROR_OCCURRED = 4;
  NOTIFICATION_EVENT_SCAN_COMPLETED = 5;
}
```

---

## Service Definitions Needed

### Priority 1: Core Media Services

**Location**: `pkg/media/proto/services/`

#### MediaService
- **Purpose**: Core media file and library management
- **Methods**: 12 RPC methods for scanning, metadata, and file operations
- **Dependencies**: Database, Config, Auth modules
- **Estimated Complexity**: Large (will be heavily used)

#### SubtitleService
- **Purpose**: Subtitle processing, conversion, and synchronization
- **Methods**: 10 RPC methods for subtitle operations
- **Dependencies**: Media, Translation, Provider modules
- **Estimated Complexity**: Large (core business logic)

#### SubtitleProviderService
- **Purpose**: Managing 40+ subtitle provider integrations
- **Methods**: 4 RPC methods for provider configuration and testing
- **Dependencies**: Config, Auth modules
- **Estimated Complexity**: Medium (provider abstraction)

### Priority 2: Language Processing Services

**Location**: `pkg/translation/proto/services/`

#### TranslationService
- **Purpose**: Text and subtitle translation via Google/OpenAI
- **Methods**: 6 RPC methods for translation operations
- **Dependencies**: Config, Auth modules
- **Estimated Complexity**: Medium (external API integration)

#### TranscriptionService
- **Purpose**: Audio transcription via Whisper and other services
- **Methods**: 6 RPC methods for transcription operations
- **Dependencies**: Media, Config modules
- **Estimated Complexity**: Medium (Whisper integration)

### Priority 3: Integration Services

**Location**: `pkg/integration/proto/services/`

#### IntegrationService
- **Purpose**: Sonarr, Radarr, Plex integration
- **Methods**: 6 RPC methods for external service integration
- **Dependencies**: Config, Auth, Webhook modules
- **Estimated Complexity**: Medium (external API coordination)

#### ExternalAPIService
- **Purpose**: TheMovieDB and other metadata APIs
- **Methods**: 3 RPC methods for external data fetching
- **Dependencies**: Config, Cache modules
- **Estimated Complexity**: Small (API wrapper)

### Priority 4: User and Task Services

**Location**: `pkg/profile/proto/services/` and `pkg/task/proto/services/`

#### UserProfileService (extends existing auth)
- **Purpose**: User preferences and language profiles
- **Methods**: 6 RPC methods for profile management
- **Dependencies**: Auth module
- **Estimated Complexity**: Small (data management)

#### TaskService (extends existing queue)
- **Purpose**: Background job processing for subtitle operations
- **Methods**: 6 RPC methods for job management
- **Dependencies**: Queue, Auth modules
- **Estimated Complexity**: Medium (async processing)

#### SchedulerService (extends existing queue)
- **Purpose**: Cron-based scheduling for library scans
- **Methods**: 4 RPC methods for schedule management
- **Dependencies**: Queue, Config modules
- **Estimated Complexity**: Small (cron wrapper)

---

## Implementation Priority Matrix

### 🔥 **Phase 1: Core Media & Subtitle Operations** (Weeks 1-4)
**Impact**: High | **Effort**: High | **Dependencies**: Low

| Service                 | Priority | Estimated Work | Key Benefits              |
| ----------------------- | -------- | -------------- | ------------------------- |
| MediaService            | ⭐⭐⭐      | 3 weeks        | Core business foundation  |
| SubtitleService         | ⭐⭐⭐      | 3 weeks        | Primary value proposition |
| SubtitleProviderService | ⭐⭐⭐      | 2 weeks        | Provider abstraction      |

**Deliverables:**
- Complete media file management
- Subtitle format conversion and synchronization
- Provider registry and configuration
- ~80 new message types

### 🚀 **Phase 2: Language Processing** (Weeks 5-7)
**Impact**: High | **Effort**: Medium | **Dependencies**: Medium

| Service              | Priority | Estimated Work | Key Benefits               |
| -------------------- | -------- | -------------- | -------------------------- |
| TranslationService   | ⭐⭐       | 2 weeks        | Translation feature parity |
| TranscriptionService | ⭐⭐       | 2 weeks        | Whisper integration        |

**Deliverables:**
- Google Translate and OpenAI integration
- Whisper transcription services
- Language detection and management
- ~40 new message types

### 🔧 **Phase 3: Integration & Automation** (Weeks 8-10)
**Impact**: Medium | **Effort**: Medium | **Dependencies**: High

| Service            | Priority | Estimated Work | Key Benefits          |
| ------------------ | -------- | -------------- | --------------------- |
| IntegrationService | ⭐⭐       | 2 weeks        | Enterprise features   |
| TaskService        | ⭐⭐       | 1.5 weeks      | Background processing |
| SchedulerService   | ⭐        | 1 week         | Automated operations  |

**Deliverables:**
- Sonarr/Radarr/Plex integration
- Background job processing
- Cron-based scheduling
- ~30 new message types

### 🎨 **Phase 4: User Experience & Analytics** (Weeks 11-12)
**Impact**: Medium | **Effort**: Low | **Dependencies**: High

| Service             | Priority | Estimated Work | Key Benefits         |
| ------------------- | -------- | -------------- | -------------------- |
| UserProfileService  | ⭐        | 1 week         | User customization   |
| NotificationService | ⭐        | 1 week         | User engagement      |
| AnalyticsService    | ⭐        | 1 week         | Operational insights |

**Deliverables:**
- User preferences and language profiles
- Multi-channel notifications
- Usage analytics and monitoring
- ~25 new message types

### 📊 **Total Implementation Estimate**
- **Timeline**: 12 weeks for full implementation
- **New Message Types**: ~175 messages across 8 modules
- **New Services**: 11 new services + enhancements to 3 existing
- **Integration Effort**: 2-3 weeks for subtitle-manager migration

---

## Integration Strategy

### Migration Approach

**1. Gradual Service Migration**
```go
// Phase 1: Add gRPC alongside existing implementations
type MediaManager struct {
    localImpl  *LocalMediaService     // Current implementation
    grpcClient media.MediaServiceClient // New gCommon service
    useGRPC    bool                   // Feature flag
}

// Phase 2: Implement hybrid mode
func (m *MediaManager) ScanLibrary(ctx context.Context, path string) error {
    if m.useGRPC {
        return m.grpcClient.ScanLibrary(ctx, &media.ScanLibraryRequest{Path: path})
    }
    return m.localImpl.ScanLibrary(ctx, path)
}

// Phase 3: Remove local implementations
```

**2. Protobuf-First Development**
- All new features use gCommon protobuf messages
- Existing types gradually converted to protobuf equivalents
- Maintain backward compatibility during transition

**3. Configuration Migration**
```yaml
# Current subtitle-manager.yaml
providers:
  opensubtitles:
    enabled: true
    username: "user"
    password: "pass"

# New gcommon-integrated config
gcommon:
  subtitle_provider_service:
    enabled: true
    endpoint: "localhost:50051"

providers: # Backward compatibility maintained
  opensubtitles:
    enabled: true
    username: "user"
    password: "pass"
```

### Backward Compatibility Strategy

**1. Interface Preservation**
```go
// Existing subtitle-manager interfaces remain unchanged
type SubtitleProvider interface {
    Search(ctx context.Context, query SearchQuery) ([]Subtitle, error)
    Download(ctx context.Context, id string) (*Subtitle, error)
}

// New implementation uses gCommon internally
type GCommonSubtitleProvider struct {
    client subtitles.SubtitleProviderServiceClient
}

func (p *GCommonSubtitleProvider) Search(ctx context.Context, query SearchQuery) ([]Subtitle, error) {
    req := &subtitles.SearchSubtitlesRequest{
        Query: query.ToProto(),
        // ... map other fields
    }
    resp, err := p.client.SearchSubtitles(ctx, req)
    return ConvertFromProto(resp.Results), err
}
```

**2. Data Migration Tools**
```bash
# Migrate existing SQLite data to gCommon format
subtitle-manager migrate-to-gcommon --db-path ./data.db --gcommon-endpoint localhost:50051

# Export current configuration to gCommon
subtitle-manager export-config --format gcommon --output gcommon-config.yaml
```

### Testing Strategy

**1. Integration Test Suite**
```go
// Test both local and gCommon implementations
func TestMediaServiceParity(t *testing.T) {
    // Setup local implementation
    localService := &LocalMediaService{}

    // Setup gCommon implementation
    grpcService := setupGCommonMediaService(t)

    // Run identical test suite against both
    testCases := []struct{
        name string
        test func(MediaService) error
    }{
        {"ScanLibrary", testScanLibrary},
        {"GetMediaInfo", testGetMediaInfo},
        // ... more tests
    }

    for _, tc := range testCases {
        t.Run(tc.name+"_Local", func(t *testing.T) {
            err := tc.test(localService)
            assert.NoError(t, err)
        })

        t.Run(tc.name+"_GCommon", func(t *testing.T) {
            err := tc.test(grpcService)
            assert.NoError(t, err)
        })
    }
}
```

**2. Performance Benchmarks**
```go
func BenchmarkSubtitleConversion(b *testing.B) {
    implementations := map[string]SubtitleService{
        "Local":   &LocalSubtitleService{},
        "GCommon": &GCommonSubtitleService{},
    }

    for name, impl := range implementations {
        b.Run(name, func(b *testing.B) {
            for i := 0; i < b.N; i++ {
                _, err := impl.ConvertFormat(testSubtitle, "srt")
                assert.NoError(b, err)
            }
        })
    }
}
```

---

## Migration Roadmap

### Phase 1: Foundation (Weeks 1-4)
**Goal**: Core media and subtitle services operational

**Week 1-2: Media Service Implementation**
- [ ] Implement `MediaService` with file scanning and metadata operations
- [ ] Create `MediaFile`, `MediaMetadata`, and related message types
- [ ] Add support for directory watching and library management
- [ ] Implement media quality assessment and validation

**Week 3-4: Subtitle Service Implementation**
- [ ] Implement `SubtitleService` with format conversion and synchronization
- [ ] Create `SubtitleFile`, `SubtitleMetadata`, and quality scoring types
- [ ] Add subtitle provider abstraction layer
- [ ] Implement subtitle search and download operations

**Integration Tasks:**
- [ ] Update subtitle-manager to use new media types optionally
- [ ] Create adapter layer for backward compatibility
- [ ] Add feature flags for gradual migration

### Phase 2: Language Processing (Weeks 5-7)
**Goal**: Translation and transcription services integrated

**Week 5-6: Translation Service**
- [ ] Implement `TranslationService` with Google and OpenAI support
- [ ] Create translation metadata and language profile types
- [ ] Add batch translation capabilities
- [ ] Implement language detection and preference management

**Week 7: Transcription Service**
- [ ] Implement `TranscriptionService` with Whisper integration
- [ ] Create transcription result and configuration types
- [ ] Add audio processing and segment timing
- [ ] Implement model selection and optimization

**Integration Tasks:**
- [ ] Migrate subtitle-manager translation features to gCommon
- [ ] Update Whisper integration to use gRPC services
- [ ] Add language profile management to web UI

### Phase 3: Integration & Automation (Weeks 8-10)
**Goal**: External services and background processing

**Week 8: Integration Service**
- [ ] Implement `IntegrationService` for Sonarr/Radarr/Plex
- [ ] Create webhook event processing and configuration types
- [ ] Add external API abstraction for metadata services
- [ ] Implement path mapping and sync configuration

**Week 9: Task Management**
- [ ] Enhance existing queue module with subtitle-specific operations
- [ ] Implement `TaskService` for background job processing
- [ ] Add progress tracking and job history
- [ ] Create batch operation support

**Week 10: Scheduler Service**
- [ ] Implement `SchedulerService` with cron-based scheduling
- [ ] Add library scan automation
- [ ] Create maintenance task scheduling
- [ ] Implement job retry and error handling

**Integration Tasks:**
- [ ] Migrate subtitle-manager webhook system to gCommon
- [ ] Update background job processing to use gRPC
- [ ] Add scheduler integration to web UI

### Phase 4: User Experience (Weeks 11-12)
**Goal**: User profiles and operational features

**Week 11: User Profiles**
- [ ] Enhance existing auth module with profile management
- [ ] Implement `UserProfileService` for preferences and settings
- [ ] Create language profile and provider preference types
- [ ] Add user customization and interface settings

**Week 12: Notifications & Analytics**
- [ ] Implement `NotificationService` for multi-channel alerts
- [ ] Enhance existing metrics module with subtitle-specific analytics
- [ ] Add usage tracking and performance monitoring
- [ ] Create system health and alerting

**Integration Tasks:**
- [ ] Complete subtitle-manager migration to gCommon services
- [ ] Add user profile management to web UI
- [ ] Implement notification configuration interface
- [ ] Add analytics dashboard to web UI

### Post-Migration Cleanup (Week 13)
- [ ] Remove deprecated local implementations
- [ ] Update documentation and examples
- [ ] Performance optimization and load testing
- [ ] Final integration testing and validation

---

## Benefits and Impact

### For Subtitle Manager

**1. Reduced Codebase Complexity**
- **Before**: ~50,000 LOC with multiple database implementations
- **After**: ~30,000 LOC focused on business logic and UI
- **Benefit**: 40% reduction in maintenance burden

**2. Enhanced Reliability**
- **Before**: Custom implementations with potential bugs
- **After**: Shared, tested services from gCommon
- **Benefit**: Production-tested reliability and consistency

**3. Better Performance**
- **Before**: Direct database calls and synchronous operations
- **After**: Optimized gRPC services with connection pooling
- **Benefit**: Improved scalability and response times

**4. Enterprise Features**
- **Before**: Basic functionality with limited scalability
- **After**: Enterprise-grade services (PostgreSQL, clustering, etc.)
- **Benefit**: Production deployment capabilities

### For GCommon Project

**1. Real-World Validation**
- **Before**: Theoretical protobuf services without concrete use cases
- **After**: Production-proven services tested by subtitle-manager
- **Benefit**: Validates API design and identifies edge cases

**2. Domain Expansion**
- **Before**: Generic infrastructure services only
- **After**: Media processing and content management capabilities
- **Benefit**: Broadens gCommon's applicability to media applications

**3. Service Maturation**
- **Before**: Basic CRUD operations in most modules
- **After**: Complex workflows and real-world business logic
- **Benefit**: More sophisticated and useful service offerings

**4. Documentation and Examples**
- **Before**: Limited real-world usage examples
- **After**: Complete application demonstrating gCommon integration
- **Benefit**: Better developer onboarding and adoption

### For the Broader Ecosystem

**1. Microservices Reference Architecture**
- Complete example of migrating monolithic application to microservices
- Demonstrates gradual migration strategies and backward compatibility
- Shows real-world gRPC service design patterns

**2. Media Processing Framework**
- Reusable services for other media management applications
- Standardized APIs for subtitle, translation, and transcription services
- Foundation for building additional media-focused applications

**3. Production Readiness Template**
- Authentication, authorization, and user management
- Background job processing and scheduling
- Notification and monitoring integration
- Configuration management and deployment patterns

---

## Recommended Next Steps

### Immediate Actions (Next 2 Weeks)

**1. Architecture Planning**
- [ ] Review and approve this requirements analysis
- [ ] Create detailed service interface specifications
- [ ] Design protobuf package structure and naming conventions
- [ ] Plan backward compatibility and migration strategy

**2. Development Environment Setup**
- [ ] Create feature branches for new service modules
- [ ] Set up development and testing infrastructure for new services
- [ ] Establish CI/CD pipelines for protobuf generation and testing
- [ ] Create integration testing framework

**3. Stakeholder Alignment**
- [ ] Review requirements with subtitle-manager maintainers
- [ ] Confirm service interface designs and message types
- [ ] Establish timeline and resource allocation
- [ ] Define success criteria and acceptance tests

### Short-term Implementation (Weeks 3-6)

**1. Core Service Development**
- [ ] Begin implementation of MediaService and SubtitleService
- [ ] Create foundational message types and enums
- [ ] Implement basic CRUD operations for each service
- [ ] Set up service registration and discovery

**2. Integration Preparation**
- [ ] Create adapter layer in subtitle-manager for gCommon services
- [ ] Implement feature flags for gradual service migration
- [ ] Develop data migration tools and scripts
- [ ] Create comprehensive test suite for service parity

### Medium-term Goals (Weeks 7-12)

**1. Service Completion**
- [ ] Complete all Priority 1 and Priority 2 services
- [ ] Implement comprehensive error handling and logging
- [ ] Add performance monitoring and metrics collection
- [ ] Create complete documentation and examples

**2. Production Migration**
- [ ] Begin gradual migration of subtitle-manager to gCommon services
- [ ] Conduct performance testing and optimization
- [ ] Implement production monitoring and alerting
- [ ] Complete integration testing and validation

### Long-term Vision (Beyond 12 Weeks)

**1. Ecosystem Development**
- [ ] Open source the enhanced gCommon services
- [ ] Create developer documentation and migration guides
- [ ] Build additional applications using the media services
- [ ] Establish community contribution guidelines

**2. Service Enhancement**
- [ ] Add advanced features based on real-world usage
- [ ] Implement additional integrations and protocols
- [ ] Optimize performance for large-scale deployments
- [ ] Develop enterprise features and support options

---

## Conclusion

This analysis reveals that subtitle-manager represents an ideal real-world use case for expanding gCommon's capabilities into the media processing domain. The implementation of the required services will not only benefit subtitle-manager by reducing complexity and improving reliability, but will also significantly enhance gCommon's value proposition as a comprehensive microservices framework.

The proposed 12-week implementation plan provides a structured approach to developing ~175 new message types and 11 new services, with clear phases that allow for gradual migration and validation. The combination of subtitle-manager's production requirements and gCommon's infrastructure foundation creates an opportunity to build a robust, reusable media processing platform.

The investment in these services will pay dividends through improved maintainability, enhanced reliability, and the creation of a reference architecture for other media management applications. This represents a strategic opportunity to demonstrate gCommon's potential while solving real-world problems in the media processing domain.

---

**Document Version**: 1.0
**Last Updated**: July 27, 2025
**Next Review**: August 10, 2025
**Status**: Ready for Implementation Planning
