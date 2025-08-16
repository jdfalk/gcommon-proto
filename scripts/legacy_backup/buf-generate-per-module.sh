#!/bin/bash
# file: scripts/buf-generate-per-module.sh
# version: 1.0.0
# guid: 7f8e9d0a-1b2c-3d4e-5f6a-7b8c9d0e1f2a

# Generate protobuf files per module with detailed reporting
# This avoids the issue where buf generate stops at the first error

set -e

echo "🔧 Buf Generate Per Module"
echo "=========================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Arrays to track results
declare -a success_modules=()
declare -a failed_modules=()
declare -a error_details=()

# Create logs directory if it doesn't exist
mkdir -p logs

# Function to generate for a specific module
generate_module() {
    local module_path="$1"
    local module_name=$(basename "$module_path")

    echo -n "📦 Processing $module_name... "

    # Create a log file for this module
    local log_file="logs/buf_generate_${module_name}_$(date +%Y%m%d_%H%M%S).log"

    # Run copilot-agent-util buf generate for this specific module path
    if copilot-agent-util buf generate --path "$module_path" > "$log_file" 2>&1; then
        echo -e "${GREEN}✅ SUCCESS${NC}"
        success_modules+=("$module_name")
    else
        echo -e "${RED}❌ FAILED${NC}"
        failed_modules+=("$module_name")

                # Store error details - prefer actual error lines (non-timestamped), strip ANSI codes
                # 1) Strip ANSI
                # 2) Drop lines starting with an ISO timestamp (with or without prior ANSI codes)
                # 3) Take the first couple of meaningful lines
                local error_summary=$(awk '
                        BEGIN { ofs=" " }
                        {
                            line=$0
                            gsub(/\x1B\[[0-9;]*[mK]/, "", line)           # strip ANSI
                            if (line ~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}T/) next  # skip timestamped
                            if (line ~ /^[[:space:]]*$/) next                # skip blank
                            print line
                        }
                ' "$log_file" | head -n 3 | tr '\n' ' ' | cut -c1-180)
                if [ -z "$error_summary" ]; then
                        # Fallback: try common error keywords
                        error_summary=$(awk '{ line=$0; gsub(/\x1B\[[0-9;]*[mK]/, "", line); print line }' "$log_file" \
                                | grep -E "(Failure|failed|error|not exist|unknown)" | head -n 3 | tr '\n' ' ' | cut -c1-180)
                fi
        error_details+=("$module_name: $error_summary")

        echo -e "   ${YELLOW}Log: $log_file${NC}"
    fi
}

# Main execution
echo "🔍 Scanning pkg/ directory for modules..."
echo ""

# Find all directories in pkg/ that contain proto files
for module_dir in pkg/*/; do
    if [ -d "$module_dir" ] && find "$module_dir" -name "*.proto" -type f | grep -q .; then
        generate_module "$module_dir"
    fi
done

echo ""
echo "📊 SUMMARY REPORT"
echo "================="

# Success summary
if [ ${#success_modules[@]} -gt 0 ]; then
    echo -e "${GREEN}✅ SUCCESSFUL MODULES (${#success_modules[@]}):${NC}"
    for module in "${success_modules[@]}"; do
        echo -e "   ${GREEN}✓${NC} $module"
    done
    echo ""
fi

# Failure summary
if [ ${#failed_modules[@]} -gt 0 ]; then
    echo -e "${RED}❌ FAILED MODULES (${#failed_modules[@]}):${NC}"
    for module in "${failed_modules[@]}"; do
        echo -e "   ${RED}✗${NC} $module"
    done
    echo ""

    echo -e "${YELLOW}🔍 ERROR DETAILS:${NC}"
    for error in "${error_details[@]}"; do
        echo -e "   ${YELLOW}⚠️${NC} $error"
    done
    echo ""
fi

# Overall status
total_modules=$((${#success_modules[@]} + ${#failed_modules[@]}))
success_rate=$((${#success_modules[@]} * 100 / total_modules))

echo -e "${BLUE}📈 OVERALL STATUS:${NC}"
echo "   Total modules: $total_modules"
echo "   Successful: ${#success_modules[@]}"
echo "   Failed: ${#failed_modules[@]}"
echo "   Success rate: ${success_rate}%"
echo ""

if [ ${#failed_modules[@]} -eq 0 ]; then
    echo -e "${GREEN}🎉 All modules generated successfully!${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️  Some modules need attention. Check the logs in logs/ directory for details.${NC}"
    echo ""
    echo -e "${BLUE}💡 NEXT STEPS:${NC}"
    echo "   1. Review error logs for failed modules"
    echo "   2. Fix proto import issues or missing files"
    echo "   3. Re-run this script to verify fixes"
    echo "   4. Use 'buf lint --path pkg/MODULE_NAME/' to validate specific modules"
    exit 1
fi
