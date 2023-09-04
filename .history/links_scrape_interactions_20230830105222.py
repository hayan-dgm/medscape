import pandas as pd
import requests
from bs4 import BeautifulSoup

urls = []
# Read the Excel file
excel_filename = 'MedScape_Antidotes2.xlsx'
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
                            t.find_all_sibilings()
                            for sib in t:
                                print(sib.text)
                        print("%"*30)
                        # info.append(interactions.text)
                    # for i in interactions:
                    #     print(i.text)
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
# infos.append('\n'.join(info))         
# for i in infos:
# df["interactions"] = infos

# df.to_excel(excel_filename, index=False)