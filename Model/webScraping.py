from bs4 import BeautifulSoup
import numpy as np
import requests
import random
import pandas as pd

def webScraping():
    list_prices = []
    list_squaredMeter = []
    list_locations = []
    list_rooms = []
    list_bathrooms = []
    list_property_type = []
    city = ''
    startIndex = 0
    endIndex = 0

    for i in range(3):
        index = i
        if(index == 0):
            URL = f"https://www.icasas.mx/venta/habitacionales-casas-chiapas-comitan-dominguez-2_5_6_0_108_0/f_1-recamara,2-recamaras,3-recamaras,4-recamaras,5-recamaras,1-bano,2-banos,3-banos,4-banos,5-banos"
            city = 'COMITAN'
            startIndex = 1
            endIndex = 4
        elif(index == 1):
            URL = f'https://www.icasas.mx/venta/habitacionales-departamentos-chiapas-tuxtla-gutierrez-2_3_6_0_186_0/f_1-recamara,2-recamaras,3-recamaras,4-recamaras,5-recamaras,1-bano,2-banos,3-banos,4-banos,5-banos/t_casas/o_economicos'
            city = 'TUXTLA GUTIERREZ'
            startIndex = 1
            endIndex = 86
        elif(index == 2):    
            URL = f'https://www.icasas.mx/venta/habitacionales-casas-chiapas-san-cristobal-casas-2_5_6_0_161_0/f_1-recamara,2-recamaras,3-recamaras,4-recamaras,5-recamaras,1-bano,2-banos,3-banos,4-banos,5-banos/t_departamentos'
            city = 'SAN CRISTOBAL DE LAS CASAS'
            startIndex = 1
            endIndex = 10
        
        for i in range(startIndex, endIndex):
            URL = f'{URL}/p_{i}'
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find(class_='listAds')

            price_elements = results.find_all("div", class_="price")
            squareMeter_elements = results.find_all("span", class_="areaBuilt")
            location_elements = results.find_all("a", class_='detail-redirection')
            room_elements = results.find_all("span", class_='rooms')
            bathroom_elements = results.find_all("span", class_="bathrooms")


            for price in price_elements:
                value = price.text.strip()
                if(value.__contains__('Remate Bancario')):
                    value = value.replace('Remate Bancario', '')
                elif(value.__contains__('Desde')):
                    value = value.replace('Desde', '')

                value = value.replace('\n', '').replace(' ', '').replace('MX$', '').replace(',','').replace('\t', '')
                value = int(value)
                list_prices.append(value)


            for squareMeter in squareMeter_elements:
                value = squareMeter.text.strip()
                value = value.replace('m2', '').replace(',', '')
                value = np.double(value)
                list_squaredMeter.append(value)


            for location in location_elements:
                value = location.text.strip()
                if(value.__contains__('Casa en Venta')):
                    list_property_type.append('Casa')
                elif(value.__contains__('Departamento en Venta')):
                    list_property_type.append('Departamento')
                list_locations.append(city)


            for room in room_elements:
                value = room.text.strip()
                value = value.strip()
                value = int(value)
                list_rooms.append(value)


            for bathroom in bathroom_elements:
                value = bathroom.text.strip()
                value = value.strip()
                value = int(value)
                list_bathrooms.append(value)      


        if(len(list_squaredMeter) < len(list_locations)):
            while(len(list_squaredMeter) != len(list_locations)):
                new_squaredMeter = random.randint(40,120)
                list_squaredMeter.append(new_squaredMeter)
                if(len(list_squaredMeter) == len(list_locations)):
                    break
        
    return list_locations, list_property_type, list_squaredMeter, list_rooms, list_bathrooms, list_prices



def createDataFrame():
    list_locations, list_property_type, list_squaredMeter, list_rooms, list_bathrooms, list_prices  = webScraping()

    data = {
        'location': list_locations,
        'propertyType': list_property_type,
        'squaredMeter': list_squaredMeter,
        'room': list_rooms,
        'bathroom': list_bathrooms,
        'prices': list_prices,
    }

    dataFrame = pd.DataFrame(data)
    dataFrame.to_csv('dataset.csv', index=False)
    print(dataFrame)

createDataFrame()