# 2018-10-10 -- dette modul er beregnet til metoder der finder den by og den stat hvor der er flest observationer:

import library.states as states
import pandas as pd

'''
RangeIndex: 80332 entries, 0 to 80331
Data columns (total 9 columns):
date_time            79638 non-null datetime64[ns]
city                 80332 non-null object
state                74535 non-null object
country              70662 non-null object
shape                78400 non-null object
duration_secounds    80332 non-null int32
comments             80317 non-null object
latitude             80332 non-null float64
longitude            80332 non-null float64
dtypes: datetime64[ns](1), float64(2), int32(1), object(5)
'''

#word_count = pd.Series(' '.join(data['overview'].astype(str)).split()).value_counts()
#most_used_words = word_count[:100]



def find_state(data):
    panda_serie = data.groupby('city').size()
    sorted = panda_serie.sort_values()
    result = sorted[sorted == sorted[-1]]#9655]
    Myindex = result.index[0]  
    # korrekt loesning:  (evt. kig efter statsnavne: states.statedict["ca"])
    print("City: " + Myindex + " has " + sorted[-1].astype('str') + " UFO sightings in total")
   
    panda_serie = data.groupby('state').size()
    sorted = panda_serie.sort_values()
    result = sorted[sorted == sorted[-1]]#9655]
    Myindex = result.index[0]  
    # korrekt loesning:  (evt. kig efter statsnavne: states.statedict["ca"])
    print("State: " + Myindex + " has " + sorted[-1].astype('str') + " UFO sightings in total")

    
    '''
    print(result)               # ca 9655
    print(type(result))         # dtype: int64  <class 'pandas.core.series.Series'>
    Myindex = result.index[0]   
    print(Myindex)              # ca
    print(type(Myindex))        # <class 'str'>
    '''