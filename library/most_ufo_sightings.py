# 2018-10-10 -- dette modul er beregnet til metoder der finder den by og den stat hvor der er flest observationer:

import library.states as states
import pandas as pd

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
