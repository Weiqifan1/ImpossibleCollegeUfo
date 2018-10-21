import pandas as pd
import matplotlib.pyplot as plt
from time import strptime


def ufo_sightings_monthly(data):

    count = data['date_time'].groupby(
        [data['date_time'].dt.month.rename('Month').fillna(0).astype(int)]).count()

    count.plot(kind='bar')

    plot_file = 'sightings_monthly.png'
    ax = count.plot()
    plt.xticks(rotation=45)
    ax.set_title('UFO Sightings Based on Month')
    ax.set_ylabel('Number of Sightings')
    ax.grid(False)  # Get som space just below 0 on x axe.

    fig = ax.get_figure()

    # Save file
    fig.savefig(plot_file)
