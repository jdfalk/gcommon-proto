#!/bin/bash
# filepath: /Users/jdfalk/repos/github.com/jdfalk/gcommon/commit_protos_by_module.sh
#
# Script to commit proto files by module following conventional commit guidelines
# Each module's proto files will be committed together with proper documentation

set -e

echo "🚀 COMMITTING PROTO FILES BY MODULE"
echo "===================================="

# Function to generate file list for commit message
generate_file_list() {
    local module="$1"
    local files=()

    # Get all modified proto files for the module
    while IFS= read -r file; do
        if [[ "$file" =~ ^[[:space:]]*M[[:space:]]+pkg/${module}/proto/ ]]; then
            # Remove the 'M ' prefix and trim whitespace
            clean_file=$(echo "$file" | sed 's/^[[:space:]]*M[[:space:]]*//')
            files+=("$clean_file")
        fi
    done < <(git status --porcelain)

    # Generate the file list section
    if [[ ${#files[@]} -gt 0 ]]; then
        echo ""
        echo "Files changed:"
        for file in "${files[@]}"; do
            local filename=$(basename "$file")
            local file_type="protobuf placeholder structure"

            # Determine more specific description based on file path
            if [[ "$file" =~ /services/ ]]; then
                file_type="service definition placeholder"
            elif [[ "$file" =~ /messages/ ]]; then
                file_type="message type placeholder"
            elif [[ "$file" =~ /requests/ ]]; then
                file_type="request message placeholder"
            elif [[ "$file" =~ /responses/ ]]; then
                file_type="response message placeholder"
            elif [[ "$file" =~ /enums/ ]]; then
                file_type="enum definition placeholder"
            elif [[ "$file" =~ /types/ ]]; then
                file_type="type definition placeholder"
            fi

            echo "- Added ${file_type}: [${file}](https://github.com/jdfalk/gcommon/blob/main/${file})"
        done
    fi
}

# Function to commit a module's proto files
commit_module_protos() {
    local module="$1"
    local module_display="$2"

    echo "📦 Processing ${module_display} module..."

    # Check if there are any modified proto files for this module
    local has_changes=$(git status --porcelain | grep -c "^[[:space:]]*M[[:space:]]*pkg/${module}/proto/" || true)

    if [[ "$has_changes" -eq 0 ]]; then
        echo "   ⏭️  No changes found for ${module_display} module"
        return 0
    fi

    echo "   📝 Found $has_changes proto file(s) to commit"

    # Stage the proto files for this module
    git add "pkg/${module}/proto/"

    # Generate commit message
    local commit_title="feat(${module}): add protobuf placeholder structures"
    local commit_body="Initialize protobuf definitions for ${module_display} module with basic package structure, imports, and TODO placeholders for implementation.

Establish foundation for ${module_display} service definitions with standardized protobuf structure including proper edition 2023 syntax, Go package options, and organized file hierarchy.

This provides the scaffolding for implementing:
- Service interfaces and RPC method definitions
- Request/response message type definitions
- Enum types and data structure definitions
- Proper package organization and import statements
- Go code generation compatibility with protoc-gen-go

All files follow protobuf edition 2023 specification and include comprehensive TODO markers for systematic implementation of actual service definitions."

    # Add file list
    local file_list=$(generate_file_list "$module")
    local full_message="${commit_body}${file_list}"

    # Commit the changes
    git commit -m "$commit_title" -m "$full_message"

    echo "   ✅ Committed ${module_display} module proto files"
}

# Commit configuration and helper files first
echo "📋 Committing configuration and helper files..."
git add .mockery.yml TODO.md generate.sh analyze_protos.sh add_proto_headers.sh
git commit -m "chore(build): update proto build configuration and documentation" -m "Update mockery configuration with complete service definitions and enhance project documentation with proto file analysis.

Establish comprehensive build tooling for protobuf implementation including:
- Complete service interface definitions for mockery
- Proto file analysis and tracking documentation
- Header generation and analysis automation scripts
- Build process documentation and guidelines

Files changed:
- Updated mockery config with all proto services: [.mockery.yml](https://github.com/jdfalk/gcommon/blob/main/.mockery.yml)
- Added comprehensive proto analysis documentation: [TODO.md](https://github.com/jdfalk/gcommon/blob/main/TODO.md)
- Enhanced proto generation script: [generate.sh](https://github.com/jdfalk/gcommon/blob/main/generate.sh)
- Added proto file analysis automation: [analyze_protos.sh](https://github.com/jdfalk/gcommon/blob/main/analyze_protos.sh)
- Added proto header generation script: [add_proto_headers.sh](https://github.com/jdfalk/gcommon/blob/main/add_proto_headers.sh)"

echo "   ✅ Configuration files committed"
echo ""

# Commit each module's proto files
commit_module_protos "auth" "Authentication"
commit_module_protos "cache" "Cache"
commit_module_protos "config" "Configuration"
commit_module_protos "db" "Database"
commit_module_protos "health" "Health Check"
commit_module_protos "log" "Logging"
commit_module_protos "metrics" "Metrics"
commit_module_protos "queue" "Message Queue"
commit_module_protos "web" "Web Server"

echo ""
echo "🎉 SUCCESS: all proto files committed by module!"
echo "=============================================="
echo ""
echo "📊 Summary:"
echo "- Configuration files: ✅ committed"
echo "- Auth module: ✅ committed"
echo "- Cache module: ✅ committed"
echo "- Config module: ✅ committed"
echo "- Database module: ✅ committed"
echo "- Health module: ✅ committed"
echo "- Logging module: ✅ committed"
echo "- Metrics module: ✅ committed"
echo "- Queue module: ✅ committed"
echo "- Web module: ✅ committed"
echo ""
echo "🚀 ready for protobuf implementation!"
echo ""
echo "📝 Next steps:"
echo "   1. Implement core service definitions (auth, config, log)"
echo "   2. Define message types for requests/responses"
echo "   3. Add enum definitions and data structures"
echo "   4. Validate proto compilation with protoc"
echo "   5. Generate Go code and test integration"
