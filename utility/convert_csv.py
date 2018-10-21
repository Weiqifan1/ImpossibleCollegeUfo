import pandas as pd
from tqdm import tqdm


def convert_csv_to_dataframe(file_name):
    '''
    This method read the csv file and convert it to a dataframe.
    When it's done it change the date to a date time object and some of the columns to integers.
    '''
    # Returneres som en dataframe.
    # low_memory=False because column 5 and 9 has mixed datatypes.
    print('Convert csv file to a dataFrame.')
    for row in tqdm(file_name, total=len(file_name)): # For the progress bar.
        data = pd.read_csv(file_name, sep=',', header=None, low_memory=False, usecols=[0, 1, 2, 3, 4, 5, 7, 9, 10], names=[
                       "date_time", "city", "state", "country", "shape", "duration_secounds", "comments", "latitude", "longitude"])
    
    # Convert string to datetime
    # iterrows = iterate through DataFrame's row for the progress bar.
    print('Convert date to datetime object.')
    for index, row in tqdm(data.iterrows(), total = len(data.index)): 
        data['date_time'] = pd.to_datetime(data['date_time'], errors='coerce')
    
    # Convert string to int. to_numeric converts to float. fillna sets empty values to 0.
    # MIXED DATA TYPES!
    data['duration_secounds'] = pd.to_numeric(
        data['duration_secounds'], errors='coerce').fillna(0).astype(int)

    # MIXED DATA TYPES!
    # data['duration_minutes'] = pd.to_numeric(data['duration_minutes'], errors='coerce').fillna(0).astype(int)

    # We use fillna(0) to replace NaN with 0 so we can convert to float.
    data['latitude'] = pd.to_numeric(
        data['latitude'], errors='coerce').fillna(0).astype(float)

    return data
