import pandas as pd
import requests
from bs4 import BeautifulSoup

urls = []
# Read the Excel file
excel_filename = '2MedScape_allergy_cold.xlsx'
df = pd.read_excel(excel_filename)

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
        try:
            response = requests.get(value+"#3")
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.content,'html.parser')
                    interactions = soup.find(id = "drug_interlist")
                    for i in interactions:
                        print(i.text)
                    # head = soup.find('div',class_="drugdbsectioncontent drug")
                    # h3 = head.findAll("h3")
                    # info = []
                    # for hs in h3:
                    #     print("\n***"+hs.text+"***:\n")
                    #     info.append("\n***"+hs.text+"***:\n")
                    #     iis = []
                    #     for i in hs.find_all_next("p"):
                    #         if str(i.text).startswith("To view"):
                    #             break
                    #         else:
                    #             print(i.text)
                    #             iis.append(i.text)
                    #             # info.append(i.text)
                    #             # info.append(hs.find_next().text)
                    #     info.append(' '.join(iis))
                    # infos.append(' '.join(info))
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