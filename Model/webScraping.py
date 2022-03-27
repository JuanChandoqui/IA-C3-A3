import urllib.request
from bs4 import BeautifulSoup
import numpy as np
import requests

def webScraping():
    list_prices = []
    list_squaredMeter = []
    list_locations = []
    list_rooms = []
    list_bathrooms = []

    for i in range(2, 86):
        URL = f"https://www.icasas.mx/venta/habitacionales-casas-economicas-chiapas-tuxtla-gutierrez-2_5_6_0_186_0/p_{i}"
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
            # print(value)
            list_prices.append(value)


        for squareMeter in squareMeter_elements:
            value = squareMeter.text.strip()
            value = value.replace('m2', '').replace(',', '')
            value = np.double(value)
            # print(value)
            list_squaredMeter.append(value)


        for location in location_elements:
            value = location.text.strip()
            value = value.replace('Casa en Venta ', '').replace('S/c', '').replace('#s/n', '').replace('#sn', '').replace('\n', '').replace('#0','')
            
            if(value.startswith(' ,')):
                value = value.replace(' ,', '')
            value = value.strip()
            # print(value)
            list_locations.append(value)


        for room in room_elements:
            value = room.text.strip()
            value = value.strip()
            value = int(value)
            list_rooms.append(value)
            # print(value)


        for bathroom in bathroom_elements:
            value = bathroom.text.strip()
            value = value.strip()
            value = int(value)
            # print(value)
            list_bathrooms.append(value)
        
    print(f'len list location: {len(list_locations)},len list square: {len(list_squaredMeter)}, len list rooms: {len(list_rooms)}, len list bathrooms: {len(list_bathrooms)}, len list prices: {len(list_prices)}')

    return list_locations, list_squaredMeter, list_rooms,list_bathrooms, list_prices

webScraping()