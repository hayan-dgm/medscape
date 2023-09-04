import subprocess
import pandas as pd
import os
import sys



urls = []
# Read the Excel file
excel_filename = 'MedScape_Antidotes_one.xlsx'
df = pd.read_excel(excel_filename)

# Iterate through the DataFrame's rows
for index, row in df.iterrows():
    # Create a dictionary for each row and append it to the list
    row_dict = {'Medicine Link': row['Medicine Link']}
    urls.append(row_dict)

path = os.path.join(*urls.keys())  # This will work

subprocess.run(['python','links_scrape_info.py',path,excel_filename,df],shell=False)