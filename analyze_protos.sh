#!/bin/bash

# Script to analyze all proto files and categorize them

echo "🔍 ANALYZING ALL PROTO FILES..."
echo "================================"

EMPTY_PROTOS=()
NON_EMPTY_PROTOS=()
ALL_SERVICES=()

# Find all proto files
while IFS= read -r -d '' proto_file; do
    # Check if file is empty or only has basic content
    if [[ ! -s "$proto_file" ]] || [[ $(wc -c < "$proto_file") -lt 100 ]]; then
        EMPTY_PROTOS+=("$proto_file")
    else
        NON_EMPTY_PROTOS+=("$proto_file")

        # Check if it defines a service
        if grep -q "^service " "$proto_file"; then
            service_name=$(grep "^service " "$proto_file" | sed 's/service \([A-Za-z0-9_]*\).*/\1/')
            ALL_SERVICES+=("$service_name")
        fi
    fi
done < <(find pkg -name "*.proto" -print0)

echo "📊 ANALYSIS RESULTS:"
echo "==================="
echo "Total Proto Files: $((${#EMPTY_PROTOS[@]} + ${#NON_EMPTY_PROTOS[@]}))"
echo "Empty Proto Files: ${#EMPTY_PROTOS[@]}"
echo "Non-Empty Proto Files: ${#NON_EMPTY_PROTOS[@]}"
echo "Services Found: ${#ALL_SERVICES[@]}"
echo ""

echo "📝 EMPTY PROTO FILES:"
echo "====================="
for proto in "${EMPTY_PROTOS[@]}"; do
    echo "  - $proto"
done

echo ""
echo "🚀 NON-EMPTY PROTO FILES:"
echo "========================="
for proto in "${NON_EMPTY_PROTOS[@]}"; do
    echo "  - $proto"
done

echo ""
echo "🔧 SERVICES FOUND:"
echo "=================="
for service in "${ALL_SERVICES[@]}"; do
    echo "  - $service"
done

# Save results to files for further processing
printf '%s\n' "${EMPTY_PROTOS[@]}" > empty_protos.txt
printf '%s\n' "${NON_EMPTY_PROTOS[@]}" > non_empty_protos.txt
printf '%s\n' "${ALL_SERVICES[@]}" > services_found.txt

echo ""
echo "✅ Analysis complete! Results saved to:"
echo "  - empty_protos.txt"
echo "  - non_empty_protos.txt"
echo "  - services_found.txt"
