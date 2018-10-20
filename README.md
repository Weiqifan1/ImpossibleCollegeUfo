# ImpossibleCollegeUfo

## Documentation
Analyzine the ufo dataset from the group Impossible College. It is a collection og more than 80000 of ufo sightings mainly in USA.  
This is the link to the assignment:  
https://github.com/BoMarconiHenriksen/impossibleCollegeDataset  

## Group
Anders Nissen, Christian Lykke and Bo Henriksen.  

## How to run the project
1. Clone the project  
2. Cd into the directory of the project  
3. To run the project you need to paste this url to the dataset as a parameter 
https://raw.githubusercontent.com/planetsig/ufo-reports/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv  

4. Example of how to run the project:  
5. python main.py [<url_to_dataset>]  

## Dependencies
The project use dependencies which is part of Pythons Anaconda installation and TextBlob.  
Install TextBlob with: pip install -U textblob  
Instal folium with: pip install folium  

## Results
#### Which place are there most UFO sightings?  
Seattle has 525 UFO sightings in total (city).  
California has 9655 UFO sightings in total (state).  

#### How have the UFO sightings evoled over time (It's fine to answer this question with a plot)?  
Make the image wider to better see the dates when you have cloned the repository.  

<img src="https://github.com/Weiqifan1/ImpossibleCollegeUfo/blob/developer/sightings_over_time.png" width="1000">

#### Which time of the year are there most UFO sightings?  
July has the most UFO sightings.  

![alt text](https://github.com/Weiqifan1/ImpossibleCollegeUfo/blob/developer/sightings_monthly.png)  

#### How does a UFO look like?   
![alt text](https://github.com/Weiqifan1/ImpossibleCollegeUfo/blob/developer/Ufo_shapes.png) 

#### For how long could the sightings been seen (avarage)?  
Average Ufo sighting length: 150 minutes, 27 seconds.  

#### Plot 1.  
Which days are most likely to see a UFO?  
x is monday to sunday.  
y is 1 to 0.  

![alt text](https://github.com/Weiqifan1/ImpossibleCollegeUfo/blob/developer/Ufo_week_days.png)

#### Plot 2.  
Make a graph with polarity and sentiment.  
x in the plot is index with sightings.  
y in the plot is 0 to 1.  


#### Plot 3.  
Make a plot which shows the number of sightings in USA per state and colour code it. Dark colour indicates many sightings and ligh colour indicates few sightings.  
