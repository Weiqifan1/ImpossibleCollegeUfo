""" 
The url to run this program use this url:
https://raw.githubusercontent.com/planetsig/ufo-reports/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv
"""
import utility.downloader as downloader
import utility.convert_csv as convert_csv
import pandas as pd
import library.sightings_over_time as sightings

# Udkommenteret mens vi udvikler
""" if __name__ == '__main__':
    global file_name
    file_name = downloader.download_file() """


# Fjernes når vi aflever.
file_name = 'ufo-scrubbed-geocoded-time-standardized.csv'

data = convert_csv.convert_csv_to_dataframe(file_name)

print(sightings.ufo_sightings_over_time(data))


# Gør at vi kan printe all kolonner.
#pd.set_option('display.max_columns', None)

# Til test
#def first(data):
    # print(data.columns)
 #   print(data.info())
    # print(data)


#first(data)
