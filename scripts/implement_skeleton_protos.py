#!/usr/bin/env python3
# file: implement_skeleton_protos.py
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7890-abcd-ef1234567890

"""
Implement all skeleton protobuf files with proper message definitions.
This script identifies skeleton files and implements appropriate message structures.
"""

import os
from pathlib import Path
from typing import List


def get_proto_files(base_dir: str) -> List[str]:
    """Get all .proto files recursively."""
    proto_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".proto"):
                proto_files.append(os.path.join(root, file))
    return proto_files


def is_skeleton_file(file_path: str) -> bool:
    """Check if a proto file is a skeleton file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            return "SKELETON_FILE" in content
    except Exception:
        return False


def get_message_name_from_filename(file_path: str) -> str:
    """Extract message name from filename."""
    filename = Path(file_path).stem
    # Convert snake_case to PascalCase
    parts = filename.split("_")
    return "".join(word.capitalize() for word in parts)


def implement_auth_skeleton(file_path: str, content: str) -> str:
    """Implement auth-related skeleton files."""
    filename = Path(file_path).stem

    # Auth implementation patterns
    implementations = {
        "enable_2fa_request": """message Enable2FaRequest {
  // User ID requesting 2FA enablement
  string user_id = 1;

  // Phone number for SMS-based 2FA
  optional string phone_number = 2;

  // Whether to use authenticator app
  bool use_authenticator = 3;

  // Backup codes preference
  bool generate_backup_codes = 4;
}""",
        "enable_2fa_response": """message Enable2FaResponse {
  // Success status
  bool success = 1;

  // QR code for authenticator setup (base64 encoded)
  optional string qr_code = 2;

  // Secret key for manual entry
  optional string secret_key = 3;

  // Backup codes (if requested)
  repeated string backup_codes = 4;

  // Error message if operation failed
  optional string error_message = 5;
}""",
        "disable_2fa_request": """message Disable2FaRequest {
  // User ID requesting 2FA disable
  string user_id = 1;

  // Current password for verification
  string password = 2;

  // 2FA code for verification
  string verification_code = 3;
}""",
        "disable_2fa_response": """message Disable2FaResponse {
  // Success status
  bool success = 1;

  // Error message if operation failed
  optional string error_message = 2;
}""",
        "verify_2fa_request": """message Verify2FaRequest {
  // User ID
  string user_id = 1;

  // 2FA verification code
  string code = 2;

  // Type of 2FA being verified
  enum TwoFaType {
    TWO_FA_TYPE_UNSPECIFIED = 0;
    TWO_FA_TYPE_TOTP = 1;  // Time-based One-Time Password
    TWO_FA_TYPE_SMS = 2;   // SMS code
    TWO_FA_TYPE_BACKUP = 3; // Backup code
  }
  TwoFaType type = 3;
}""",
        "verify_2fa_response": """message Verify2FaResponse {
  // Verification success
  bool verified = 1;

  // Error message if verification failed
  optional string error_message = 2;

  // Remaining attempts (for rate limiting)
  optional int32 remaining_attempts = 3;
}""",
        "enable_mfa_request": """message EnableMfaRequest {
  // User ID requesting MFA enablement
  string user_id = 1;

  // MFA methods to enable
  repeated MfaMethod methods = 2;

  // Primary contact method
  string primary_contact = 3;
}

enum MfaMethod {
  MFA_METHOD_UNSPECIFIED = 0;
  MFA_METHOD_SMS = 1;
  MFA_METHOD_EMAIL = 2;
  MFA_METHOD_TOTP = 3;
  MFA_METHOD_HARDWARE_KEY = 4;
}""",
        "enable_mfa_response": """message EnableMfaResponse {
  // Success status
  bool success = 1;

  // Setup instructions for each method
  repeated MfaSetupInstruction setup_instructions = 2;

  // Error message if operation failed
  optional string error_message = 3;
}

