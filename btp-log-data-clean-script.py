import pandas as pd

# Load the Excel file with the appropriate engine
file_path = "BTPsubacct_config_change_log.xlsx"
xls = pd.ExcelFile(file_path, engine='openpyxl')

# Load the main data sheet
df = xls.parse("Subacct Config Change Log")

# Step 1: Remove rows with missing critical fields
critical_fields = ['LOG_ID', 'SUBACCOUNT_ID', 'SUBACCOUNT_NAME', 'REGION', 'CONFIG_AREA', 'PARAMETER', 'ACTION_TYPE', 'RESULT', 'USER_ID', 'SOURCE', 'CHANGE_TIMESTAMP']
df_cleaned = df.dropna(subset=critical_fields)

# Step 2: Standardize text casing for categorical fields
text_fields = ['SUBACCOUNT_NAME', 'REGION', 'CONFIG_AREA', 'PARAMETER', 'ACTION_TYPE', 'RESULT', 'USER_ID', 'SOURCE']
for field in text_fields:
    df_cleaned[field] = df_cleaned[field].astype(str).str.upper()

# Step 3: Ensure consistent datetime formatting
df_cleaned['CHANGE_TIMESTAMP'] = pd.to_datetime(df_cleaned['CHANGE_TIMESTAMP'], errors='coerce')
df_cleaned = df_cleaned.dropna(subset=['CHANGE_TIMESTAMP'])

# Save the cleaned and formatted data to a new Excel file
output_file = "Cleaned_BTPsubacct_config_change_log.xlsx"
df_cleaned.to_excel(output_file, index=False)

print(f"Cleaned and formatted data has been saved to '{output_file}'.")

