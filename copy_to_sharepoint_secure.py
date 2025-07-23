import os
import shutil
import datetime
import re
import sys

# Constants
MAX_FILE_SIZE_MB = 10
ALLOWED_EXTENSIONS = {'.csv', '.xlsx', '.xls'}

def sanitize_filename(filename):
    # Remove any path traversal characters and allow only safe characters
    filename = os.path.basename(filename)
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)

def is_valid_file(file_path):
    if not os.path.isfile(file_path):
        raise ValueError("Source file does not exist.")
    if os.path.getsize(file_path) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise ValueError("File exceeds maximum allowed size.")
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError("Unsupported file extension.")
    return True

def copy_file_to_sharepoint(source_path, destination_folder):
    try:
        # Validate and sanitize
        is_valid_file(source_path)
        sanitized_name = sanitize_filename(os.path.basename(source_path))
        today = datetime.datetime.now().strftime("%m-%d-%Y")
        new_filename = f"{today}_{sanitized_name}"

        # Ensure destination folder exists
        if not os.path.isdir(destination_folder):
            raise ValueError("Destination folder does not exist.")

        destination_path = os.path.join(destination_folder, new_filename)

        # Copy file
        shutil.copy2(source_path, destination_path)
        print(f"File copied successfully to: {destination_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage:
# copy_file_to_sharepoint('C:/Users/YourName/Documents/report.xlsx', 'S:/SharePoint/TeamDocs')

