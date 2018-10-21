
import pandas as pd
import matplotlib.pyplot as plt
import math

def week_graf(data):
    print("weekday")

    daylist = data['date_time'].dt.dayofweek.tolist()
    daydict = _enumerate(daylist)

    valuelist = sorted(list(daydict.values()))
    keylist = _get_keys_from_values(valuelist, daydict)
    day_names = _float_to_day(keylist)

    _save_piechart(valuelist, day_names)
   
def _float_to_day(float_list):
    index = [int(i) for i in float_list]
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]
    return [weekdays[i] for i in index]


def _save_piechart(valuelist, keylist):
    ufopie = plt.subplot()
    ufopie.pie(valuelist, labels=tuple(keylist), autopct='%1.2f',
        shadow=False, startangle=90)
    ufopie.axis('equal')
    plt.title("Ufo's by weekday in pct (avg = 14.286%)")
    plot_file = 'Ufo_week_days.png'
    fig = ufopie.get_figure()
    fig.savefig(plot_file)


def _enumerate(week_days):
    week_day_dict = {}
    for day in week_days:
        if not math.isnan(day):
            week_day_dict.setdefault(day, 0)
            week_day_dict[day] += 1
    return week_day_dict


def _get_keys_from_values(value_list, dict):
    keylist = []
    for value in value_list:
        key = [k for k,v in dict.items() if v == value]
        keylist.append(key[0])
    return keylist
    