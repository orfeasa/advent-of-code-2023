#!/bin/bash

cookie_file="cookie.txt"
template_dir="day_xx"
day_padded=$(date +%d)
day_directory="day_$day_padded"

# Check if the directory for the day already exists
if [ -d "$day_directory" ]; then
    echo "Directory $day_directory already exists."
    exit 1
fi

# Copy the template directory
cp -r "$template_dir" "$day_directory"

# Fetch input and save to input.txt
cookie=$(tr -d '\n' < "$cookie_file")
year=$(date +%Y)

if (( $(date +%m) <= 6 )); then
    year=$(( year - 1 ))
fi

day=$(date +%-d)
input_url="https://adventofcode.com/$year/day/$day/input"
input_file="$day_directory/input.txt"

# Fetch the input with error handling
if ! curl "$input_url" --compressed -H "Cookie: session=${cookie}" -o "$input_file"; then
    echo "Failed to fetch input from $input_url."
    echo "Please check and update the cookie file."
    rm -r "$day_directory"  # Clean up by removing the created directory
    exit 1
fi

# Detect the platform (Linux or macOS) and use the appropriate sed syntax
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS (BSD sed)
    sed -i '' "s/$template_dir/$day_directory/g" "$day_directory/main.py"
else
    # Linux (GNU sed)
    sed -i "s/$template_dir/$day_directory/g" "$day_directory/main.py"
fi

if [ $? -ne 0 ]; then
    echo "Failed to update file paths in the script."
    exit 1
fi

echo "Input fetched and saved to $input_file"
