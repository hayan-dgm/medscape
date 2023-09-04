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
            response = requests.get(value+"#10")
            print(response.url)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.content,'html.parser')
                    head = soup.find('div',id="content_10")
                    # print("#"*30)
                    # print("\n***"+head.text+"***\n")
                    # print("#"*30)
                    info =[]
                    # p_tags = head.findAll("p")
                    # for t in head:
                        # next_t = t.next_sibling
                        # while next_t is not None :
                        #     if next_t.name == 'p':
                        #         print(next_t.text)
                        #     else:
                        #         break
                        #     next_t= next_t.next_sibling
                    p_tags =head.find_all()
                    for tags in p_tags:
                        while p_tags.name != "p":
                                p_tags=p_tags.next_sibling
                    for p in p_tags:
                        if p.name == 'p':
                            print(p.text)
                        else:
                            print(p.name)
                            break
                        # else:
                        #     break

                    h3_tags =head.findAll('h3')
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
                    # innerParas = head.findAll("p")
                    # for h in innerHeads:
                    #     print("\n***"+h.text+"***\n")
                    #     for p in innerParas:
                    #         print(p.text)
                        # print("#"*30)
                        # contents = h.contents
                        # for info in contents:
                        #     print(info.text)
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
    df["Pharmacology"] = infos

df.to_excel(excel_filename, index=False)