message MfaSetupInstruction {
  MfaMethod method = 1;
  string instruction = 2;
  optional string qr_code = 3;
  optional string secret_key = 4;
}""",
        "disable_mfa_request": """message DisableMfaRequest {
  // User ID requesting MFA disable
  string user_id = 1;

  // Current password for verification
  string password = 2;

  // MFA verification code
  string verification_code = 3;

  // Specific methods to disable (empty = all)
  repeated MfaMethod methods = 4;
}""",
        "disable_mfa_response": """message DisableMfaResponse {
  // Success status
  bool success = 1;

  // Methods that were disabled
  repeated MfaMethod disabled_methods = 2;

  // Error message if operation failed
  optional string error_message = 3;
}""",
        "verify_mfa_request": """message VerifyMfaRequest {
  // User ID
  string user_id = 1;

  // MFA verification code
  string code = 2;

  // Method being verified
  MfaMethod method = 3;

  // Context for the verification (login, transaction, etc.)
  string context = 4;
}""",
        "verify_mfa_response": """message VerifyMfaResponse {
  // Verification success
  bool verified = 1;

  // Error message if verification failed
  optional string error_message = 2;

  // Remaining attempts (for rate limiting)
  optional int32 remaining_attempts = 3;

  // Session token if successful
  optional string session_token = 4;
}""",
        "verify_email_request": """message VerifyEmailRequest {
  // User ID or email to verify
  string identifier = 1;

  // Verification token from email
  string verification_token = 2;
}""",
        "verify_email_response": """message VerifyEmailResponse {
  // Verification success
  bool verified = 1;

  // Error message if verification failed
  optional string error_message = 2;

  // User ID that was verified
  optional string user_id = 3;
}""",
        "send_verification_email_request": """message SendVerificationEmailRequest {
  // User ID or email address
  string identifier = 1;

  // Template to use for email
  optional string template = 2;

  // Additional context data
  map<string, string> context = 3;
}""",
        "send_verification_email_response": """message SendVerificationEmailResponse {
  // Send success
  bool sent = 1;

  // Error message if send failed
  optional string error_message = 2;

  // Token expiry time
  optional int64 expires_at = 3;
}""",
        "resend_verification_request": """message ResendVerificationRequest {
  // User ID or email address
  string identifier = 1;

  // Verification type
  enum VerificationType {
    VERIFICATION_TYPE_UNSPECIFIED = 0;
    VERIFICATION_TYPE_EMAIL = 1;
    VERIFICATION_TYPE_SMS = 2;
  }
  VerificationType type = 2;
}""",
        "register_user_response": """message RegisterUserResponse {
  // Registration success
  bool success = 1;

  // User ID of created user
  optional string user_id = 2;

  // Whether email verification is required
  bool email_verification_required = 3;

  // Error message if registration failed
  optional string error_message = 4;

  // Session token if immediate login is allowed
  optional string session_token = 5;
}""",
        "delete_user_response": """message DeleteUserResponse {
  // Deletion success
  bool success = 1;

  // Error message if deletion failed
  optional string error_message = 2;

  // Data retention information
  optional string data_retention_info = 3;
}""",
        "get_auth_config_request": """message GetAuthConfigRequest {
  // Optional specific config keys to retrieve
  repeated string keys = 1;

  // Include sensitive configuration
  bool include_sensitive = 2;
}""",
        "list_permissions_request": """message ListPermissionsRequest {
  // User or role ID to list permissions for
  optional string subject_id = 1;

  // Subject type
  enum SubjectType {
    SUBJECT_TYPE_UNSPECIFIED = 0;
    SUBJECT_TYPE_USER = 1;
    SUBJECT_TYPE_ROLE = 2;
  }
  SubjectType subject_type = 2;

  // Pagination
  int32 page_size = 3;
  string page_token = 4;
}""",
        "list_permissions_response": """message ListPermissionsResponse {
  // List of permissions
  repeated Permission permissions = 1;

  // Next page token
  string next_page_token = 2;

  // Total count
  int32 total_count = 3;
}

