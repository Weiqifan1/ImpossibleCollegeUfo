
import csv
import os.path
import sys
from lib.downloader import downloader
import pandas as pd
import os

#https://www.datacamp.com/community/tutorials/pandas-read-csv

if __name__ == "__main__":
    try:
        _, url, file_name = sys.argv
    except:
        try:
            _, url, = sys.argv
            file_name = os.path.basename(url)
            downloader(url, file_name)
        except Exception as e:
            print("Something went wrong.. : ", e)
            sys.exit(1)

    # download file from given url as file_name
    #downloader(url, file_name)

    #movies_metadata = pd.read_csv(file_name, low_memory=False, error_bad_lines=False)
    
    #pd.read_csv(file_name,  sep=',', delimiter=None, header= None, low_memory=False, error_bad_lines=False)

    #data = csv.reader(file_name)
    #data = pd.read_csv(file_name, sep=',',usecols=[0, 2, 3, 7, 8, 9, 10], low_memory=False) 
    #usecols=[0, 2, 3, 7, 8, 9, 10]

    data = pd.read_csv(file_name,  engine='python', sep= 'default', header=None, error_bad_lines=False) 
    # nrows=11, 

    print(data.info())

    #help(pd.read_csv)









# old main
'''

import lib.downloader as downloader
import lib.convert_csv as convert_csv
#import library.popular_danish_movie as popular_danish_movie
#import library.english_action_movie as english_action_movie
#import library.plot_reliase_and_runtime as reliase_and_runtime
#import library.plot_adult_movies as plot_adult_movies
#import library.buzz_words as buzz_words
#import library.animated_movies as animated_movies
#import library.highest_budget as highest_budget

# kør programmet:
# python main.py 
# https://github.com/planetsig/ufo-reports/blob/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv

#eller
# https://www.kaggle.com/NUFORC/ufo-sightings#complete.csv

if __name__ == '__main__':
    global file_name
    file_name = downloader.download_file()

data = convert_csv.convert_csv_to_dataframe(file_name)

print("hello chr")

'''


# end