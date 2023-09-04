import pandas as pd
import requests
from bs4 import BeautifulSoup

urls = []
# Read the Excel file
excel_filename = 'MedScape_Antidotes.xlsx'
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
            response = requests.get(value)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.content,'html.parser')
                    head = soup.find('div',class_="drugdbsectioncontent drug")
                    h3 = head.findAll("h3")
                    info = []
                    for hs in h3:
                        print(hs.text)
                        sibs = hs.find_next_sibilings("p")
                        # print(sibs)
                        for s in sibs:
                            print("()"*30)
                            print(s.text)
                            print("()"*30)
    
                        # info.append("\n***"+hs.text+"***:\n")
                        # info.append(hs.find_next().text)
                    # infos.append(' '.join(info))
                    break
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