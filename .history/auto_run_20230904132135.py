import subprocess
import pandas as pd
import json
import os
import sys



# urls = []
# Read the Excel file
excel_filename = 'MedScape_allergy_cold.xlsx'
# df = pd.read_excel(excel_filename)

# # Iterate through the DataFrame's rows
# for index, row in df.iterrows():
#     # Create a dictionary for each row and append it to the list
#     row_dict = {'Medicine Link': row['Medicine Link']}
#     urls.append(row_dict)


# subprocess.run(['python','links_scrape_info.py',excel_filename],shell=False)
subprocess.run(['python','main.py'],shell=False)
subprocess.run(['python','links_scrape_dosage_forms.py'],shell=False)
subprocess.run(['python','links_scrape_interactions.py'],shell=False)
subprocess.run(['python','links_scrape_adverse_effects.py'],shell=False)
subprocess.run(['python','links_scrape_warnings.py'],shell=False)
subprocess.run(['python','links_scrape_pregnancy.py'],shell=False)
subprocess.run(['python','links_scrape_pharmacology.py'],shell=False)