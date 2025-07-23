**Secure CSV Append Script with Logging**

This Python script provides a secure and robust way to append data from one CSV file to another, ensuring:



**Filename validation**

Header consistency

Logging of all operations

Error handling for common issues



**📂 Features**

✅ Validates filenames to prevent unsafe file access

✅ Checks if both source and target files exist

✅ Ensures both files are non-empty

✅ Verifies that CSV headers match before appending

✅ Skips rows with empty fields

✅ Logs all actions and errors to secure\_csv\_append.log



**🛠️ Requirements**

Python 3.x

No external libraries required



**🚀 Usage**

```
from secure\_csv\_append\_script\_logged import secure\_append\_csv



secure\_append\_csv("source.csv", "target.csv")


```


**📋 Function Overview**

secure\_append\_csv(source\_file, target\_file)

Appends rows from source\_file to target\_file after validating:



Filenames

File existence

Header match

Non-empty content

is\_valid\_filename(filename)

Ensures the filename is a .csv with safe characters.



read\_csv\_file(filepath)

Reads and returns rows from a CSV file.



write\_csv\_file(filepath, rows)

Appends non-empty rows to a CSV file.



headers\_match(header1, header2)

Checks if two CSV headers are identical.



**🧾 Logging**

All operations and errors are logged to:



secure\_csv\_append.log

Log format:

```

YYYY-MM-DD HH:MM:SS - LEVEL - Message

```

**⚠️ Error Handling**

Raises exceptions for:



Invalid filenames

Missing files

Empty files

Header mismatches

File read/write errors



**📄 License**

This script is provided as-is for educational and internal use. Customize as needed for your project.





