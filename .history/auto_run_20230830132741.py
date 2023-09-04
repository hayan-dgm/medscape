import subprocess
import pandas as pd
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

subprocess.run([sys.executable,'links_scrape_info.py',urls,excel_filename,df])