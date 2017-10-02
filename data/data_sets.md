# Datasets
Here is a list of the datasets used in the project.

## data/flight_delays_2015/
<https://www.kaggle.com/usdot/flight-delays>: this dataset contains 3 files
* airlines.csv contains the info for all the airlines in the dataset.
* airports.csv contains the info for all the airports in the dataset.
* flights.csv contains the info for all the flights in the dataset, this file is the bulk of the data.

Corrected the following rows in airports file (were missing latitude/longitude):
*ECP,Northwest Florida Beaches International Airport,Panama City,FL,USA,30.352103,-85.792960
*UST,Northeast Florida Regional Airport (St. Augustine Airport),St. Augustine,FL,USA,29.954924,-81.340138
*PBG,Plattsburgh International Airport,Plattsburgh,NY,USA,44.655571,-73.466823

## data/weather/
<https://cloud.google.com/bigquery/public-data/noaa-gsod>: this dataset is on bigquery.
* stations.csv this dataset contains the list of stations and can be retrieved with the following query

```sql
SELECT * FROM [bigquery-public-data:noaa_gsod.stations]
```