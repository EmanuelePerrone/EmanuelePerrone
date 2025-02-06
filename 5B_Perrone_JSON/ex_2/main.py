import json
import jsonschema
from jsonschema import validate
from datetime import datetime

def load_schema():
    with open('tracking.schema.json', 'r') as schema_file:
        return json.load(schema_file)

def load_tracking_data():
    with open('tracking-data.json', 'r') as data_file:
        return json.load(data_file)

def validate_tracking_data(tracking_data, schema):
    for step in tracking_data:
        try:
            validate(instance=step, schema=schema)
            print(f"Valid tracking step: {step['location']['city']}, {step['location']['state']} - {step['timestamp']}")
        except jsonschema.exceptions.ValidationError as e:
            print(f"Validation error in tracking step: {e.message}")

def main():
    schema = load_schema()
    tracking_data = load_tracking_data()

    validate_tracking_data(tracking_data, schema)

    print("\nPackage tracking:")
    for step in tracking_data:
        location = step['location']
        timestamp = datetime.fromisoformat(step['timestamp'].replace('Z', '+00:00'))
        print(f"- {location['city']}, {location['state']} - {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
