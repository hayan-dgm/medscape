import pandas as pd
import requests
from bs4 import BeautifulSoup
import shlex
import subprocess

# import sys
# excel_filename = sys.argv[1]
urls = []
# Read the Excel file

excel_filename = 'MedScape_Anesthetics.xlsx'
df = pd.read_excel(excel_filename)


def addInfo(count):
    if int(count) > 0:
        for i in range(int(count)):
            infos.append("empty")
        
        df["Adverse Effects"] = infos

    else:
        print("nothing to add !\n")
        df["Adverse Effects"] = infos


# Iterate through the DataFrame's rows
for index, row in df.iterrows():
    # Create a dictionary for each row and append it to the list
    row_dict = {'Medicine Link': row['Medicine Link']}
    urls.append(row_dict)

infos = []
failed = []
counter = 1



for elements in urls :
    for key, value in elements.items():
        print("------"+str(counter)+"------")
        counter = counter +1
        try:
            response = requests.get(value+"#4")
            print(response.url)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.content,'html.parser')
                    head = soup.find('div',id="content_4")

                    info =[]
                    if head is not None:
                        h3_tags = head.findAll('h3')
                        for h3 in h3_tags:
                            print("\n***"+h3.text+"***\n")
                            info.append("\n***"+h3.text+"***\n")
                            next_sibling = h3.next_sibling
                            while next_sibling is not None and next_sibling.name != 'h3':
                                # if next_sibling.name == 'p':
                                print(next_sibling.text)
                                info.append(next_sibling.text)
                                next_sibling = next_sibling.next_sibling
                        infos.append("\n".join(info))
                    else:
                        infos.append("\n empty".join(info))

                except:
                    infos.append('unknown')
            else:
                infos.append("network error")
    
        except:
            print("#"*30)
            print("************FAILD***********")
            infos.append("\n failed")
            failed.append(response.url)

            print("#"*30)
            break

with open ('failed.txt', 'w') as file:  
    for line in failed:  
        file.writelines(line)  
if len(df["Adverse Effects"]) == len(infos):
    df["Adverse Effects"] = infos
else:
    print(len(df["Adverse Effects"]))
    print(len(infos))

    if len(df["Adverse Effects"]) != len(infos):
        addInfo((len(df["Adverse Effects"]) - len(infos)) )



df.to_excel(excel_filename, index=False,)