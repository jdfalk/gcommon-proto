#!/bin/bash
# filepath: /Users/jdfalk/repos/github.com/jdfalk/gcommon/create_github_issues.sh
#
# Script to create comprehensive GitHub issues and project for GCommon development
# Creates kanban-style tickets organized by module and work type

# Don't exit on error - we want to handle errors gracefully
set +e

echo "🚀 CREATING GITHUB ISSUES AND PROJECT FOR GCOMMON"
echo "=================================================="

# Counters for tracking
LABELS_CREATED=0
LABELS_SKIPPED=0
MILESTONES_CREATED=0
MILESTONES_SKIPPED=0
ISSUES_CREATED=0
ISSUES_SKIPPED=0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to check if issue already exists
issue_exists() {
    local title="$1"
    # Search for issues with the exact title (case-insensitive)
    local existing=$(gh issue list --search "\"$title\"" --state all --json title,number --jq ".[] | select(.title == \"$title\") | .number" 2>/dev/null)
    if [[ -n "$existing" ]]; then
        echo "$existing"
        return 0
    fi
    return 1
}

# Function to create issue and return issue number
create_issue() {
    local title="$1"
    local body="$2"
    local labels="$3"
    local milestone="$4"

    # Check if issue already exists
    if existing_issue=$(issue_exists "$title"); then
        echo -e "${YELLOW}⏭️  Issue already exists: #$existing_issue - $title${NC}"
        ((ISSUES_SKIPPED++))
        echo "$existing_issue"
        return 0
    fi

    echo -e "${BLUE}Creating issue: $title${NC}"

    # Use arrays for better argument handling
    local issue_args=("gh" "issue" "create" "--title" "$title" "--body" "$body")

    # Add labels if provided, but validate they exist first
    if [[ -n "$labels" ]]; then
        # Split labels by comma and validate each one exists
        IFS=',' read -ra LABEL_ARRAY <<< "$labels"
        local valid_labels=()
        for label in "${LABEL_ARRAY[@]}"; do
            label=$(echo "$label" | xargs) # trim whitespace
            if gh label list --json name --jq ".[].name" | grep -q "^$label$" 2>/dev/null; then
                valid_labels+=("$label")
            else
                echo -e "${YELLOW}⚠️  Label '$label' doesn't exist, skipping${NC}"
            fi
        done

        # Add valid labels to command
        if [[ ${#valid_labels[@]} -gt 0 ]]; then
            for label in "${valid_labels[@]}"; do
                issue_args+=("--label" "$label")
            done
        fi
    fi

    # Add milestone if provided and exists
    if [[ -n "$milestone" ]]; then
        # Check if milestone exists using API
        local milestone_exists=$(gh api repos/:owner/:repo/milestones --jq ".[] | select(.title == \"$milestone\") | .number" 2>/dev/null)
        if [[ -n "$milestone_exists" ]]; then
            issue_args+=("--milestone" "$milestone")
        else
            echo -e "${YELLOW}⚠️  Milestone '$milestone' doesn't exist, creating issue without milestone${NC}"
        fi
    fi

    echo -e "${BLUE}Running: ${issue_args[*]}${NC}"

    # Execute the command and capture the issue URL
    if issue_url=$("${issue_args[@]}" 2>&1); then
        local issue_number=$(echo "$issue_url" | grep -o '[0-9]\+$')
        if [[ -n "$issue_number" ]]; then
            echo -e "${GREEN}✅ Created issue #$issue_number${NC}"
            ((ISSUES_CREATED++))
            echo "$issue_number"
        else
            echo -e "${RED}❌ Unexpected response: $issue_url${NC}"
            return 1
        fi
    else
        echo -e "${RED}❌ Failed to create issue: $title${NC}"
        echo -e "${RED}Error: $issue_url${NC}"
        # Check if it exists now (maybe race condition)
        if existing_issue=$(issue_exists "$title"); then
            echo -e "${YELLOW}⏭️  Issue now exists: #$existing_issue - $title${NC}"
            ((ISSUES_SKIPPED++))
            echo "$existing_issue"
            return 0
        fi
        return 1
    fi
}

# Function to create label if it doesn't exist
create_label() {
    local name="$1"
    local description="$2"
    local color="$3"

    echo -e "${BLUE}Processing label: $name${NC}"

    # Always try to create/update the label with --force to handle color/description updates
    local cmd="gh label create \"$name\" --description \"$description\" --force"
    if [[ -n "$color" ]]; then
        cmd="$cmd --color \"$color\""
    fi

    echo -e "${BLUE}Running command: $cmd${NC}"

    # Try to create/update the label
    if eval $cmd 2>&1; then
        echo -e "${GREEN}✅ Created/updated label: $name${NC}"
        ((LABELS_CREATED++))
    else
        local exit_code=$?
        echo -e "${RED}❌ Command failed with exit code: $exit_code${NC}"
        # If creation failed, check if it exists and count as skipped
        if gh label list --json name --jq ".[].name" | grep -q "^$name$" 2>/dev/null; then
            echo -e "${YELLOW}⏭️  Label exists but couldn't update: $name${NC}"
            ((LABELS_SKIPPED++))
        else
            echo -e "${RED}❌ Failed to create label: $name${NC}"
            return 1
        fi
    fi

    echo -e "${BLUE}Finished processing label: $name${NC}"
}

# Function to create milestone if it doesn't exist (using GitHub API)
create_milestone() {
    local title="$1"
    local description="$2"
    local due_date="$3"

    echo -e "${BLUE}Processing milestone: $title${NC}"

    # Check if milestone already exists using API
    local existing=$(gh api repos/:owner/:repo/milestones --jq ".[] | select(.title == \"$title\") | .number" 2>/dev/null)
    if [[ -n "$existing" ]]; then
        echo -e "${YELLOW}⏭️  Milestone already exists: $title${NC}"
        ((MILESTONES_SKIPPED++))
        return 0
    fi

    # Create milestone using GitHub API
    local milestone_data=$(printf '{"title": "%s", "description": "%s", "due_on": "%sT23:59:59Z"}' "$title" "$description" "$due_date")

    if gh api repos/:owner/:repo/milestones -X POST --input - <<< "$milestone_data" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Created milestone: $title${NC}"
        ((MILESTONES_CREATED++))
    else
        echo -e "${RED}❌ Failed to create milestone: $title${NC}"
        ((MILESTONES_SKIPPED++))
    fi
}

# Function to create project (DISABLED - projects already exist)
create_project() {
    echo -e "${YELLOW}Skipping project creation - projects already exist${NC}"

    # List existing projects
    echo -e "${BLUE}Existing projects:${NC}"
    gh project list

    echo -e "${GREEN}✅ Using existing project${NC}"
}

# Create all necessary labels first
echo -e "${YELLOW}Creating labels...${NC}"

# Module labels (blue theme)
create_label "module:auth" "Authentication module" "0052CC"
create_label "module:cache" "Cache module" "0052CC"
create_label "module:config" "Configuration module" "0052CC"
create_label "module:database" "Database module" "0052CC"
create_label "module:health" "Health module" "0052CC"
create_label "module:logging" "Logging module" "0052CC"
create_label "module:metrics" "Metrics module" "0052CC"
create_label "module:queue" "Queue module" "0052CC"
create_label "module:web" "Web module" "0052CC"

# Type labels (purple theme)
create_label "type:protobuf" "Protobuf definitions" "7057FF"
create_label "type:grpc" "gRPC service implementation" "7057FF"
create_label "type:provider" "Backend provider implementation" "7057FF"
create_label "type:testing" "Testing and quality assurance" "7057FF"
create_label "type:docs" "Documentation" "7057FF"
create_label "type:example" "Example code" "7057FF"
create_label "type:infrastructure" "CI/CD and tooling" "7057FF"
create_label "type:performance" "Performance optimization" "7057FF"

# Priority labels (traffic light theme)
create_label "priority:high" "High priority" "D73A49"
create_label "priority:medium" "Medium priority" "FFC107"
create_label "priority:low" "Low priority" "28A745"

# Status labels (gray theme)
create_label "status:blocked" "Blocked by dependencies" "6C757D"

# Special labels
create_label "good-first-issue" "Good for newcomers" "7057FF"

# Size labels (green theme)
create_label "size:small" "1-2 days work" "C5F467"
create_label "size:medium" "3-5 days work" "7CB342"
create_label "size:large" "1+ weeks work" "388E3C"

echo -e "${GREEN}✅ All labels created${NC}"

# Create milestones
echo -e "${YELLOW}Creating milestones...${NC}"

create_milestone "v0.2.0" "Phase 1 - Foundation Completion" "2025-07-15"
create_milestone "v0.3.0" "Phase 2 - Core Services" "2025-09-30"
create_milestone "v0.4.0" "Phase 3 - Advanced Services" "2025-12-15"
create_milestone "v1.0.0" "Phase 4 - Production Ready" "2026-03-31"

echo -e "${GREEN}✅ All milestones created${NC}"

# Now create issues organized by module and type

echo -e "${YELLOW}Creating Foundation & Infrastructure issues...${NC}"

# Foundation Issues
create_issue "Complete protobuf compilation validation across all modules" \
"## Objective
Ensure all protobuf files compile successfully across all 9 modules.

## Tasks
- [ ] Run protobuf compilation tests on all modules
- [ ] Fix any remaining import path issues
- [ ] Validate all proto syntax is correct
- [ ] Document compilation process

## Acceptance Criteria
- All proto files compile without errors
- Compilation test script passes 100%
- Documentation updated with compilation instructions

## Dependencies
None - this is foundational work" \
"type:protobuf,priority:high,size:small" \
"v0.2.0"

create_issue "Set up comprehensive CI/CD pipeline" \
"## Objective
Establish automated testing, building, and deployment pipeline.

## Tasks
- [ ] Set up GitHub Actions workflows
- [ ] Add automated testing on multiple Go versions
- [ ] Add protobuf compilation validation
- [ ] Add code coverage reporting
- [ ] Add security scanning
- [ ] Set up automated releases

## Acceptance Criteria
- All PRs automatically tested
- Code coverage reporting enabled
- Security scanning integrated
- Automated release process documented

## Dependencies
None" \
"type:infrastructure,priority:high,size:medium" \
"v0.2.0"

create_issue "Create comprehensive project documentation structure" \
"## Objective
Establish clear, comprehensive documentation for users and contributors.

## Tasks
- [ ] Standardize documentation format across modules
- [ ] Create contributor guidelines
- [ ] Add API reference documentation
- [ ] Create troubleshooting guides
- [ ] Add architectural decision records

## Acceptance Criteria
- Consistent documentation format
- Complete API documentation
- Clear contributor onboarding
- Troubleshooting guides available

## Dependencies
None" \
"type:docs,priority:medium,size:medium" \
"v0.2.0"

echo -e "${YELLOW}Creating Metrics Module issues (70% → 100%)...${NC}"

create_issue "Complete OpenTelemetry integration for metrics module" \
"## Objective
Finish OpenTelemetry integration to reach 100% metrics module completion.

## Tasks
- [ ] Complete OpenTelemetry provider implementation
- [ ] Add OTLP exporter support
- [ ] Implement trace correlation with metrics
- [ ] Add OpenTelemetry configuration options
- [ ] Update examples to show OpenTelemetry usage

## Acceptance Criteria
- OpenTelemetry provider fully functional
- OTLP export working
- Examples demonstrate integration
- Tests cover all functionality

## Dependencies
None" \
"module:metrics,type:provider,priority:high,size:medium" \
"v0.2.0"

create_issue "Complete metrics module gRPC service implementation" \
"## Objective
Finish gRPC service implementation for metrics module.

## Tasks
- [ ] Complete remaining gRPC service methods
- [ ] Add streaming metrics support
- [ ] Implement metrics aggregation service
- [ ] Add metrics query service
- [ ] Update service documentation

## Acceptance Criteria
- All gRPC methods implemented
- Streaming functionality working
- Service tests passing
- Documentation complete

## Dependencies
- Protobuf compilation validation" \
"module:metrics,type:grpc,priority:high,size:medium" \
"v0.2.0"

create_issue "Add metrics module performance benchmarks" \
"## Objective
Establish performance benchmarks for metrics collection and reporting.

## Tasks
- [ ] Create benchmark tests for metric collection
- [ ] Benchmark different backend providers
- [ ] Add memory usage profiling
- [ ] Create performance comparison documentation
- [ ] Set performance regression detection

## Acceptance Criteria
- Comprehensive benchmark suite
- Performance baseline established
- Regression detection automated
- Performance documentation complete

## Dependencies
- Metrics module completion" \
"module:metrics,type:performance,priority:medium,size:small" \
"v0.2.0"

echo -e "${YELLOW}Creating Logging Module issues (50% → 100%)...${NC}"

create_issue "Complete logging module gRPC service implementation" \
"## Objective
Implement complete gRPC services for distributed logging.

## Tasks
- [ ] Implement LogService gRPC methods
- [ ] Implement LogManagementService gRPC methods
- [ ] Add log streaming functionality
- [ ] Implement log aggregation service
- [ ] Add log query and filtering service

## Acceptance Criteria
- All gRPC service methods implemented
- Log streaming working with backpressure handling
- Aggregation service functional
- Query service with filtering capabilities
- All services have comprehensive tests

## Dependencies
- Protobuf compilation validation" \
"module:logging,type:grpc,priority:high,size:large" \
"v0.3.0"

create_issue "Implement structured logging with correlation IDs" \
"## Objective
Add advanced structured logging capabilities with request correlation.

## Tasks
- [ ] Implement correlation ID propagation
- [ ] Add structured field validation
- [ ] Implement log context management
- [ ] Add sampling support for high-volume logging
- [ ] Create log enrichment pipeline

## Acceptance Criteria
- Correlation IDs automatically propagated
- Structured fields validated and consistent
- Context properly managed across goroutines
- Sampling reduces log volume intelligently
- Enrichment pipeline configurable

## Dependencies
- Logging gRPC services" \
"module:logging,type:provider,priority:high,size:medium" \
"v0.3.0"

create_issue "Add logging module provider implementations" \
"## Objective
Complete backend provider implementations for different logging systems.

## Tasks
- [ ] Complete Zap provider implementation
- [ ] Complete Logrus provider implementation
- [ ] Add syslog provider
- [ ] Add file rotation provider
- [ ] Add remote logging provider (e.g., Elasticsearch)

## Acceptance Criteria
- All providers fully functional
- Provider switching without code changes
- Configuration-driven provider selection
- Performance optimized for each provider
- Tests for all providers

## Dependencies
- Logging interfaces finalized" \
"module:logging,type:provider,priority:medium,size:large" \
"v0.3.0"

create_issue "Create comprehensive logging examples" \
"## Objective
Provide clear examples for all logging use cases.

## Tasks
- [ ] Basic logging example
- [ ] Structured logging example
- [ ] Distributed logging example
- [ ] Log aggregation example
- [ ] Custom provider example

## Acceptance Criteria
- Examples cover all major use cases
- Examples are well-documented
- Examples include best practices
- Examples demonstrate integration patterns
- Examples are tested and working

## Dependencies
- Logging module completion" \
"module:logging,type:example,priority:medium,size:medium" \
"v0.3.0"

echo -e "${YELLOW}Creating Auth Module issues (45% → 100%)...${NC}"

create_issue "Complete authentication service implementation" \
"## Objective
Implement remaining AuthService methods and complete service functionality.

## Tasks
- [ ] Implement RefreshToken method
- [ ] Implement RevokeToken method
- [ ] Implement GetUserInfo method
- [ ] Add multi-factor authentication support
- [ ] Implement token introspection

## Acceptance Criteria
- All AuthService methods implemented
- MFA flow working end-to-end
- Token lifecycle fully managed
- User information retrieval working
- Comprehensive test coverage

## Dependencies
- Protobuf compilation validation" \
"module:auth,type:grpc,priority:high,size:large" \
"v0.3.0"

create_issue "Implement authorization service with RBAC" \
"## Objective
Complete AuthorizationService with role-based access control.

## Tasks
- [ ] Implement CheckPermission method
- [ ] Implement role management methods
- [ ] Add permission inheritance
- [ ] Implement resource-based permissions
- [ ] Add authorization policies

## Acceptance Criteria
- RBAC fully functional
- Permission checking optimized
- Role hierarchy supported
- Resource permissions working
- Policy engine implemented

## Dependencies
- Auth service implementation" \
"module:auth,type:grpc,priority:high,size:large" \
"v0.3.0"

create_issue "Implement session management service" \
"## Objective
Complete SessionService with full session lifecycle management.

## Tasks
- [ ] Complete session creation and validation
- [ ] Implement session expiration and renewal
- [ ] Add concurrent session management
- [ ] Implement session invalidation
- [ ] Add session activity tracking

## Acceptance Criteria
- Session lifecycle fully managed
- Concurrent sessions handled properly
- Activity tracking working
- Session security enforced
- Performance optimized

## Dependencies
- Auth service implementation" \
"module:auth,type:grpc,priority:medium,size:medium" \
"v0.3.0"

create_issue "Add authentication provider implementations" \
"## Objective
Implement various authentication backends and providers.

## Tasks
- [ ] OAuth2/OIDC provider
- [ ] LDAP provider
- [ ] Database-backed provider
- [ ] JWT provider
- [ ] API key provider

## Acceptance Criteria
- All providers fully functional
- Provider configuration standardized
- Provider switching supported
- Security best practices followed
- Comprehensive testing

## Dependencies
- Auth service completion" \
"module:auth,type:provider,priority:medium,size:large" \
"v0.3.0"

create_issue "Create comprehensive auth examples and documentation" \
"## Objective
Provide complete examples and documentation for authentication module.

## Tasks
- [ ] Basic authentication example
- [ ] OAuth2 integration example
- [ ] RBAC implementation example
- [ ] Multi-factor authentication example
- [ ] Complete API documentation

## Acceptance Criteria
- Examples cover all auth patterns
- Documentation is comprehensive
- Security guidelines included
- Best practices documented
- Integration guides available

## Dependencies
- Auth module completion" \
"module:auth,type:docs,priority:medium,size:medium" \
"v0.3.0"

echo -e "${YELLOW}Creating Database Module issues (30% → 100%)...${NC}"

create_issue "Complete database service protobuf definitions" \
"## Objective
Finish all protobuf message types for database operations.

## Tasks
- [ ] Complete DatabaseService request/response messages
- [ ] Complete TransactionService messages
- [ ] Complete SchemaService messages
- [ ] Complete MigrationService messages
- [ ] Add batch operation messages

## Acceptance Criteria
- All service messages defined
- Message validation implemented
- Cross-service consistency maintained
- Documentation complete
- Protobuf compilation successful

## Dependencies
- Protobuf compilation validation" \
"module:database,type:protobuf,priority:high,size:medium" \
"v0.2.0"

create_issue "Implement complete DatabaseService gRPC implementation" \
"## Objective
Implement all DatabaseService methods for core database operations.

## Tasks
- [ ] Implement Query and Execute methods
- [ ] Add batch operation support
- [ ] Implement connection pooling
- [ ] Add query optimization
- [ ] Implement result streaming

## Acceptance Criteria
- All database operations working
- Batch operations optimized
- Connection pooling efficient
- Query performance optimized
- Streaming results working

## Dependencies
- Database protobuf completion" \
"module:database,type:grpc,priority:high,size:large" \
"v0.3.0"

create_issue "Implement transaction service with distributed support" \
"## Objective
Complete transaction management with distributed transaction support.

## Tasks
- [ ] Implement transaction lifecycle management
- [ ] Add distributed transaction support
- [ ] Implement savepoint management
- [ ] Add transaction isolation levels
- [ ] Implement deadlock detection

## Acceptance Criteria
- ACID transactions working
- Distributed transactions supported
- Savepoints functional
- Isolation levels configurable
- Deadlock handling implemented

## Dependencies
- Database service implementation" \
"module:database,type:grpc,priority:high,size:large" \
"v0.3.0"

create_issue "Complete database provider implementations" \
"## Objective
Finish implementations for all supported database backends.

## Tasks
- [ ] Complete PostgreSQL provider
- [ ] Complete CockroachDB provider
- [ ] Complete Pebble provider
- [ ] Enhance SQLite provider
- [ ] Add provider-specific optimizations

## Acceptance Criteria
- All providers fully functional
- Provider-specific features available
- Performance optimized per backend
- Feature parity across providers
- Comprehensive testing

## Dependencies
- Database service completion" \
"module:database,type:provider,priority:medium,size:large" \
"v0.3.0"

create_issue "Implement schema management and migrations" \
"## Objective
Complete schema management with automatic migrations.

## Tasks
- [ ] Implement schema versioning
- [ ] Add automatic migration generation
- [ ] Implement rollback functionality
- [ ] Add schema validation
- [ ] Create migration testing tools

## Acceptance Criteria
- Schema versions tracked automatically
- Migrations generated from schema changes
- Rollbacks working reliably
- Schema validation comprehensive
- Migration testing automated

## Dependencies
- Database service completion" \
"module:database,type:grpc,priority:medium,size:large" \
"v0.3.0"

echo -e "${YELLOW}Creating Cache Module issues (20% → 100%)...${NC}"

create_issue "Implement complete cache service gRPC methods" \
"## Objective
Implement all CacheService and CacheManagementService methods.

## Tasks
- [ ] Implement basic cache operations (Get, Set, Delete)
- [ ] Add batch operations support
- [ ] Implement TTL management
- [ ] Add cache statistics and monitoring
- [ ] Implement cache invalidation patterns

## Acceptance Criteria
- All cache operations working
- Batch operations optimized
- TTL properly managed
- Statistics collection working
- Invalidation patterns implemented

## Dependencies
- Protobuf compilation validation" \
"module:cache,type:grpc,priority:high,size:large" \
"v0.3.0"

create_issue "Add cache provider implementations" \
"## Objective
Implement various cache backend providers.

## Tasks
- [ ] Complete Redis provider
- [ ] Complete Memcached provider
- [ ] Enhance in-memory provider
- [ ] Add distributed cache provider
- [ ] Implement cache clustering

## Acceptance Criteria
- All providers fully functional
- Provider selection configurable
- Distributed caching working
- Clustering implemented
- Performance optimized

## Dependencies
- Cache service implementation" \
"module:cache,type:provider,priority:medium,size:large" \
"v0.3.0"

create_issue "Implement advanced cache features" \
"## Objective
Add advanced caching capabilities like cache warming and compression.

## Tasks
- [ ] Implement cache warming strategies
- [ ] Add data compression support
- [ ] Implement cache partitioning
- [ ] Add cache replication
- [ ] Implement smart eviction policies

## Acceptance Criteria
- Cache warming automated
- Compression reduces memory usage
- Partitioning working efficiently
- Replication maintains consistency
- Eviction policies optimized

## Dependencies
- Cache provider completion" \
"module:cache,type:provider,priority:medium,size:medium" \
"v0.4.0"

echo -e "${YELLOW}Creating Config Module issues (20% → 100%)...${NC}"

create_issue "Implement configuration service interfaces" \
"## Objective
Create Go interfaces for configuration management.

## Tasks
- [ ] Design configuration provider interface
- [ ] Create configuration watcher interface
- [ ] Design validation interface
- [ ] Create encryption interface
- [ ] Design configuration schema interface

## Acceptance Criteria
- Interfaces support all use cases
- Provider swapping possible
- Hot reload supported
- Validation framework integrated
- Encryption/decryption supported

## Dependencies
None" \
"module:config,type:protobuf,priority:high,size:medium" \
"v0.2.0"

create_issue "Implement configuration gRPC services" \
"## Objective
Complete ConfigService and ConfigSchemaService implementations.

## Tasks
- [ ] Implement configuration CRUD operations
- [ ] Add configuration watching with real-time updates
- [ ] Implement configuration validation
- [ ] Add configuration versioning
- [ ] Implement configuration templates

## Acceptance Criteria
- All config operations working
- Real-time updates functional
- Validation prevents invalid configs
- Versioning tracks changes
- Templates reduce duplication

## Dependencies
- Config protobuf completion" \
"module:config,type:grpc,priority:high,size:large" \
"v0.3.0"

create_issue "Add configuration provider implementations" \
"## Objective
Implement various configuration source providers.

## Tasks
- [ ] File-based provider (JSON, YAML, TOML)
- [ ] Environment variable provider
- [ ] Remote configuration provider (etcd, Consul)
- [ ] Database configuration provider
- [ ] Kubernetes ConfigMap provider

## Acceptance Criteria
- All providers functional
- Provider composition supported
- Hot reload working for all sources
- Provider priorities configurable
- Fallback mechanisms implemented

## Dependencies
- Config service implementation" \
"module:config,type:provider,priority:medium,size:large" \
"v0.3.0"

create_issue "Implement configuration hot reload and validation" \
"## Objective
Add advanced configuration management features.

## Tasks
- [ ] Implement hot reload without service restart
- [ ] Add schema-based validation
- [ ] Implement configuration encryption
- [ ] Add configuration audit logging
- [ ] Create configuration diff tools

## Acceptance Criteria
- Hot reload works seamlessly
- Schema validation comprehensive
- Sensitive data encrypted
- All changes audited
- Diff tools help troubleshooting

## Dependencies
- Config provider completion" \
"module:config,type:provider,priority:medium,size:medium" \
"v0.4.0"

echo -e "${YELLOW}Creating Queue Module issues (10% → 100%)...${NC}"

create_issue "Implement queue service Go interfaces" \
"## Objective
Create comprehensive Go interfaces for message queue operations.

## Tasks
- [ ] Design message producer interface
- [ ] Create message consumer interface
- [ ] Design queue management interface
- [ ] Create batch processing interface
- [ ] Design dead letter queue interface

## Acceptance Criteria
- Interfaces support all messaging patterns
- Producer/consumer decoupled properly
- Management operations comprehensive
- Batch processing efficient
- Dead letter handling robust

## Dependencies
None" \
"module:queue,type:protobuf,priority:high,size:medium" \
"v0.2.0"

create_issue "Implement queue gRPC services" \
"## Objective
Complete QueueService and QueueManagementService implementations.

## Tasks
- [ ] Implement message publishing methods
- [ ] Implement message consumption methods
- [ ] Add queue management operations
- [ ] Implement workflow orchestration
- [ ] Add batch processing support

## Acceptance Criteria
- All queue operations working
- Message delivery guaranteed
- Queue management comprehensive
- Workflows orchestrated properly
- Batch processing optimized

## Dependencies
- Queue protobuf completion" \
"module:queue,type:grpc,priority:high,size:large" \
"v0.4.0"

create_issue "Add message queue provider implementations" \
"## Objective
Implement various message queue backend providers.

## Tasks
- [ ] RabbitMQ provider implementation
- [ ] NATS provider implementation
- [ ] AWS SQS provider implementation
- [ ] Apache Kafka provider implementation
- [ ] In-memory provider for testing

## Acceptance Criteria
- All providers fully functional
- Provider features properly exposed
- Performance optimized per backend
- Provider switching configurable
- Test provider available

## Dependencies
- Queue service implementation" \
"module:queue,type:provider,priority:medium,size:large" \
"v0.4.0"

create_issue "Implement advanced queue features" \
"## Objective
Add advanced messaging capabilities.

## Tasks
- [ ] Implement message routing and filtering
- [ ] Add retry logic with exponential backoff
- [ ] Implement dead letter queue handling
- [ ] Add message deduplication
- [ ] Implement priority queues

## Acceptance Criteria
- Routing works with complex patterns
- Retry logic prevents message loss
- Dead letters handled appropriately
- Deduplication prevents duplicates
- Priority queues functional

## Dependencies
- Queue provider completion" \
"module:queue,type:provider,priority:medium,size:medium" \
"v0.4.0"

echo -e "${YELLOW}Creating Web Module issues (10% → 100%)...${NC}"

create_issue "Implement web service Go interfaces" \
"## Objective
Create comprehensive interfaces for web server functionality.

## Tasks
- [ ] Design HTTP server interface
- [ ] Create middleware interface
- [ ] Design WebSocket interface
- [ ] Create routing interface
- [ ] Design static file serving interface

## Acceptance Criteria
- Interfaces support all web patterns
- Middleware chain composable
- WebSocket bi-directional communication
- Routing flexible and fast
- Static serving optimized

## Dependencies
None" \
"module:web,type:protobuf,priority:high,size:medium" \
"v0.2.0"

create_issue "Implement web gRPC services" \
"## Objective
Complete WebService, MiddlewareService, and WebSocketService.

## Tasks
- [ ] Implement HTTP request/response handling
- [ ] Implement middleware management
- [ ] Add WebSocket connection management
- [ ] Implement routing configuration
- [ ] Add static file serving

## Acceptance Criteria
- HTTP handling efficient and secure
- Middleware easily configurable
- WebSocket connections managed properly
- Routing performance optimized
- Static files served efficiently

## Dependencies
- Web protobuf completion" \
"module:web,type:grpc,priority:high,size:large" \
"v0.4.0"

create_issue "Add web server provider implementations" \
"## Objective
Implement various web server backend providers.

## Tasks
- [ ] Standard library HTTP provider
- [ ] Gin framework provider
- [ ] Echo framework provider
- [ ] Fiber framework provider
- [ ] gRPC-Gateway integration

## Acceptance Criteria
- All providers fully functional
- Framework features properly exposed
- Performance comparison documented
- Provider switching supported
- gRPC-Gateway working

## Dependencies
- Web service implementation" \
"module:web,type:provider,priority:medium,size:large" \
"v0.4.0"

create_issue "Implement advanced web features" \
"## Objective
Add advanced web server capabilities.

## Tasks
- [ ] Implement request/response compression
- [ ] Add security headers management
- [ ] Implement rate limiting
- [ ] Add request tracing integration
- [ ] Implement graceful shutdown

## Acceptance Criteria
- Compression reduces bandwidth
- Security headers properly configured
- Rate limiting prevents abuse
- Tracing provides observability
- Shutdown doesn't drop connections

## Dependencies
- Web provider completion" \
"module:web,type:provider,priority:medium,size:medium" \
"v0.4.0"

echo -e "${YELLOW}Creating Cross-Module Integration issues...${NC}"

create_issue "Implement service discovery and registration" \
"## Objective
Add service discovery capabilities across all modules.

## Tasks
- [ ] Design service registry interface
- [ ] Implement service registration
- [ ] Add health check integration
- [ ] Implement load balancing
- [ ] Add service mesh compatibility

## Acceptance Criteria
- Services automatically discovered
- Health checks integrated
- Load balancing working
- Service mesh compatible
- Registration reliable

## Dependencies
- Health module completion" \
"type:infrastructure,priority:medium,size:large" \
"v0.4.0"

create_issue "Create comprehensive integration examples" \
"## Objective
Provide examples showing modules working together.

## Tasks
- [ ] Multi-module application example
- [ ] Microservices architecture example
- [ ] Observability integration example
- [ ] Security integration example
- [ ] Performance optimization example

## Acceptance Criteria
- Examples show real-world usage
- Architecture patterns demonstrated
- Best practices documented
- Performance considerations shown
- Security properly implemented

## Dependencies
- Multiple modules completion" \
"type:example,priority:medium,size:large" \
"v1.0.0"

create_issue "Implement comprehensive observability" \
"## Objective
Ensure all modules provide proper observability.

## Tasks
- [ ] Standardize metrics across modules
- [ ] Implement distributed tracing
- [ ] Add structured logging integration
- [ ] Create observability dashboards
- [ ] Add alerting rules

## Acceptance Criteria
- Metrics consistent across modules
- Tracing shows request flows
- Logs properly correlated
- Dashboards provide insights
- Alerts catch issues early

## Dependencies
- Metrics, logging completion" \
"type:infrastructure,priority:medium,size:large" \
"v1.0.0"

echo -e "${YELLOW}Creating Performance and Quality issues...${NC}"

create_issue "Establish performance benchmarks for all modules" \
"## Objective
Create comprehensive performance benchmarking suite.

## Tasks
- [ ] Create benchmark tests for each module
- [ ] Establish performance baselines
- [ ] Add memory usage profiling
- [ ] Implement performance regression testing
- [ ] Create performance comparison reports

## Acceptance Criteria
- Benchmarks cover all critical paths
- Baselines documented
- Memory profiling automated
- Regression detection working
- Comparison reports generated

## Dependencies
- All modules functional" \
"type:performance,priority:medium,size:large" \
"v1.0.0"

create_issue "Implement comprehensive security audit" \
"## Objective
Conduct thorough security review and testing.

## Tasks
- [ ] Perform static code analysis
- [ ] Conduct dependency vulnerability scanning
- [ ] Implement security best practices
- [ ] Add security testing automation
- [ ] Create security documentation

## Acceptance Criteria
- Code analysis clean
- No vulnerable dependencies
- Best practices followed
- Security tests automated
- Security guide complete

## Dependencies
- All modules functional" \
"type:infrastructure,priority:high,size:medium" \
"v1.0.0"

create_issue "Create production deployment guides" \
"## Objective
Provide comprehensive production deployment documentation.

## Tasks
- [ ] Create Kubernetes deployment guides
- [ ] Add Docker configuration examples
- [ ] Document scaling strategies
- [ ] Create monitoring setup guides
- [ ] Add troubleshooting documentation

## Acceptance Criteria
- Deployment guides comprehensive
- Examples working and tested
- Scaling strategies documented
- Monitoring properly configured
- Troubleshooting covers common issues

## Dependencies
- All modules production ready" \
"type:docs,priority:medium,size:medium" \
"v1.0.0"

# Project setup complete - using existing projects
echo -e "${YELLOW}Using existing GitHub projects...${NC}"

echo -e "${GREEN}✅ Project setup complete${NC}"

echo ""
echo -e "${GREEN}🎉 SUCCESS: GitHub issues and project setup completed!${NC}"
echo "=============================================="
echo ""
echo -e "${BLUE}📊 Summary:${NC}"
echo "Labels: $LABELS_CREATED created, $LABELS_SKIPPED already existed"
echo "Milestones: $MILESTONES_CREATED created, $MILESTONES_SKIPPED already existed"
echo "Issues: $ISSUES_CREATED created, $ISSUES_SKIPPED already existed"
echo ""
echo -e "${BLUE}🚀 Next Steps:${NC}"
echo "1. Visit the GitHub project to organize issues into columns"
echo "2. Assign team members to specific issues"
echo "3. Set up project automation rules"
echo "4. Begin work on high-priority foundation issues"
echo ""
echo -e "${BLUE}🔗 Quick Links:${NC}"
echo "- Project: https://github.com/jdfalk/gcommon/projects"
echo "- Issues: https://github.com/jdfalk/gcommon/issues"
echo "- Milestones: https://github.com/jdfalk/gcommon/milestones"
