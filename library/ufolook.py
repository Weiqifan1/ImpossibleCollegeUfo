import pandas as pd
import matplotlib.pyplot as plt

def ufolook(data):
    shapelist = data['shape'].tolist()
    mydict = _enumerate(shapelist)
    num_of_shapes = sum(mydict.values())
    chart_limmit = num_of_shapes/40
    mydict = _remove_rare_shapes(mydict, chart_limmit)
    
    valuelist = sorted(list(mydict.values()))
    keylist = _get_keys_from_values(valuelist, mydict)
    too_few = num_of_shapes - sum(valuelist)
    
    valuelist.append(too_few)
    keylist.append("too_few_to_show")
    _save_piechart(valuelist, keylist)
   
def _save_piechart(valuelist, keylist):
    ufopie = plt.subplot()
    ufopie.pie(valuelist, labels=tuple(keylist), autopct='%1.1f',
        shadow=False, startangle=90)
    ufopie.axis('equal')
    plt.title("Ufo shape percentages")
    plot_file = 'Ufo_shapes.png'
    fig = ufopie.get_figure()
    fig.savefig(plot_file)

def _enumerate(nameList):
    nameApear = {}
    for word in nameList:
        nameApear.setdefault(word, 0)
        nameApear[word] += 1
    return nameApear

def _remove_rare_shapes(shape_dict, limmit):
    return { k:v for k, v in shape_dict.items() if v > limmit}

def _get_keys_from_values(value_list, dict):
    keylist = []
    for value in value_list:
        key = [k for k,v in dict.items() if v == value]
        keylist.append(key[0])
    return keylist