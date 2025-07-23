**📄secure\_json\_to\_csv\_cli.py**



📌 **Purpose**

This script securely converts a JSON file to a CSV file using command-line arguments. It is designed for enterprise environments with strong security practices to prevent common vulnerabilities.



✅ **Features**

File size validation: Limits input to 5MB (CWE-400)

Path sanitization: Prevents path traversal (CWE-22)

Extension and structure checks: Ensures valid JSON format (CWE-20, CWE-502)

Flattening: Converts nested JSON into flat CSV-compatible format

UTF-8 encoding: Supports international characters



**🧰 Prerequisites**

Python 3.6 or higher

No external libraries required



**🚀 Usage**

1\. Save the script

Save the script as secure\_json\_to\_csv\_cli.py.



2\. Open a terminal or command prompt

3\. Run the script with:


```

python secure\_json\_to\_csv\_cli.py input.json output.csv

```





**Replace**:

input.json with the path to your JSON file

output.csv with the desired output file name



**🛡️ Security Considerations**

CWE-22: Sanitizes file names to prevent directory traversal

CWE-434: Only processes JSON files

CWE-400: Limits file size to prevent resource exhaustion

CWE-20: Validates input structure before processing

