import pandas as pd
import matplotlib.pyplot as plt


def ufo_sightings_over_time(data):
    
    count = data['date_time'].groupby(
        [data['date_time'].dt.year.rename('Year').fillna(0).astype(int)]).count()

    count.plot(kind='bar')

    plot_file = 'sightings_over_time.png'
    ax = count.plot()
    plt.xticks(rotation=45)
    ax.set_title('UFO Sightings Over Time')
    ax.set_ylabel('Number of Sightings')
    ax.grid(False)  # Get som space just below 0 on x axe.

    fig = ax.get_figure()

    # Save file.
    fig.savefig(plot_file)
 