message Permission {
  string id = 1;
  string name = 2;
  string description = 3;
  repeated string actions = 4;
  repeated string resources = 5;
  int64 created_at = 6;
  int64 updated_at = 7;
}""",
        "create_permission_request": """message CreatePermissionRequest {
  // Permission name
  string name = 1;

  // Permission description
  string description = 2;

  // Actions this permission grants
  repeated string actions = 3;

  // Resources this permission applies to
  repeated string resources = 4;
}""",
        "delete_permission_request": """message DeletePermissionRequest {
  // Permission ID to delete
  string permission_id = 1;

  // Force deletion even if assigned
  bool force = 2;
}""",
        "grant_permission_request": """message GrantPermissionRequest {
  // Subject ID (user or role)
  string subject_id = 1;

  // Subject type
  enum SubjectType {
    SUBJECT_TYPE_UNSPECIFIED = 0;
    SUBJECT_TYPE_USER = 1;
    SUBJECT_TYPE_ROLE = 2;
  }
  SubjectType subject_type = 2;

  // Permission ID to grant
  string permission_id = 3;
}""",
        "revoke_permission_request": """message RevokePermissionRequest {
  // Subject ID (user or role)
  string subject_id = 1;

  // Subject type
  enum SubjectType {
    SUBJECT_TYPE_UNSPECIFIED = 0;
    SUBJECT_TYPE_USER = 1;
    SUBJECT_TYPE_ROLE = 2;
  }
  SubjectType subject_type = 2;

  // Permission ID to revoke
  string permission_id = 3;
}""",
        "delete_role_response": """message DeleteRoleResponse {
  // Deletion success
  bool success = 1;

  // Error message if deletion failed
  optional string error_message = 2;

  // Number of users/entities that lost this role
  int32 affected_subjects = 3;
}""",
        "assign_role_response": """message AssignRoleResponse {
  // Assignment success
  bool success = 1;

  // Error message if assignment failed
  optional string error_message = 2;

  // Effective permissions after assignment
  repeated string effective_permissions = 3;
}""",
        "revoke_role_response": """message RevokeRoleResponse {
  // Revocation success
  bool success = 1;

  // Error message if revocation failed
  optional string error_message = 2;

  // Remaining permissions after revocation
  repeated string remaining_permissions = 3;
}""",
        "list_api_keys_request": """message ListApiKeysRequest {
  // User ID to list API keys for
  optional string user_id = 1;

  // Include expired keys
  bool include_expired = 2;

  // Pagination
  int32 page_size = 3;
  string page_token = 4;
}""",
        "list_api_keys_response": """message ListApiKeysResponse {
  // List of API keys
  repeated ApiKey api_keys = 1;

  // Next page token
  string next_page_token = 2;

  // Total count
  int32 total_count = 3;
}

message ApiKey {
  string id = 1;
  string name = 2;
  string key_prefix = 3;  // Only show prefix for security
  repeated string scopes = 4;
  int64 created_at = 5;
  int64 expires_at = 6;
  int64 last_used_at = 7;
  bool is_active = 8;
}""",
        "get_api_key_request": """message GetApiKeyRequest {
  // API key ID
  string key_id = 1;

  // Include usage statistics
  bool include_stats = 2;
}""",
        "get_api_key_response": """message GetApiKeyResponse {
  // API key details
  optional ApiKey api_key = 1;

  // Usage statistics if requested
  optional ApiKeyStats stats = 2;

  // Error message if not found
  optional string error_message = 3;
}

message ApiKeyStats {
  int32 total_requests = 1;
  int32 successful_requests = 2;
  int32 failed_requests = 3;
  int64 last_used_at = 4;
  repeated DailyUsage daily_usage = 5;
}

message DailyUsage {
  string date = 1;  // YYYY-MM-DD format
  int32 request_count = 2;
}""",
        "revoke_api_key_request": """message RevokeApiKeyRequest {
  // API key ID to revoke
  string key_id = 1;

  // Reason for revocation
  optional string reason = 2;
}""",
        "revoke_api_key_response": """message RevokeApiKeyResponse {
  // Revocation success
  bool success = 1;

  // Error message if revocation failed
  optional string error_message = 2;

  // Revocation timestamp
  int64 revoked_at = 3;
}""",
        "token_metadata": """message TokenMetadata {
  // Token ID
  string token_id = 1;

  // Token type
  enum TokenType {
    TOKEN_TYPE_UNSPECIFIED = 0;
    TOKEN_TYPE_ACCESS = 1;
    TOKEN_TYPE_REFRESH = 2;
    TOKEN_TYPE_ID = 3;
    TOKEN_TYPE_API_KEY = 4;
  }
  TokenType type = 2;

  // Subject (user ID)
  string subject = 3;

  // Audience
  repeated string audience = 4;

  // Scopes
  repeated string scopes = 5;

  // Issued at timestamp
  int64 issued_at = 6;

  // Expires at timestamp
  int64 expires_at = 7;

  // Not before timestamp
  optional int64 not_before = 8;

  // Issuer
  string issuer = 9;
}""",
        "security_context": """message SecurityContext {
  // User ID
  string user_id = 1;

  // Session ID
  string session_id = 2;

  // User roles
  repeated string roles = 3;

  // User permissions
  repeated string permissions = 4;

  // Authentication method used
  enum AuthMethod {
    AUTH_METHOD_UNSPECIFIED = 0;
    AUTH_METHOD_PASSWORD = 1;
    AUTH_METHOD_MFA = 2;
    AUTH_METHOD_API_KEY = 3;
    AUTH_METHOD_OAUTH = 4;
    AUTH_METHOD_SSO = 5;
  }
  AuthMethod auth_method = 5;

  // MFA verified
  bool mfa_verified = 6;

  // IP address
  string ip_address = 7;

  // User agent
  string user_agent = 8;

  // Authentication timestamp
  int64 auth_timestamp = 9;

  // Context metadata
  map<string, string> metadata = 10;
}""",
        "permission_metadata": """message PermissionMetadata {
  // Permission ID
  string permission_id = 1;

  // Permission name
  string name = 2;

  // Resource types this permission applies to
  repeated string resource_types = 3;

  // Actions allowed by this permission
  repeated string actions = 4;

  // Conditions or constraints
  repeated PermissionCondition conditions = 5;

  // Permission level (system, organization, project, etc.)
  enum PermissionLevel {
    PERMISSION_LEVEL_UNSPECIFIED = 0;
    PERMISSION_LEVEL_SYSTEM = 1;
    PERMISSION_LEVEL_ORGANIZATION = 2;
    PERMISSION_LEVEL_PROJECT = 3;
    PERMISSION_LEVEL_RESOURCE = 4;
  }
  PermissionLevel level = 6;

  // Creation metadata
  int64 created_at = 7;
  string created_by = 8;
}

