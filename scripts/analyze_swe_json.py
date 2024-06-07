import sys
import json

def analyze_swe_json(file_path):
    with open(file_path, 'r') as file:
        swe_json_data = json.load(file)
        # Process the JSON data as needed
        print(swe_json_data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_swe_json.py <path_to_json_file>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    analyze_swe_json(json_file_path)
