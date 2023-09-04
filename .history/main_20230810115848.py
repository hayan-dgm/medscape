import requests
from bs4 import BeautifulSoup
import pandas as pd




def iterate(elements):
        # Loop through the elements and extract information
    for medicine in elements:
        print("*"*30)
        print("topic head:\t" + medicine.find('div',class_='topic-head').text)
        items = medicine.find_all('li')
        for i in items:
            print("Link name:\t" + i.text)
            print("Link url:\t" + i.find('a')['href'])
        # print("Link url:\t" + medicine.find_all('a')['href'])
        print("*"*30)
        try:
            # listItem = medicine.find('li').text
            # print('\n-----'+listItem+'-----\n')
            # medicineName = medicine.find('a').text
            # medicineLink = medicine.find('a')['href']              
            # Print extracted data for debugging
            # print(f"Medicine Name: {medicineName}")
            # print(f"Medicine Link: {medicineLink}")
            # print("-" * 30)
            # Append data to lists
            medNames.append(medicineName)
            medLinks.append(medicineLink)
        except : 
            global loop
            loop = False



url = "https://reference.medscape.com/drugs/allergy-cold"

mainResponse = requests.get(url)


if mainResponse.status_code == 200:
    mainSoup = BeautifulSoup(mainResponse.content,'html.parser')
    
    mainElements = mainSoup.find_all('div', class_='topic-section')

    medNames = []
    medLinks = []

    iterate(mainElements)


    data = {'Medicine Name': medNames , 'Medicine Link':medLinks}
    df = pd.DataFrame(data)
    print(df)

    excel_filename = 'MedScape_allergy_cold.xlsx'
    df.to_excel(excel_filename, index=False, engine='openpyxl')