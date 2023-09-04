import pandas as pd
import requests
from bs4 import BeautifulSoup
# import sys
# excel_filename = sys.argv[1]
urls = []
# Read the Excel file
excel_filename = 'MedScape_allergy_cold.xlsx'
df = pd.read_excel(excel_filename)

def addInfo(count):
    if int(count) > 0:
        for i in range(int(count)):
            infos.append("empty")
        
        df["Warnings"] = infos

    else:
        print("nothing to add !\n")
        df["Warnings"] = infos

# Iterate through the DataFrame's rows
for index, row in df.iterrows():
    # Create a dictionary for each row and append it to the list
    row_dict = {'Medicine Link': row['Medicine Link']}
    urls.append(row_dict)

infos = []
counter = 1
for elements in urls :
    for key, value in elements.items():
        print("------"+str(counter)+"------")
        counter = counter +1

        try:
            response = requests.get(value+"#5")
            print(response.url)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.content,'html.parser')
                    head = soup.find('div',id="content_5")

                    info =[]
                    h3_tags = head.findAll('h3')
                    for h3 in h3_tags:
                        print("\n***"+h3.text+"***\n")
                        info.append("\n***"+h3.text+"***\n")
                        next_sibling = h3.next_sibling
                        while next_sibling is not None and next_sibling.name != 'h3':
                            print(next_sibling.text)
                            info.append(next_sibling.text)
                            next_sibling = next_sibling.next_sibling
                    infos.append("\n".join(info))

                except:
                    infos.append('unknown')
        except:
            print("#"*30)
            print("************FAILD***********")
            print("#"*30)
            break
      
if len(df["Warnings"]) == len(infos):
    df["Warnings"] = infos
else:
    print(len(df["Warnings"]))
    print(len(infos))

    addInfo((len(df["Warnings"]) - len(infos)) )

df.to_excel(excel_filename, index=False)