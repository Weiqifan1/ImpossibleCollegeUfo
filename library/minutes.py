
import pandas as pd
import matplotlib.pyplot as plt

def ufo_minutes(data):
    second_list = data['duration_secounds'].tolist()
    clean_list = [i for i in second_list if i > 0]
    seconds_total = sum(clean_list)
    average = seconds_total // len(clean_list)
    minutes = average // 60
    seconds = average  % 60

    print("average Ufo sighting length: " + 
        str(minutes) + " minutes, " +
        str(seconds) + " seconds.")
    