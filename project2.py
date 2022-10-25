import json
import csv

import matplotlib.pyplot as plt
import numpy as np

#json gdp china and usa
accumulator = []
accumulator2 = []

with open('/Users/davidlee/Desktop/Coursework F22/CS 40/project2/GDP USA.json') as f:
    text = f.read()
    accumulator = json.loads(text)
with open('/Users/davidlee/Desktop/Coursework F22/CS 40/project2/gdp_china.json') as f:
    text = f.read()
    accumulator2 = json.loads(text)

gdp_dict_usa = {}
for entry in accumulator[1]:
    gdp_dict_usa.update({int(entry['date']):entry['value']})
years = gdp_dict_usa.keys()
gdp_by_usa = gdp_dict_usa.values()


gdp_dict_china = {}
for entry in accumulator2[1]:
    gdp_dict_china.update({int(entry['date']):entry['value']})
china_years = gdp_dict_china.keys()
gdp_by_china = gdp_dict_china.values()


plt.title('GDP of the USA and China from 1960 to 2020')
plt.plot(years, gdp_by_usa, 'b', label='USA GDP')
plt.plot(china_years, gdp_by_china, 'r', label = 'China GDP')
plt.xlabel('Year')
plt.xticks(np.arange(min(years), max(years),10))
plt.ylabel('Annual GDP (Millions of $)')
plt.legend()
plt.show()


#csv electric vehicles in washington
ev = open('/Users/davidlee/Desktop/Coursework F22/CS 40/project2/Electric_Vehicle_Population_Data.csv')
read = csv.reader(ev)
ev_data = list(read)
ev_dict = {}
for evcar in ev_data[1:]:
    if evcar[6] not in ev_dict:
        ev_dict.update({evcar[6]: 0})
    else:
        ev_dict[evcar[6]]+=1
ev_dict = {key:val for key, val in ev_dict.items() if val > 5000}
brands_ev = ev_dict.keys()
number_of_Cars = ev_dict.values()

plt.title('Top 5 Electric Vehicle presence by brand in Washington in 2022')
plt.xlabel('Brands')
plt.ylabel('Number of EV in Washington')
plt.bar(brands_ev, number_of_Cars)
plt.show()
