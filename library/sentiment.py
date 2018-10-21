
# to run this code, open gitbash and write the command: conda install -c conda-forge textblob
# (see https://anaconda.org/conda-forge/textblob)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

def create_pol(mytext):
    polarity_value = TextBlob(mytext).sentiment.polarity
    #return polarity_value such that it goes form 0 to 1 instead of -1 to 1
    return (polarity_value+1)/2

def create_sen(mytext):
    return TextBlob(mytext).sentiment.subjectivity

def senttiment_info(data):
    
    data["polarity"] = data.apply (lambda row: create_pol(str(row.comments)),axis=1)#TextBlob(data['comments']).sentiment.polarity
    data["subjectivity"] = data.apply (lambda row: create_sen(str(row.comments)),axis=1)#TextBlob(data['comments']).sentiment.subjectivity
    subset = data[["subjectivity", "polarity"]]
    draw(subset)

    #frameList = np.array_split(hello, 10)
    #df = pd.concat([frameList[0].mean(), frameList[1].mean(), frameList[2].mean()], axis=1).reset_index()
    #df.T # dette burde dreje dataframen 90 grader, men det sker ikke ?!
    #print(type(df))
    #print(len(df))
    #print(df.head())


def draw(subset):   
    plot_file = 'sentiment.png'
    ax = subset.plot()
    ax.set_title('UFO Sightings sentiment')
    ax.set_xlabel('sighting index')
    ax.set_ylabel('polarity: negative(0) vs. positive(1)\nsubjectivity: objective(0) vs. subjective(1)')
    fig = ax.get_figure()
    fig.savefig(plot_file)
    
