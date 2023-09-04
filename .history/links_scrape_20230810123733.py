import pandas as pd
import requests
from bs4 import BeautifulSoup

urls = []
# Read the Excel file
excel_filename = 'MedScape_allergy_cold.xlsx'
df = pd.read_excel(excel_filename)

# Iterate through the DataFrame's rows
for index, row in df.iterrows():
    # Create a dictionary for each row and append it to the list
    row_dict = {'Medicine Link': row['Medicine Link']}
    urls.append(row_dict)

titles = []
for elements in urls :
    for key, value in elements.items():
        print(value)
        response = requests.get(value)
        if response.status_code == 200:
            # soup = BeautifulSoup(response.content,'html.parser')
             print(BeautifulSoup(response.content,'html.parser').prettify())
             break
        break
    break
            # dosing = soup.find('div',id_="dose_adult")
            # print(soup.prettify())
            # if dosing :
            #     info = dosing.find_next_siblings('div')
            #     title=[]
            #     for inner in info:
            #         title.append(inner.text)
            #     titles.append(' '.join(title))            
# for i in titles:
#     print("--\n"+i)

#     df["dosing"] = titles
#     df.to_excel(excel_filename, index=False)