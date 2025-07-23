
import csv
import os
import re
import logging

# Configure secure logging
logging.basicConfig(
    filename='secure_csv_append.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def is_valid_filename(filename):
    return re.match(r'^[\w,\s-]+\.csv$', filename) is not None

def read_csv_file(filepath):
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            logging.info(f"Successfully read file: {filepath}")
            return rows
    except Exception as e:
        logging.error(f"Error reading file {filepath}: {e}")
        raise

def write_csv_file(filepath, rows):
    try:
        with open(filepath, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in rows:
                if all(field.strip() for field in row):  # Skip rows with empty fields
                    writer.writerow(row)
            logging.info(f"Successfully appended rows to file: {filepath}")
    except Exception as e:
        logging.error(f"Error writing to file {filepath}: {e}")
        raise

def headers_match(header1, header2):
    return header1 == header2

def secure_append_csv(source_file, target_file):
    if not (is_valid_filename(source_file) and is_valid_filename(target_file)):
        logging.error("Invalid filename(s) provided.")
        raise ValueError("Invalid filename(s). Only .csv files with safe characters are allowed.")

    if not (os.path.exists(source_file) and os.path.exists(target_file)):
        logging.error("One or both files do not exist.")
        raise FileNotFoundError("One or both files do not exist.")

    source_rows = read_csv_file(source_file)
    target_rows = read_csv_file(target_file)

    if not source_rows or not target_rows:
        logging.error("One or both files are empty.")
        raise ValueError("One or both files are empty.")

    if not headers_match(source_rows[0], target_rows[0]):
        logging.error("CSV headers do not match.")
        raise ValueError("CSV headers do not match.")

    write_csv_file(target_file, source_rows[1:])
    logging.info(f"Appended data from {source_file} to {target_file} successfully.")
