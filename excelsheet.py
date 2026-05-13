import pandas as pd
import os
from glob import glob

# Folder path
folder_path = r"Your_Folder_Path"

# Sare excel files uthao
excel_files = glob(os.path.join(folder_path, "*.xlsx"))

# Master file output
output_file = os.path.join(folder_path, "Master_File.xlsx")

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:

    for file in excel_files:

        # File read karo
        df = pd.read_excel(file)

        # Filename without extension
        sheet_name = os.path.splitext(os.path.basename(file))[0]

        # Excel sheet name max 31 chars
        sheet_name = sheet_name[:31]

        # Sheet me save karo
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Master file created successfully!")