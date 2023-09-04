import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
# excel_filename = sys.argv[1]
urls = []
# Read the Excel file
excel_filename = 'MedScape_Anesthetics.xlsx'
df = pd.read_excel(excel_filename)


def addInfo(count):
    if int(count) > 0:
        for i in range(int(count)):
            infos.append("empty")
        
        df["Interactions"] = infos

    else:
        print("nothing to add !\n")
        df["Interactions"] = infos


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
            response = requests.get(value+"#3")
            if response.status_code == 200:
                print(response.url)
                info = []
                try:
                    soup = BeautifulSoup(response.content,'html.parser')
                    interactions = soup.find(id = "drug_interlist")
                    if interactions is None:
                        info.append('unknown')
                    else:
                        titles = interactions.find_all("h4")
                        for t in titles:
                            print("\n***"+t.text+"***\n")
                            info.append("\n***"+t.text+"***\n")
                            contents = t.find_next()
                            for c in contents:
                                print(c.text)
                                info.append(c.text)

                        infos.append("\n".join(info))
                        print("%"*30)
                 
                except:
                    infos.append('unknown')
            else:
                infos.append("network error")
        except:
            print("#"*30)
            print("************FAILD***********")
            print("#"*30)
            break

if len(df["Interactions"]) == len(infos):
    df["Interactions"] = infos
else:
    print(len(df["Interactions"]))
    print(len(infos))
    
    addInfo((len(df["Interactions"]) - len(infos)) )

df.to_excel(excel_filename, index=True)