message PermissionCondition {
  string key = 1;
  string operator = 2;  // eq, ne, in, not_in, etc.
  repeated string values = 3;
}""",
        "session_metadata": """message SessionMetadata {
  // Session ID
  string session_id = 1;

  // User ID
  string user_id = 2;

  // Session start time
  int64 started_at = 3;

  // Last activity time
  int64 last_activity = 4;

  // Session expiry time
  int64 expires_at = 5;

  // IP address
  string ip_address = 6;

  // User agent
  string user_agent = 7;

  // Device information
  optional DeviceInfo device_info = 8;

  // Location information
  optional LocationInfo location_info = 9;

  // Session state
  enum SessionState {
    SESSION_STATE_UNSPECIFIED = 0;
    SESSION_STATE_ACTIVE = 1;
    SESSION_STATE_IDLE = 2;
    SESSION_STATE_EXPIRED = 3;
    SESSION_STATE_TERMINATED = 4;
  }
  SessionState state = 10;
}

message DeviceInfo {
  string device_id = 1;
  string device_type = 2;  // mobile, desktop, tablet
  string os = 3;
  string browser = 4;
  bool is_trusted = 5;
}

message LocationInfo {
  string country = 1;
  string region = 2;
  string city = 3;
  double latitude = 4;
  double longitude = 5;
}""",
        "claims": """message Claims {
  // Standard JWT claims
  string issuer = 1;       // iss
  string subject = 2;      // sub
  repeated string audience = 3; // aud
  int64 expires_at = 4;    // exp
  int64 not_before = 5;    // nbf
  int64 issued_at = 6;     // iat
  string jwt_id = 7;       // jti

  // Custom claims
  string user_id = 8;
  string username = 9;
  string email = 10;
  bool email_verified = 11;
  repeated string roles = 12;
  repeated string permissions = 13;
  repeated string scopes = 14;

  // MFA claims
  bool mfa_verified = 15;
  string mfa_method = 16;

  // Session claims
  string session_id = 17;
  bool is_refresh_token = 18;

  // Additional metadata
  map<string, string> metadata = 19;
}""",
    }

    if filename in implementations:
        # Replace the skeleton content with actual implementation
        lines = content.split("\n")
        new_lines = []
        in_skeleton_section = False

        for line in lines:
            if "SKELETON_FILE" in line:
                in_skeleton_section = True
                continue
            elif line.strip().startswith("//") and "TODO" in line:
                continue
            elif line.strip() == "" and in_skeleton_section:
                continue
            else:
                new_lines.append(line)
                if "option features.(pb.go).api_level = API_OPAQUE;" in line:
                    # Add the implementation after the options
                    new_lines.append("")
                    new_lines.append(implementations[filename])
                    new_lines.append("")
                    in_skeleton_section = False

        return "\n".join(new_lines)

    return content


def implement_queue_skeleton(file_path: str, content: str) -> str:
    """Implement queue-related skeleton files."""
    filename = Path(file_path).stem

    implementations = {
        "create_topic_response": """message CreateTopicResponse {
  // Creation success
  bool success = 1;

  // Topic ID of created topic
  optional string topic_id = 2;

  // Error message if creation failed
  optional string error_message = 3;

  // Topic metadata
  optional TopicMetadata metadata = 4;
}

