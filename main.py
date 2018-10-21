""" 
The url to run this program use this url:
https://raw.githubusercontent.com/planetsig/ufo-reports/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv
"""

import pandas as pd
import utility.downloader as downloader
import utility.convert_csv as convert_csv
import library.sightings_over_time as sightings
import library.most_ufo_sightings as sights
import library.most_sightings_monthly as monthly_sightings
import library.ufolook as look
import library.minutes as sight_min
import library.weekdays as week
import library.usa_map_sightings as usa_map


if __name__ == '__main__':
    global file_name
    file_name = downloader.download_file() 

data = convert_csv.convert_csv_to_dataframe(file_name)

print(sightings.ufo_sightings_over_time(data))
print(monthly_sightings.ufo_sightings_monthly(data))
sights.find_state(data)
look.ufolook(data)   # note, der er endnu ikke lavet textblob analyse
sight_min.ufo_minutes(data)
week.week_graf(data)
#print(usa_map.usa_map_sightings(data))
