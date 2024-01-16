#seattle,WA,GHCND:US1WAKG0038
import json
import csv

# Use this station code to select all the measurements belonging to it from the JSON data.
seattle_measurement = []

with open('precipitation.json') as file:
    precipitation = json.load(file)
    
for entry in precipitation:
    if entry['station'] == 'GHCND:US1WAKG0038':
        seattle_measurement.append(entry)

#print(seattle_measurement)

# Calculate the total_monthly_precipitation: a list with the total precipitation per month, for that location
total_monthly_precipitation = {} #month:value,month:value

for entry in seattle_measurement:
    date_parts = entry['date'].split('-')
    month = date_parts[1]
    if month in total_monthly_precipitation:
        #month = old value + new value
        total_monthly_precipitation[month] = entry['value'] + total_monthly_precipitation[month]
    else:
        #month = new value
        total_monthly_precipitation[month] = entry['value']

print(total_monthly_precipitation)

with open('results.json', 'w') as file:
    json.dump(total_monthly_precipitation, file)

