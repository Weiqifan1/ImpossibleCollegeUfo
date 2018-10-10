import pandas as pd


def convert_csv_to_dataframe(file_name):
    '''
    This method read the csv file and convert it to a dataframe.
    When it's done it change the date to a date time object and some of the columns to integers.
    '''
    # Returneres som en dataframe.
    # low_memory=False because column 5 and 9 has mixed datatypes.
    data = pd.read_csv(file_name, sep=',', header=None, low_memory=False, usecols=[0, 1, 2, 3, 4, 5, 7, 9, 10], names=[
                       "date_time", "city", "state", "country", "shape", "duration_secounds", "comments", "latitude", "longitude"])

    # Convert string to datetime
    # SKAL INDKOMMENTERES NÅR VI SKAL ARBEJDE MED DATOER!!!
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

    # data['longitude'] = pd.to_numeric(
    #  data['longitude'], errors='coerce').fillna(0).astype(int)

    # Convert string to int and replace .
    # data['popularity'] = pd.to_numeric(data['popularity'].str.replace(
    #    '.', ''), errors='coerce').fillna(0).astype(int)

    return data
