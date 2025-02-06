import json
import jsonschema
from jsonschema import validate
from datetime import datetime

def load_schema():
    try:
        with open("schema.json", "r") as schema_file:
            return json.load(schema_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading schema: {e}")
        return None

def load_data():
    try:
        with open("data.json", "r") as data_file:
            return json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading medical test data: {e}")
        return []

def evaluate_status(value, min_ref, max_ref):
    if value < min_ref:
        return "too low"
    elif value > max_ref:
        return "high value"
    return "ok"

def validate_medical_data(medical_data, schema):
    for record in medical_data:
        try:
            validate(instance=record, schema=schema)

            value = record["result"]["value"]
            min_ref = record["result"]["reference_range"]["min"]
            max_ref = record["result"]["reference_range"]["max"]

            computed_status = evaluate_status(value, min_ref, max_ref)

            stored_status = record["result"]["status"]
            if computed_status != stored_status:
                print(f"⚠️ Mismatch in status for {record['test_type']} - Expected: {computed_status}, Found: {stored_status}")
                record["result"]["status"] = computed_status

            print(f"Validated: {record['patient']['first_name']} {record['patient']['last_name']} - {record['test_type']} = {value} {record['result']['unit']} ({computed_status})")

        except jsonschema.exceptions.ValidationError as e:
            print(f"Validation error in record {record}: {e.message}")

def main():
    schema = load_schema()
    if schema is None:
        return

    medical_data = load_data()
    if not medical_data:
        return

    validate_medical_data(medical_data, schema)

    print("\nMedical Test Results:")
    for record in medical_data:
        print(f" Patient: {record['patient']['first_name']} {record['patient']['last_name']}")
        print(f" Test Date: {record['timestamp']}")
        print(f" Test: {record['test_type']}")
        print(f" Value: {record['result']['value']} {record['result']['unit']}")
        print(f" Reference Range: {record['result']['reference_range']['min']} - {record['result']['reference_range']['max']} {record['result']['unit']}")
        print(f" Status: {record['result']['status']}\n")

if __name__ == "__main__":
    main()