message TopicMetadata {
  string name = 1;
  int32 partition_count = 2;
  int32 replication_factor = 3;
  map<string, string> config = 4;
  int64 created_at = 5;
}""",
        "list_topics_response": """message ListTopicsResponse {
  // List of topics
  repeated Topic topics = 1;

  // Next page token
  string next_page_token = 2;

  // Total count
  int32 total_count = 3;
}

message Topic {
  string id = 1;
  string name = 2;
  int32 partition_count = 3;
  int32 replication_factor = 4;
  int64 created_at = 5;
  int64 message_count = 6;
  int64 size_bytes = 7;
  map<string, string> config = 8;
}""",
        "get_partition_info_request": """message GetPartitionInfoRequest {
  // Topic ID or name
  string topic = 1;

  // Specific partition ID (optional)
  optional int32 partition_id = 2;

  // Include detailed statistics
  bool include_stats = 3;
}""",
        "delete_topic_request": """message DeleteTopicRequest {
  // Topic ID or name to delete
  string topic = 1;

  // Force deletion even if not empty
  bool force = 2;
}""",
        "delete_response": """message DeleteResponse {
  // Deletion success
  bool success = 1;

  // Error message if deletion failed
  optional string error_message = 2;

  // Number of messages deleted
  optional int64 deleted_count = 3;
}""",
        "push_response": """message PushResponse {
  // Push success
  bool success = 1;

  // Message ID assigned
  optional string message_id = 2;

  // Partition where message was stored
  optional int32 partition = 3;

  // Offset within partition
  optional int64 offset = 4;

  // Error message if push failed
  optional string error_message = 5;

  // Timestamp when message was stored
  optional int64 timestamp = 6;
}""",
        "unsubscribe_response": """message UnsubscribeResponse {
  // Unsubscribe success
  bool success = 1;

  // Error message if unsubscribe failed
  optional string error_message = 2;

  // Final offset position
  optional int64 final_offset = 3;
}""",
        "delete_queue_request": """message DeleteQueueRequest {
  // Queue ID or name to delete
  string queue = 1;

  // Force deletion even if not empty
  bool force = 2;

  // Purge messages before deletion
  bool purge_first = 3;
}""",
        "purge_request": """message PurgeRequest {
  // Queue or topic to purge
  string target = 1;

  // Purge messages older than timestamp
  optional int64 older_than = 2;

  // Purge specific partition (for topics)
  optional int32 partition = 3;

  // Maximum number of messages to purge
  optional int64 max_count = 4;
}""",
        "seek_request": """message SeekRequest {
  // Queue or topic to seek in
  string target = 1;

  // Consumer ID or subscription ID
  string consumer_id = 2;

  // Seek position
  oneof position {
    int64 offset = 3;        // Specific offset
    int64 timestamp = 4;     // Timestamp to seek to
    SeekType type = 5;       // Beginning or end
  }

  // Partition to seek (for topics)
  optional int32 partition = 6;
}

enum SeekType {
  SEEK_TYPE_UNSPECIFIED = 0;
  SEEK_TYPE_BEGINNING = 1;
  SEEK_TYPE_END = 2;
}""",
        "delete_request": """message DeleteRequest {
  // Target queue or topic
  string target = 1;

  // Message ID to delete
  string message_id = 2;

  // Alternative: delete by offset
  optional int64 offset = 3;

  // Alternative: delete by timestamp range
  optional int64 from_timestamp = 4;
  optional int64 to_timestamp = 5;
}""",
        "get_cluster_info_response": """message GetClusterInfoResponse {
  // Cluster information
  ClusterInfo cluster = 1;

  // Node information
  repeated NodeInfo nodes = 2;

  // Error message if failed to get info
  optional string error_message = 3;
}

message ClusterInfo {
  string cluster_id = 1;
  string version = 2;
  int32 node_count = 3;
  int32 topic_count = 4;
  int64 total_messages = 5;
  int64 total_size_bytes = 6;
  string leader_node = 7;
  ClusterState state = 8;
}

enum ClusterState {
  CLUSTER_STATE_UNSPECIFIED = 0;
  CLUSTER_STATE_HEALTHY = 1;
  CLUSTER_STATE_DEGRADED = 2;
  CLUSTER_STATE_OFFLINE = 3;
}

