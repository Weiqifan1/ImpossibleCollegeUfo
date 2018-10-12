import pandas as pd
import matplotlib.pyplot as plt
from time import strptime


def ufo_sightings_monthly(data):
    # TODO: Remove the 0 from the list.
    # TODO: Change the graf??
    # TODO: Change monthe from number to name of month. dt.strftime('%B')
    # Make an print line with result.

    count = data['date_time'].groupby(
        [data['date_time'].dt.month.rename('Month').fillna(0).astype(int)]).count()

    # print(count)

    count.plot(kind='bar')

    plot_file = 'sightings_monthly.png'
    ax = count.plot()
    plt.xticks(rotation=45)
    ax.set_title('UFO Sightings Based on Month')
    # ax.legend(loc='upper center')
    ax.set_ylabel('Number of Sightings')
    ax.grid(False)  # Get som space just below 0 on x axe.

    fig = ax.get_figure()

    # TODO: Save file in png folder.
    fig.savefig(plot_file)
    plt.show()
