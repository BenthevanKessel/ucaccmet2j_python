import json
import csv

#seattle,WA,GHCND:US1WAKG0038
seattle_measurement = []

with open('precipitation.json') as file:
    precipitation = json.load(file)
    
for entry in precipitation:
    if entry['station'] == 'GHCND:US1WAKG0038':
        seattle_measurement.append(entry)

print(seattle_measurement)