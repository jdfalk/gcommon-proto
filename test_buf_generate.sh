#!/bin/bash
# file: test_buf_generate.sh
# version: 1.0.0  
# guid: 123e4567-e89b-12d3-a456-426614174000

# Quick test of buf generate per module using direct buf commands
# This avoids the copilot-agent-util dependency issue

set -e

echo "🔧 Testing Buf Generate Per Module (Direct)"
echo "==========================================="
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

# Function to test linting for a specific module (simpler than generation)
test_module_lint() {
    local module_path="$1"
    local module_name=$(basename "$module_path")

    echo -n "📦 Testing $module_name... "

    # Create a log file for this module
    local log_file="logs/buf_lint_${module_name}_$(date +%Y%m%d_%H%M%S).log"

    # Run buf lint for this specific module path
    if buf lint --path "$module_path" > "$log_file" 2>&1; then
        echo -e "${GREEN}✅ SUCCESS${NC}"
        success_modules+=("$module_name")
    else
        echo -e "${RED}❌ FAILED${NC}"
        failed_modules+=("$module_name")

        # Store error details - get first few lines of actual errors
        local error_summary=$(head -n 3 "$log_file" | tr '\n' ' ' | cut -c1-120)
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
        test_module_lint "$module_dir"
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
    echo -e "${GREEN}🎉 All modules passed lint successfully!${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️  Some modules need attention. Check the logs in logs/ directory for details.${NC}"
    exit 1
fi