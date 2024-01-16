import json
import csv

# Use this station code to select all the measurements belonging to it from the JSON data.
# seattle_measurement = []
# with open('precipitation.json') as file:
#     precipitation = json.load(file) 
# for entry in precipitation:
#     if entry['station'] == 'GHCND:US1WAKG0038':
#         seattle_measurement.append(entry)

# Calculate the total_monthly_precipitation: a list with the total precipitation per month, for that location
# total_monthly_precipitation = {}
# for entry in seattle_measurement:
#     date_parts = entry['date'].split('-')
#     month = date_parts[1]
#     if month in total_monthly_precipitation:
#         total_monthly_precipitation[month] = entry['value'] + total_monthly_precipitation[month]
#     else:
#         total_monthly_precipitation[month] = entry['value']
# with open('results.json', 'w') as file:
#     json.dump(total_monthly_precipitation, file)

# Calculate the total_yearly_precipitation, i.e., the sum of the precipitation over the whole year for one location.
# with open('results.json') as file:
#     results = json.load(file)
# total_yearly_preciptation = 0
# for month in results:
#     total_yearly_preciptation = total_yearly_preciptation + results[month]

# Calculate the relative_monthly_precipitation (proportion of the yearly rain) per month, 
# relative_monthly_precipitation = {}
# for month in results:
#     relative_monthly_precipitation[month] = results[month]/total_yearly_preciptation
# with open('results.json', 'w') as file:
#     json.dump(relative_monthly_precipitation, file)

# Rewrite your code so that it calculates all the above for each location (don’t do this manually,
    # but instead have Python read the station codes from the CSV).

stations_sorted = {}
with open('stations.csv') as file:
    stations = csv.DictReader(file)
    stations_list = list(stations)
with open('precipitation.json') as file:
    precipitation = json.load(file) 

for entry in stations_list:
    entry_name = entry["Location"]
    stations_sorted[entry_name] = {
        "station": entry["Station"],
        "state": entry["State"]
    }

precipitation_sorted = {}
for entry in precipitation:
    entry_name = entry["station"]
    if entry_name in precipitation_sorted:
        precipitation_sorted[entry_name].append(entry)
    else:
        precipitation_sorted[entry_name] = [entry]


total_monthly_precipitation = {}
for location in precipitation_sorted:
    per_location_dict = {}
    for entry in precipitation_sorted[location]:
        date_parts = entry['date'].split('-')
        month = date_parts[1]
        if month in per_location_dict:
            per_location_dict[month] = entry['value'] + per_location_dict[month]
        else:
            per_location_dict[month] = entry['value']
    total_monthly_precipitation[location] = per_location_dict

print(total_monthly_precipitation)
print(stations_sorted)

# Calculate the relative_yearly_precipitation compared to the other stations, i.e. what
    # percentage of all the measured rain in all locations, fell in Seattle?
# Commit your script and your output results.json to your version history.

