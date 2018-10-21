import pandas as pd
import utility.downloader as downloader
import folium as folium
import json


def usa_map_sightings(data):

    # counts sightings per state.
    count_of_sightings_pr_state = data['state'].groupby(
        [data['state']]).count()
    # print(count_of_sightings_pr_state)

    # Read in our map:
    with open("us_states.json") as json_file:
        usa_map = json.load(json_file)
        #print(usa_map)

    # Center map.
    map = folium.Map(location=[48, -102], zoom_start=3)

    map.choropleth(geo_data=usa_map, data=count_of_sightings_pr_state,
                   columns=['State', ''],
                   key_on='feature.id',
                   fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
                   legend_name='Number of UFO per State')

    map
