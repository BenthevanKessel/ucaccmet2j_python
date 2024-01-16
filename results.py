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

# print(total_monthly_precipitation)

with open('results.json', 'w') as file:
    json.dump(total_monthly_precipitation, file)

# Calculate the total_yearly_precipitation, i.e., the sum of the precipitation over the whole year for one location.

with open('results.json') as file:
    results = json.load(file)

total_yearly_preciptation = 0

for month in results:
    total_yearly_preciptation = total_yearly_preciptation + results[month]

# print(total_yearly_preciptation)

# Calculate the relative_monthly_precipitation (proportion of the yearly rain) per month, 
    # e.g., if 20% of the rain in 2010 in Seattle fell in November, the corresponding value should read 0.2

relative_monthly_precipitation = {}

for month in results:
    relative_monthly_precipitation[month] = results[month]/total_yearly_preciptation

print(relative_monthly_precipitation)

# Commit your script and your output results.json to your version history.

with open('results.json', 'w') as file:
    json.dump(relative_monthly_precipitation, file)