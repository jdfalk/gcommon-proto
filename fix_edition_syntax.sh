#!/bin/bash

# Fix files where import comes before edition declaration
files=$(buf generate 2>&1 | grep "syntax error: unexpected \"edition\"" | cut -d: -f1 | sort | uniq)

for file in $files; do
    if [[ -f "$file" ]]; then
        echo "Fixing $file"
        
        # Create temporary file to reconstruct proper order
        temp_file=$(mktemp)
        
        # Extract parts
        head_comments=$(grep -n "^//" "$file" | head -10 | while read line; do echo "${line#*:}"; done)
        edition_line=$(grep "^edition = " "$file")
        package_line=$(grep "^package " "$file")
        imports=$(grep "^import " "$file" | sort | uniq)
        options=$(grep "^option " "$file")
        
        # Get everything after the first message/enum definition
        rest_start=$(grep -n "^message\|^enum\|^service" "$file" | head -1 | cut -d: -f1)
        if [[ -n "$rest_start" ]]; then
            rest_content=$(tail -n +$rest_start "$file")
        fi
        
        # Reconstruct file in proper order
        echo "$head_comments" > "$temp_file"
        echo "" >> "$temp_file"
        echo "$edition_line" >> "$temp_file"
        echo "" >> "$temp_file"
        echo "$package_line" >> "$temp_file"
        echo "" >> "$temp_file"
        echo "$imports" >> "$temp_file"
        echo "" >> "$temp_file"
        echo "$options" >> "$temp_file"
        echo "" >> "$temp_file"
        if [[ -n "$rest_content" ]]; then
            echo "$rest_content" >> "$temp_file"
        fi
        
        # Replace original with fixed version
        mv "$temp_file" "$file"
    fi
done