message NodeInfo {
  string node_id = 1;
  string address = 2;
  bool is_leader = 3;
  NodeState state = 4;
  int32 partition_count = 5;
  int64 disk_usage_bytes = 6;
  double cpu_usage_percent = 7;
  double memory_usage_percent = 8;
}

enum NodeState {
  NODE_STATE_UNSPECIFIED = 0;
  NODE_STATE_ONLINE = 1;
  NODE_STATE_OFFLINE = 2;
  NODE_STATE_SYNCING = 3;
}""",
        "export_queue_request": """message ExportQueueRequest {
  // Queue or topic to export
  string target = 1;

  // Export format
  enum ExportFormat {
    EXPORT_FORMAT_UNSPECIFIED = 0;
    EXPORT_FORMAT_JSON = 1;
    EXPORT_FORMAT_CSV = 2;
    EXPORT_FORMAT_AVRO = 3;
    EXPORT_FORMAT_PARQUET = 4;
  }
  ExportFormat format = 2;

  // Output destination
  string destination = 3;

  // Time range for export
  optional int64 from_timestamp = 4;
  optional int64 to_timestamp = 5;

  // Partition filter (for topics)
  repeated int32 partitions = 6;

  // Compression settings
  optional CompressionSettings compression = 7;

  // Include metadata
  bool include_metadata = 8;
}

message CompressionSettings {
  enum CompressionType {
    COMPRESSION_TYPE_UNSPECIFIED = 0;
    COMPRESSION_TYPE_NONE = 1;
    COMPRESSION_TYPE_GZIP = 2;
    COMPRESSION_TYPE_SNAPPY = 3;
    COMPRESSION_TYPE_LZ4 = 4;
  }
  CompressionType type = 1;
  int32 level = 2;  // Compression level
}""",
    }

    if filename in implementations:
        # Replace the skeleton content with actual implementation
        lines = content.split("\n")
        new_lines = []
        in_skeleton_section = False

        for line in lines:
            if "SKELETON_FILE" in line:
                in_skeleton_section = True
                continue
            elif line.strip().startswith("//") and "TODO" in line:
                continue
            elif line.strip() == "" and in_skeleton_section:
                continue
            else:
                new_lines.append(line)
                if "option features.(pb.go).api_level = API_OPAQUE;" in line:
                    # Add the implementation after the options
                    new_lines.append("")
                    new_lines.append(implementations[filename])
                    new_lines.append("")
                    in_skeleton_section = False

        return "\n".join(new_lines)

    return content


def implement_skeleton_file(file_path: str) -> bool:
    """Implement a single skeleton file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if "SKELETON_FILE" not in content:
            return False

        # Determine package and implement accordingly
        if "/auth/proto/" in file_path:
            new_content = implement_auth_skeleton(file_path, content)
        elif "/queue/proto/" in file_path:
            new_content = implement_queue_skeleton(file_path, content)
        else:
            print(f"⚠️  Unknown package for {file_path}, skipping")
            return False

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ Implemented {file_path}")
            return True
        else:
            print(f"⚠️  No implementation found for {file_path}")
            return False

    except Exception as e:
        print(f"❌ Error implementing {file_path}: {e}")
        return False


def main():
    """Main implementation function."""
    base_dir = "/Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg"

    print("🔍 Finding skeleton proto files...")

    # Get all proto files and filter for skeleton files
    proto_files = get_proto_files(base_dir)
    skeleton_files = [f for f in proto_files if is_skeleton_file(f)]

    print(f"📋 Found {len(skeleton_files)} skeleton files to implement")

    implemented_count = 0
    failed_count = 0

    for file_path in skeleton_files:
        if implement_skeleton_file(file_path):
            implemented_count += 1
        else:
            failed_count += 1

    print("\n📊 Implementation Summary:")
    print(f"   ✅ Successfully implemented: {implemented_count}")
    print(f"   ❌ Failed to implement: {failed_count}")
    print(f"   📁 Total skeleton files: {len(skeleton_files)}")

    if implemented_count > 0:
        print("\n🔧 Running buf generate to validate implementations...")
        import subprocess

        try:
            result = subprocess.run(
                ["buf", "generate"],
                cwd="/Users/jdfalk/repos/github.com/jdfalk/gcommon",
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                print("✅ buf generate successful - all proto files are valid!")
            else:
                print(f"❌ buf generate failed:\n{result.stderr}")
        except Exception as e:
            print(f"❌ Error running buf generate: {e}")


if __name__ == "__main__":
    main()
