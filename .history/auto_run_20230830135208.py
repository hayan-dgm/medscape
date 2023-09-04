import subprocess
import pandas as pd
import json
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


subprocess.run(['python','links_scrape_info.py',excel_filename],shell=False)
subprocess.run(['python','links_scrape_dosage_forms.py',excel_filename],shell=False)
subprocess.run(['python','links_scrape_interactions.py',excel_filename],shell=False)
subprocess.run(['python','links_scrape_adverse_effects.py',excel_filename],shell=False)
subprocess.run(['python','links_scrape_warnings.py',excel_filename],shell=False)
subprocess.run(['python','links_scrape_pregnancy.py',excel_filename],shell=False)
subprocess.run(['python','links_scrape_pharmacology.py',excel_filename],shell=False)