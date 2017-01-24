# Rain Drop, Drip Drop - UC Davis Water Consumption Project
## Winner of "Best use of Esri ArcGIS Platform" at HackDavis 2017

This project provides a data visualization tool to see real-time water-consumption analysis for UC Davis buildings. The project uses Osisoft on campus sensor data to provide a unique way of seeing higher or lower water consumption from the moment the map is loaded in comparison to last week's data. 

We utilized the ArcGis developer platform to visualize the change in consumption using opacity renderers. Once you click on the map, it will approximately take 30 to 40 seconds for the points to load (this is due to an insane amount of API calls being placed to Osisoft's API). 

### To Run: 

``` bash
export FLASK_APP = hello.py
flask run
```
