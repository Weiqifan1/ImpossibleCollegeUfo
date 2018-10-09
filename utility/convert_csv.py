import pandas as pd


def convert_csv_to_dataframe(file_name):
    '''
    This method read the csv file and convert it to a dataframe. 
    When it's done it change the date to a date time object and some of the columns to integers.
    '''
    # Returneres som en dataframe.
    # low_memory=False because column 5 and 9 has mixed datatypes.
    data = pd.read_csv(file_name, sep=',', header=None, low_memory=False, names=[
                       "date_time", "city", "state", "country", "shape", "duration_secounds",
                       "duration_minutes", "comments", "date_posted", "latitude", "longitude"])

# , usecols=[0, 2, 3, 7, 8, 9, 10, 14, 15, 16]

    # Convert string to datetime
    data['date_time'] = pd.to_datetime(data['date_time'], errors='coerce')
    data['date_posted'] = pd.to_datetime(data['date_posted'], errors='coerce')

    # Convert string to int. to_numeric converts to float. fillna sets empty values to 0. .fillna(0)
    # MIXED DATA TYPES!
    #data['duration_secounds'] = pd.to_numeric(
    #    data['duration_secounds'], errors='coerce').astype(int)
    
    # MIXED DATA TYPES!
    # data['duration_minutes'] = pd.to_numeric(data['duration_minutes'], errors='coerce').fillna(0).astype(int)
    
    # We use fillna(0) to replace NaN with 0 so we can convert to int.
    data['latitude'] = pd.to_numeric(data['latitude'], errors='coerce').fillna(0).astype(int)  
    data['longitude'] = pd.to_numeric(data['longitude'], errors='coerce').fillna(0).astype(int) 

    # Convert string to int and replace .
    # data['popularity'] = pd.to_numeric(data['popularity'].str.replace(
    #    '.', ''), errors='coerce').fillna(0).astype(int)

    return data
