**📁 copy\_to\_sharepoint\_secure.py**


**📄 Purpose**
This script securely copies a .csv, .xlsx, or .xls file from a local folder to a SharePoint-synced folder. It renames the file by prefixing the current date in MM-DD-YYYY format to the original filename.



✅ **Features**
File validation: Ensures the file exists and is under 10MB.
Extension check: Only allows .csv, .xlsx, and .xls files.
Path sanitization: Prevents path traversal attacks (CWE-22).
Safe renaming: Adds the current date to the filename.
Enterprise-ready: Designed with OWASP and CWE security best practices.


🧰 **Prerequisites**
Python 3.6 or higher
A SharePoint folder synced locally (e.g., via OneDrive or mapped network drive)


🚀 **Usage**

1. Save the script
   Save the script as copy\_to\_sharepoint\_secure.py.
2. Modify the script or call the function
   You can call the function directly in the script or from another script:

```

copy\_file\_to\_sharepoint('C:/Users/YourName/Documents/report.xlsx', 'S:/SharePoint/TeamDocs')



```



This will copy report.xlsx to the SharePoint folder and rename it to something like:

```

07-02-2025\_report.xlsx

```


**🔐 Security Considerations**
CWE-22: Prevents path traversal by sanitizing file names.
CWE-434: Restricts file types to known safe extensions.
CWE-400: Limits file size to prevent resource exhaustion.
CWE-20: Validates all inputs before processing.

