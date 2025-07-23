import argparse
import csv
import json
import os
import sys

# To use, enter on cmd line:
# python secure_json_to_csv_cli.py input.json output.csv 

MAX_FILE_SIZE_MB = 5

def sanitize_path(path):
    # Prevent path traversal
    return os.path.basename(path)

def validate_file_size(path):
    size_mb = os.path.getsize(path) / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        raise ValueError(f"File size exceeds {MAX_FILE_SIZE_MB}MB limit.")

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], f'{name}{a}_')
        elif isinstance(x, list):
            for i, a in enumerate(x):
                flatten(a, f'{name}{i}_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def convert_json_to_csv(input_file, output_file):
    input_file = sanitize_path(input_file)
    output_file = sanitize_path(output_file)

    validate_file_size(input_file)

    with open(input_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format.")

    if isinstance(data, dict):
        data = [data]
    elif not isinstance(data, list):
        raise ValueError("JSON must be an object or an array of objects.")

    flat_data = [flatten_json(item) for item in data]

    if not flat_data:
        raise ValueError("No data to write to CSV.")

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=flat_data[0].keys())
        writer.writeheader()
        writer.writerows(flat_data)

def main():
    parser = argparse.ArgumentParser(description='Secure JSON to CSV converter.')
    parser.add_argument('input', help='Input JSON file')
    parser.add_argument('output', help='Output CSV file')
    args = parser.parse_args()

    try:
        convert_json_to_csv(args.input, args.output)
        print(f"CSV file created successfully: {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

