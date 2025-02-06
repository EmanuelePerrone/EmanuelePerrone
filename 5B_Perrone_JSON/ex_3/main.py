import json
import jsonschema
from jsonschema import validate
from datetime import datetime

import jsonschema.exceptions

def load_schema():
    with open('health-monitoring-schema.json','r') as schema_file:
        return json.load(schema_file)
    
def load_data():
    with open('health-data.json','r') as schema_file:
        return json.load(schema_file)
    
def validate_health_data(health_data, schema):
    for record in health_data:
        try:
            validate(instance=record, schema=schema)
            print(f"Validate misuration: {record['measurement_type']} - {record['value']} (Data:{record['timestamp']})")
        except jsonschema.exceptions.ValidationError as e:
            print(f"Validation error in measurement: {e.message}")

def main():
    schema=load_schema()
    health_data=load_data()

    validate_health_data(health_data, schema)

    print("\nHealth monitorade:")
    for record in health_data:
        measurement_type=record['measurement_type']
        value=record['value']
        print(f"{measurement_type}: {value}")
        
if __name__ == "__main__":
    main()

