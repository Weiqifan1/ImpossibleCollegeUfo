
# 2018-10-10 -- dette modul er beregnet til metoder der finder den by og den stat hvor der er flest observationer:

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
    print(2+2)
    panda_serie = data.groupby('state').size()
    #result = "" + panda_serie.sort_values()[-1]
    print(result)
    print(type(panda_serie))