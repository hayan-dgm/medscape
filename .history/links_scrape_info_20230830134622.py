import pandas as pd
import json

import requests
from bs4 import BeautifulSoup
import sys
# urls= []
# urls = sys.argv[1]
urls = json.loads(list(sys.argv[1]))
excel_filename = sys.argv[2]
# df = sys.argv[3]

# # Read the Excel file
# excel_filename = 'MedScape_Antidotes_one.xlsx'
df = pd.read_excel(excel_filename)

# # Iterate through the DataFrame's rows
# for index, row in df.iterrows():
#     # Create a dictionary for each row and append it to the list
#     row_dict = {'Medicine Link': row['Medicine Link']}
#     urls.append(row_dict)

infos = []
counter = 1
for elements in urls :
    for key, value in elements.items():
        print("------"+str(counter)+"------")
        try:
            response = requests.get(value)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.content,'html.parser')
                    head = soup.find('div',class_="drugdbsectioncontent drug")
                    h3 = head.findAll("h3")
                    info = []
                    for hs in h3:
                        print("\n***"+hs.text+"***:\n")
                        info.append("\n***"+hs.text+"***:\n")
                        iis = []
                        for i in hs.find_all_next("p"):
                            if str(i.text).startswith("To view"):
                                break
                            else:
                                print(i.text)
                                iis.append(i.text)
                                # info.append(i.text)
                                # info.append(hs.find_next().text)
                        info.append(' '.join(iis))
                    infos.append(' '.join(info))
                except:
                    infos.append('unknown')
            # counter = counter +1
        except:
            print("#"*30)
            print("************FAILD***********")
            print("#"*30)
            break
                #  print(BeautifulSoup(response.content,'html.parser').prettify())
                # dosing = soup.find('div',id_="dose_adult")
                # print(soup.prettify())
                # if dosing :
                #     info = dosing.find_next_siblings('div')
                #     title=[]
                #     for inner in info:
                #         title.append(inner.text)
                #     titles.append(' '.join(title)) 
                #            
# for i in infos:
df["info"] = infos

df.to_excel(excel_filename, index=False)