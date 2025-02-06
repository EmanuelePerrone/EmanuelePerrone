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
        print(f"Error loading weather data: {e}")
        return []

def validate_weather_data(weather_data, schema):
    for record in weather_data:
        try:
            validate(instance=record, schema=schema)
            print(f"Validated: {record['timestamp']} - Temp: {record['temperature']}°C, Humidity: {record['humidity']}%")
        except jsonschema.exceptions.ValidationError as e:
            print(f"Validation error in record {record}: {e.message}")

def main():
    schema = load_schema()
    if schema is None:
        return

    weather_data = load_data()
    if not weather_data:
        return

    validate_weather_data(weather_data, schema)

    print("\nWeather Data Recorded:")
    for record in weather_data:
        print(f" {record['timestamp']}")
        print(f" Temperature: {record['temperature']}°C")
        print(f" Humidity: {record['humidity']}%")
        print(f" Pressure: {record['pressure']} hPa")
        print(f" Wind: {record['wind']['speed']} {record['wind']['unit']} ({record['wind']['direction']})")
        print(f" Rainfall: {record['rainfall']} mm\n")

if __name__ == "__main__":
    main()
