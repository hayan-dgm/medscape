import pandas as pd
import requests
from bs4 import BeautifulSoup

urls = []
# Read the Excel file
excel_filename = 'MedScape_Antidotes_one.xlsx'
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
            response = requests.get(value+"#0")
            print(response.url)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.content,'html.parser')
                    head = soup.find('div',id="dose_adult")
                    # print("#"*30)
                    # print("\n***"+head.text+"***\n")
                    # print("#"*30)

                    innerHeads =head.findAll('h3')
                    for h in innerHeads:
                        # print("#"*30)
                        print("\n***"+h.text+"***\n")
                        # print("#"*30)
                        for info in h.contents:
                            print(info.text)
            #         info = []
            #         for h in innerHeads:
            #             # print(h.text)
            #             info.append("\n***"+h.text+"***:\n")
            #             info.append(h.find_next('p').text)
            #             print(h.text)
            #             print(h.find_next('p').text)
            #             print("*"*30)
            #         infos.append(' '.join(info))  
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
#     df["info"] = infos

# df.to_excel(excel_filename, index=False)