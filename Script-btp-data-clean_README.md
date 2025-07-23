**📄 BTP Subaccount Config Change Log – Data Cleaning Script**
**🧰 Overview**
This script processes and cleans the SAP BTP Subaccount Configuration Change Log to prepare it for analysis and visualization. It ensures the data is consistent, complete, and formatted for tools like Power BI or Excel dashboards.

**📂 Input**
File: BTPsubacct_config_change_log.xlsx
Sheet: Subacct Config Change Log
Fields Used:
LOG_ID, SUBACCOUNT_ID, SUBACCOUNT_NAME, REGION, CONFIG_AREA, PARAMETER, OLD_VALUE, NEW_VALUE, ACTION_TYPE, RESULT, USER_ID, SOURCE, CHANGE_TIMESTAMP

**🧹 Cleaning Steps**
Remove Incomplete Records
Rows missing any of the following critical fields are dropped:

LOG_ID, SUBACCOUNT_ID, SUBACCOUNT_NAME, REGION, CONFIG_AREA, PARAMETER, ACTION_TYPE, RESULT, USER_ID, SOURCE, CHANGE_TIMESTAMP
Standardize Text Fields
All text-based fields are converted to uppercase for consistency:

SUBACCOUNT_NAME, REGION, CONFIG_AREA, PARAMETER, ACTION_TYPE, RESULT, USER_ID, SOURCE
Normalize Timestamps

CHANGE_TIMESTAMP is parsed into a consistent datetime format.
Rows with invalid or unparseable timestamps are removed.

**💾 Output**
File: Cleaned_BTPsubacct_config_change_log.xlsx
Format: Excel (.xlsx)
Location: Download Cleaned File

**🚀 How to Use the Script**
Requirements
- Python 3.8+
- pandas
- openpyxl
Steps
Place the original file BTPsubacct_config_change_log.xlsx in your working directory.
Run the script using any Python environment:
```
python clean_btp_log.py
```

Check the output file Cleaned_BTPsubacct_config_change_log.xlsx in the same directory.
Script Location
If you don’t have the script yet, I can generate and save it for you as a .py file. Just let me know!

**📊 Ready for Analysis**
This cleaned dataset is now suitable for:

- Power BI dashboards
- Excel pivot tables
- Governance and audit reporting
- Trend and anomaly detection
