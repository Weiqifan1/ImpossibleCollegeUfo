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
    # data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')

    # Convert string to int. to_numeric converts to float. fillna sets empty values to 0.
    # data['budget'] = pd.to_numeric(data['budget'], errors='coerce').fillna(0).astype(int)
    # data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce').fillna(0).astype(int)
    # data['runtime'] = pd.to_numeric(data['runtime'], errors='coerce').fillna(0).astype(int)

    # Convert string to int and replace .
    # data['popularity'] = pd.to_numeric(data['popularity'].str.replace(
    #    '.', ''), errors='coerce').fillna(0).astype(int)

    return data
