import yaml
import json
from jsonschema import validate, ValidationError, Draft7Validator
import sys

class SpecValidator:
    def __init__(self, schema_path):
        with open(schema_path, 'r') as f:
            self.schema = json.load(f)

    def validate_spec(self, spec_path):
        with open(spec_path, 'r') as f:
            spec = yaml.safe_load(f)

        validator = Draft7Validator(self.schema)
        errors = list(validator.iter_errors(spec))
        
        if not errors:
            return True, []
        
        # Simple formatting of errors
        error_messages = [f"{error.json_path}: {error.message}" for error in errors]
        return False, error_messages

if __name__ == "__main__":
    # Usage: python validate_spec.py <path_to_spec> <path_to_schema>
    success, errs = SpecValidator(sys.argv[2]).validate_spec(sys.argv[1])
    if success:
        print("✅ Validation Passed")
        sys.exit(0)
    else:
        print("❌ Validation Failed:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)