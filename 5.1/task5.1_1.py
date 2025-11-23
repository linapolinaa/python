import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def get_country_info(country_name):
    try:
        url = f"https://en.wikipedia.org/wiki/{country_name.replace(' ', '_')}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        infobox = soup.find('table', class_='infobox')
        
        capital = "N/A"
        area = "N/A"
        population = "N/A"

        if infobox:
            all_text = infobox.get_text()
            all_numbers = re.findall(r'\d{1,3}(?:,\d{3}){2,}', all_text)
            if all_numbers:
                population = max(all_numbers, key=lambda x: int(x.replace(',', ''))).replace(',', '')
            
            for row in infobox.find_all('tr'):
                header = row.find('th')
                if header and 'capital' in header.get_text().lower():
                    data_cell = row.find('td')
                    if data_cell:
                        capital_link = data_cell.find('a')
                        if capital_link:
                            capital = capital_link.get_text().strip()
                            break
            
            for row in infobox.find_all('tr'):
                header = row.find('th')
                if header and any(word in header.get_text().lower() for word in ['area', 'total']):
                    data_cell = row.find('td')
                    if data_cell:
                        area_text = data_cell.get_text()
                        area_match = re.search(r'([\d,]+)\s*k(m²|m2)', area_text)
                        if area_match:
                            area = area_match.group(1).replace(',', '')
                            break

        return {
            'country': country_name,
            'capital': capital,
            'area': area,
            'population': population
        }
        
    except:
        return None

with open('countries.txt', 'r', encoding='utf-8') as file:
    countries = [line.strip() for line in file if line.strip()]

results = []
for country in countries:
    data = get_country_info(country)
    if data:
        results.append(data)
    time.sleep(1)

with open('countries_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['country', 'capital', 'area', 'population'])
    writer.writeheader()
    writer.writerows(results)