#!/bin/bash
# file: verify_1_1_1_completion.sh
# Enhanced verification script for 1-1-1 protobuf structure with accurate counts

set -e

BASE_DIR="/Users/jdfalk/repos/github.com/jdfalk/gcommon/pkg"
MODULES=("auth" "cache" "config" "db" "health" "log" "metrics" "queue" "web" "common")

# Function to get expected count for a module
get_expected_count() {
    case $1 in
        "auth") echo 16 ;;
        "cache") echo 7 ;;
        "common") echo 39 ;;
        "config") echo 2 ;;
        "db") echo 52 ;;
        "health") echo 1 ;;
        "log") echo 0 ;;      # Log module uses existing interfaces, no proto split needed
        "metrics") echo 1 ;;
        "queue") echo 1 ;;
        "web") echo 1 ;;
        *) echo 0 ;;
    esac
}

# Total expected across all modules
TOTAL_EXPECTED=120

echo "🔍 Verifying 1-1-1 Protobuf Structure Completion"
echo "================================================"

# Function to count proto files excluding monolithic files
count_1_1_1_files() {
    local module=$1
    local base_path="$BASE_DIR/$module/proto"

    if [[ ! -d "$base_path" ]]; then
        echo "0"
        return
    fi

    # Count all .proto files except the monolithic ones
    find "$base_path" -name "*.proto" -type f | \
    grep -v -E "(${module}\.proto|common\.proto|auth\.proto|cache\.proto|database\.proto)" | \
    wc -l | tr -d ' '
}

# Function to calculate completion percentage
calc_percentage() {
    local actual=$1
    local expected=$2
    if [[ $expected -eq 0 ]]; then
        echo "100"
    else
        echo $(( (actual * 100) / expected ))
    fi
}

echo "📊 1-1-1 Conversion Progress by Module:"
echo "======================================="

total_actual=0
total_modules_complete=0

for module in "${MODULES[@]}"; do
    actual=$(count_1_1_1_files "$module")
    expected=$(get_expected_count "$module")
    percentage=$(calc_percentage $actual $expected)

    total_actual=$((total_actual + actual))

    echo -n "📁 $module: "
    if [[ $actual -eq $expected ]]; then
        echo "✅ COMPLETE ($actual/$expected files) - 100%"
        total_modules_complete=$((total_modules_complete + 1))
    elif [[ $actual -gt 0 ]]; then
        echo "🔄 IN PROGRESS ($actual/$expected files) - ${percentage}%"
    else
        echo "❌ NOT STARTED (0/$expected files) - 0%"
    fi
done

echo
echo "🎯 Overall Completion Status:"
echo "============================="

overall_percentage=$(calc_percentage $total_actual $TOTAL_EXPECTED)
echo "Total Files: $total_actual / $TOTAL_EXPECTED (${overall_percentage}%)"
echo "Modules Complete: $total_modules_complete / ${#MODULES[@]}"

if [[ $total_actual -eq $TOTAL_EXPECTED ]]; then
    echo "🎉 ALL MODULES COMPLETE! 1-1-1 conversion finished."
elif [[ $overall_percentage -ge 80 ]]; then
    echo "🚀 Nearly complete! Just a few more files needed."
elif [[ $overall_percentage -ge 50 ]]; then
    echo "📈 Great progress! Over halfway done."
else
    echo "🏗️  Good start! Keep building the 1-1-1 structure."
fi

echo
echo "📋 Detailed Module Analysis:"
echo "============================"

for module in "${MODULES[@]}"; do
    if [[ $(get_expected_count "$module") -eq 0 ]]; then
        continue
    fi

    echo "📁 $module module breakdown:"
    base_path="$BASE_DIR/$module/proto"

    if [[ -d "$base_path" ]]; then
        for category in enums types messages services requests responses; do
            if [[ -d "$base_path/$category" ]]; then
                count=$(find "$base_path/$category" -name "*.proto" -type f | wc -l | tr -d ' ')
                echo "   └── $category: $count files"
            else
                echo "   └── $category: 0 files (directory not created)"
            fi
        done
    else
        echo "   └── Proto directory not found"
    fi
    echo
done

echo "✅ Successfully completed modules:"
echo "=================================="
for module in "${MODULES[@]}"; do
    actual=$(count_1_1_1_files "$module")
    expected=$(get_expected_count "$module")
    if [[ $actual -eq $expected ]]; then
        echo "   ✅ $module ($actual files)"
    fi
done

echo
remaining_modules=()
echo "🔄 Modules needing completion:"
echo "=============================="
for module in "${MODULES[@]}"; do
    actual=$(count_1_1_1_files "$module")
    expected=$(get_expected_count "$module")
    if [[ $actual -lt $expected ]]; then
        remaining=$((expected - actual))
        echo "   🔄 $module: $remaining files remaining ($actual/$expected)"
        remaining_modules+=("$module")
    fi
done

if [[ ${#remaining_modules[@]} -eq 0 ]]; then
    echo "   🎉 No modules remaining - all complete!"
fi

echo
echo "🛠️  Next Steps:"
echo "==============="
if [[ ${#remaining_modules[@]} -gt 0 ]]; then
    echo "1. Complete remaining modules: ${remaining_modules[*]}"
    echo "2. Add lazy=true to complex fields in new files"
    echo "3. Update import statements in existing code"
    echo "4. Update build configurations (generate.sh, go.mod)"
    echo "5. Test protoc compilation"
else
    echo "1. ✅ All 1-1-1 files created!"
    echo "2. Update import statements in existing code"
    echo "3. Update build configurations"
    echo "4. Test protoc compilation"
    echo "5. Update documentation"
fi

echo
echo "💡 Benefits Achieved:"
echo "===================="
echo "• Better maintainability with single-responsibility files"
echo "• Faster compilation with targeted rebuilds"
echo "• Improved dependency management"
echo "• Performance optimization with lazy loading"
echo "• Consistent structure across all modules"
