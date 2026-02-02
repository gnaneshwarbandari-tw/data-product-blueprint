#!/bin/bash
# Internal helper to trigger Python validation

SPEC_FILE=$1
SCHEMA_FILE=$2
VALIDATOR_PATH=$3

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is required for validation."
    exit 1
fi

# Install dependencies if missing (optional/silent)
# pip3 install jsonschema PyYAML -q

# Run the validator
python3 "$VALIDATOR_PATH" "$SPEC_FILE" "$SCHEMA_FILE"