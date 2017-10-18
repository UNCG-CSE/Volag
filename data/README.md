# Datasets
Here is a list of the datafiles used in this project along with explanations.

## Source Data Sets
Datasets that were found from outside sources.

### 2015 Flight Data
<https://www.kaggle.com/usdot/flight-delays>: this dataset contains 3 files.
* data/flight_delays_2015/airlines.csv contains the info for all the airlines in the dataset.

	| column name	| description			| data type	|
	|---------------|-----------------------|-----------|
	| IATA_CODE		| Location Identifier	| String 	|
	| AIRLINE		| Airport's Name		| String	|

* data/flight_delays_2015/airports.csv contains the info for all the airports in the dataset.

	| column name	| description			| data type	|
	|---------------|-----------------------|-----------|
	| IATA_CODE		| Location Identifier	| String 	|
	|AIRPORT|Airport's Name|String|
	| CITY | City Name of the Airport | String |
	| STATE | State Name of the Airport| String|
	| COUNTRY | Country Name of the Airport | String |
	| LATITUDE | Latitude of the Airport | Float |
	| LONGITUDE | Longitude of the Airport | Float |

* data/flight_delays_2015/flights.csv contains the info for all the flights in the dataset, this file is the bulk of the data.

    | column name	| description			| data type	|
	|---------------|-----------------------|-----------|
    |YEAR     |Year of the Flight Trip|Integer|
    |MONTH|Month of the Flight Trip|Integer|
    |DAY|Day of the Flight Trip|Integer|
    |DAY_OF_WEEK|Day of week of the Flight Trip|Integer|
    |AIRLINE|Airline Identifier|String|
    |FLIGHT_NUMBER|Flight Identifier|Integer|
    |TAIL_NUMBER|Aircraft Identifier|Integer|
    |ORIGIN_AIRPORT|Starting Airport|String|
    |DESTINATION_AIRPORT|Destination Airport|String|
    |SCHEDULED_DEPARTURE|Planned Departure Time|String|
    |DEPARTURE_TIME|WHEEL_OFF - TAXI_OUT|String|
    |DEPARTURE_DELAY|Total Delay on Depature|Integer|
    |TAXI_OUT|The time duration elapsed between departure from the origin airport gate and wheels off|Integer|
    |WHEELS_OFF|The time point that the aircraft's wheels leave the ground|String|
    |SCHEDULED_TIME|Planned time amount needed for the flight trip|Integer|
    |ELAPSED_TIME|AIR_TIME+TAXI_IN+TAXI_OFF|Integer|
    |AIR_TIME|The time duration between wheels_off and wheels_on time|Integer|
    |DISTANCE|Distance between two airports|Integer|
    |WHEELS_ON|The time point that the aircraft's wheels touch on the ground|String|
    |TAXI_IN|The time duration elapsed between wheels-on and gate arrival at the destination airport|Integer|
    |SCHEDULED_ARRIVAL|Planned arrival time|String|
    |ARRIVAL_TIME|WHEELS_ON+TAXI_IN|String|
    |ARRIVAL_DELAY|ARRIVAL_TIME-SCHEDULED_ARRIVAL|Integer|
    |DIVERTED|Aircraft landed on airport that out of schedule|Integer|
    |CANCELLED|Flight Cancelled (1 = cancelled)|Integer|
    |CANCELLATION_REASON|Reason for Cancellation of flight: A - Airline/Carrier; B - Weather; C - National Air System; D - Security|String|
    |AIR_SYSTEM_DELAY|Delay caused by air system|Integer|
    |SECURITY_DELAY|Delay caused by security|Integer|
    |AIRLINE_DELAY|Delay caused by the airline|Integer|
    |LATE_AIRCRAFT_DELAY|Delay caused by aircraft|Integer|
    |WEATHER_DELAY|Delay caused by weather|Integer|

Corrected the following rows in airports file (were missing latitude/longitude):
*ECP,Northwest Florida Beaches International Airport,Panama City,FL,USA,30.352103,-85.792960
*UST,Northeast Florida Regional Airport (St. Augustine Airport),St. Augustine,FL,USA,29.954924,-81.340138
*PBG,Plattsburgh International Airport,Plattsburgh,NY,USA,44.655571,-73.466823

### 2015 NOAA Daily Weather Data
* data/weather/stations.csv this dataset is on bigquery <https://cloud.google.com/bigquery/public-data/noaa-gsod>. Stations.csv this dataset contains the list of stations and can be retrieved with the following query
	```sql
	SELECT * FROM [bigquery-public-data:noaa_gsod.stations]
	```

	| column name	| description			| data type	|
	|---------------|-----------------------|-----------|
	|usaf|Air Force station ID|STRING|
	|wban|NCDC WBAN number|STRING|
	|name|Station Name|STRING|
	|country|FIPS country ID|STRING|
	|state|State for US stations|STRING|
	|call||STRING|
	|lat|Latitude in thousandths of decimal degrees|FLOAT|
	|lon|Longitude in thousandths of decimal degrees|FLOAT|
	|elev|Elevation in meters|STRING|
	|begin|Beginning Period Of Record|STRING|
	|end|Ending Period Of Record|STRING|

