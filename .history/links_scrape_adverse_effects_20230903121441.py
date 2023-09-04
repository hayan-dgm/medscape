import pandas as pd
import requests
from bs4 import BeautifulSoup
import shlex
import subprocess

# import sys
# excel_filename = sys.argv[1]
urls = []
# Read the Excel file

config = 0

configs = ["gr-ath.prod.surfshark.comsurfshark_openvpn_tcp.ovpn","ge-tbs.prod.surfshark.comsurfshark_openvpn_tcp.ovpn","fr-bod.prod.surfshark.comsurfshark_openvpn_tcp.ovpn","dk-cph.prod.surfshark.comsurfshark_openvpn_tcp.ovpn","cy-nic.prod.surfshark.comsurfshark_openvpn_tcp.ovpn"]
# write the command to a variable
cmd = 'start /b cmd /c \"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe\" --connect '+configs[config]

# split the command to parameters (It's not a necessity, it's just a rule of good taste)
args = shlex.split(cmd)

# run and remember the process as 'x'
x = subprocess.Popen(args, shell=True)

excel_filename = 'MedScape_allergy_cold.xlsx'
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
        except requests.exceptions.ConnectionError as e:
            if config < len(configs):
                config = config + 1
            else:
                config =  0
            cmd = 'start /b cmd /c \"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe\" --connect '+configs[config]
            args = shlex.split(cmd)
            x = subprocess.Popen(args, shell=True)
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