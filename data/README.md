# Datasets
Here is a list of the datafiles used in this project along with explanations.

## Source Data Sets
Datasets that were found from outside sources.

### 2015 Flight Data
<https://www.kaggle.com/usdot/flight-delays>: this dataset contains 3 files.
* data/flight_delays_2015/airlines.csv contains the info for all the airlines in the dataset.

	| column name	| description			| data type	|
	|---------------|-----------------------|-----------|
	| IATA_CODE		| Location Identifier	| STRING 	|
	| AIRLINE		| Airport's Name		| STRING	|

* data/flight_delays_2015/airports.csv contains the info for all the airports in the dataset.

	| column name	| description			| data type	|
	|---------------|-----------------------|-----------|
	| IATA_CODE		| Location Identifier	| STRING 	|
	|AIRPORT|Airport's Name|STRING|
	| CITY | City Name of the Airport | STRING |
	| STATE | State Name of the Airport| STRING|
	| COUNTRY | Country Name of the Airport | STRING |
	| LATITUDE | Latitude of the Airport | FLOAT |
	| LONGITUDE | Longitude of the Airport | FLOAT |

    Suggested read statement:
    ```python
    dtypes = {
        'usaf': 'str',
        'wban': 'str'
    }
    airports_df = pd.read_csv('../data/flight_delays_2015/airports.csv', low_memory=False, dtype=dtypes)
    ```

* data/flight_delays_2015/flights.csv contains the info for all the flights in the dataset, this file is the bulk of the data.

    | column name	| description			| data type	|
	|---------------|-----------------------|-----------|
    |YEAR     |Year of the Flight Trip|INTEGER|
    |MONTH|Month of the Flight Trip|INTEGER|
    |DAY|Day of the Flight Trip|INTEGER|
    |DAY_OF_WEEK|Day of week of the Flight Trip|INTEGER|
    |AIRLINE|Airline Identifier|STRING|
    |FLIGHT_NUMBER|Flight Identifier|INTEGER|
    |TAIL_NUMBER|Aircraft Identifier|INTEGER|
    |ORIGIN_AIRPORT|Starting Airport|STRING|
    |DESTINATION_AIRPORT|Destination Airport|STRING|
    |SCHEDULED_DEPARTURE|Planned Departure Time|STRING|
    |DEPARTURE_TIME|WHEEL_OFF - TAXI_OUT|STRING|
    |DEPARTURE_DELAY|Total Delay on Depature|INTEGER|
    |TAXI_OUT|The time duration elapsed between departure from the origin airport gate and wheels off|INTEGER|
    |WHEELS_OFF|The time point that the aircraft's wheels leave the ground|STRING|
    |SCHEDULED_TIME|Planned time amount needed for the flight trip|INTEGER|
    |ELAPSED_TIME|AIR_TIME+TAXI_IN+TAXI_OFF|INTEGER|
    |AIR_TIME|The time duration between wheels_off and wheels_on time|INTEGER|
    |DISTANCE|Distance between two airports|INTEGER|
    |WHEELS_ON|The time point that the aircraft's wheels touch on the ground|STRING|
    |TAXI_IN|The time duration elapsed between wheels-on and gate arrival at the destination airport|INTEGER|
    |SCHEDULED_ARRIVAL|Planned arrival time|STRING|
    |ARRIVAL_TIME|WHEELS_ON+TAXI_IN|STRING|
    |ARRIVAL_DELAY|ARRIVAL_TIME-SCHEDULED_ARRIVAL|INTEGER|
    |DIVERTED|Aircraft landed on airport that out of schedule|INTEGER|
    |CANCELLED|Flight Cancelled (1 = cancelled)|INTEGER|
    |CANCELLATION_REASON|Reason for Cancellation of flight: A - Airline/Carrier; B - Weather; C - National Air System; D - Security|STRING|
    |AIR_SYSTEM_DELAY|Delay caused by air system|INTEGER|
    |SECURITY_DELAY|Delay caused by security|INTEGER|
    |AIRLINE_DELAY|Delay caused by the airline|INTEGER|
    |LATE_AIRCRAFT_DELAY|Delay caused by aircraft|INTEGER|
    |WEATHER_DELAY|Delay caused by weather|INTEGER|

    Corrected the following rows in airports file (were missing latitude/longitude):
    *ECP,Northwest Florida Beaches International Airport,Panama City,FL,USA,30.352103,-85.792960
    *UST,Northeast Florida Regional Airport (St. Augustine Airport),St. Augustine,FL,USA,29.954924,-81.340138
    *PBG,Plattsburgh International Airport,Plattsburgh,NY,USA,44.655571,-73.466823

    Suggested read statement:
    ```python
    dtypes = {
        'SCHEDULED_DEPARTURE': 'str',
        'DEPARTURE_TIME': 'str',
        'WHEELS_OFF': 'str',
        'WHEELS_ON': 'str',
        'SCHEDULED_ARRIVAL': 'str',
        'ARRIVAL_TIME': 'str'
    }
    flights_df = pd.read_csv('../data/flight_delays_2015/flights.csv', dtype=dtypes)
    ```
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

    Suggested read statement:
    ```python
    dtypes = {
        'usaf': 'str',
        'wban': 'str'
    }
    stations_df = pd.read_csv('../data/weather/stations.csv', dtype=dtypes)
    ```

* data/weather/weather_merged.csv was created by merging all the files located at <ftp://ftp.ncdc.noaa.gov/pub/data/gsod/2015/gsod_2015.tar> into a single file. The station columns were merged to create a single station identifier.

    | column name	| description			| data type	|
	|---------------|-----------------------|-----------|
    |STATION|This is the USAF and WBAN numbers concatenated and seperated by a '-'.|STRING|
    |YEARMODA|The Date of the weather observation|STRING|
    |TEMP|Mean temperature for the day in degrees Fahrenheit to tenths. Missing = 9999.9|FLOAT|
    |COUNT_TEMP|Number of observations used in calculating mean temperature|INTEGER|
    |DEWP|Mean dew point for the day in degreesm Fahrenheit to tenths.  Missing = 9999.9|FLOAT|
    |COUNT_DEWP|Number of observations used in calculating mean dew point|INTEGER|
    |SLP|Mean sea level pressure for the day in millibars to tenths. Missing = 9999.9|FLOAT|
    |COUNT_SLP|Number of observations used in calculating mean sea level pressure|INTEGER|
    |STP|Mean station pressure for the day in millibars to tenths. Missing = 9999.9|FLOAT|
    |COUNT_STP|Number of observations used in calculating mean station pressure|INTEGER|
    |VISIB|Mean visibility for the day in miles to tenths.  Missing = 999.9|FLOAT|
    |COUNT_VISIB|Number of observations used in calculating mean visibility|INTEGER|
    |WDSP|Mean wind speed for the day in knots to tenths. Missing = 999.9|STRING|
    |COUNT_WDSP|Number of observations used in calculating mean wind speed|STRING|
    |MXSPD|Maximum sustained wind speed reported for the day in knots to tenths. Missing = 999.9|STRING|
    |GUST|Maximum wind gust reported for the day in knots to tenths. Missing = 999.9|FLOAT|
    |MAX|Maximum temperature reported during the day in Fahrenheit to tenths--time of max temp report varies by country and region, so this will sometimes not be the max for the calendar day. Missing = 9999.9. * indicates max temp was  derived from the hourly data (i.e., highest hourly or synoptic-reported temperature) otherwise max temp was taken from the explicit max temp report and not from the 'hourly' data.|STRING|
    |MIN|Minimum temperature reported during the day in Fahrenheit to tenths--time of min temp report varies by country and region, so this will sometimes not be the min for the calendar day. Missing = 9999.9* indicates min temp was  derived from the hourly data (i.e., lowest hourly or synoptic-reported temperature) otherwise min temp was taken from the explicit min temp report and not from the 'hourly' data.|STRING|
    |PRCP|Total precipitation (rain and/or melted snow) reported during the day in inches and hundredths; will usually not end with the midnight observation--i.e., may include latter part of previous day. .00 indicates no measurable precipitation (includes a trace). Missing = 99.99 Note: Many stations do not report '0' on days with no precipitation--therefore, '99.99' will often appear on these days. Also, for example, a station may only report a 6-hour amount for the period during which rain fell. See Flag field for source of data. A flag is also appended that means: A = 1 report of 6-hour precipitation amount B = Summation of 2 reports of 6-hour precipitation amount C = Summation of 3 reports of 6-hour precipitation amount D = Summation of 4 reports of 6-hour precipitation amount E = 1 report of 12-hour precipitation amount F = Summation of 2 reports of 12-hour precipitation amount G = 1 report of 24-hour precipitation amount H = Station reported '0' as the amount for the day (eg, from 6-hour reports), but also reported at least one occurrence of precipitation in hourly observations--this could indicate a trace occurred, but should be considered as incomplete data for the day. I = Station did not report any precip data for the day and did not report any occurrences of precipitation in its hourly observations--it's still possible that precip occurred but was not reported|STRING|
    |SNDP|Snow depth in inches to tenths--last report for the day if reported more thanonce. Missing = 999.9 Note: Most stations do not report '0' ondays with no snow on the ground--therefore, '999.9' will often appear on these days|FLOAT|
    |FRESHTT|A 6 character field where each character is a indicator for the following events 1. fog 2. rain or drizzle 3. snow, ice or pellets 4. hail 5. thunder 6. tornado, funnel or cloud. The meaning of each is 1 = yes, 0 = no/not reported.|STRING|
    
    Suggested read statement:
    ```python
    dtypes = {
        'STATION': 'str',
        'FRSHTT': 'str'
    }
    weather_df= pd.read_csv('../data/weather/weather_merged.csv', dtype=dtypes, parse_dates=['YEARMODA'])
    ```

## Generated Data Files
* data/weather/weather_merged.csv - This file contains the flight data merged with the NOAA weather data for origin and destination. This file is generated in the data_munging.ipynb notebook. Columns that begin with 'OR_' are for the origin airport and columns that begin with 'DES_' are for the destination airport.
    
    | column name	| description			| data type	|
	|---------------|-----------------------|-----------|
    |YEAR|Year of the Flight Trip|INTEGER|
    |MONTH|Month of the Flight Trip|INTEGER|
    |DAY|Day of the Flight Trip|INTEGER|
    |DAY_OF_WEEK|Day of week of the Flight Trip|INTEGER|
    |AIRLINE|Airline Identifier|STRING|
    |FLIGHT_NUMBER|Flight Identifier|INTEGER|
    |TAIL_NUMBER|Aircraft Identifier|INTEGER|
    |ORIGIN_AIRPORT|Starting Airport|STRING|
    |DESTINATION_AIRPORT|Destination Airport|STRING|
    |SCHEDULED_DEPARTURE|Planned Departure Time|STRING|
    |DEPARTURE_TIME|WHEEL_OFF - TAXI_OUT|String|
    |DEPARTURE_DELAY|Total Delay on Depature|INTEGER|
    |TAXI_OUT|The time duration elapsed between departure from the origin airport gate and wheels off|INTEGER|
    |WHEELS_OFF|The time point that the aircraft's wheels leave the ground|STRING|
    |SCHEDULED_TIME|Planned time amount needed for the flight trip|INTEGER|
    |ELAPSED_TIME|AIR_TIME+TAXI_IN+TAXI_OFF|INTEGER|
    |AIR_TIME|The time duration between wheels_off and wheels_on time|INTEGER|
    |DISTANCE|Distance between two airports|INTEGER|
    |WHEELS_ON|The time point that the aircraft's wheels touch on the ground|STRING|
    |TAXI_IN|The time duration elapsed between wheels-on and gate arrival at the destination airport|INTEGER|
    |SCHEDULED_ARRIVAL|Planned arrival time|STRING|
    |ARRIVAL_TIME|WHEELS_ON+TAXI_IN|STRING|
    |ARRIVAL_DELAY|ARRIVAL_TIME-SCHEDULED_ARRIVAL|INTEGER|
    |DIVERTED|Aircraft landed on airport that out of schedule|INTEGER|
    |CANCELLED|Flight Cancelled (1 = cancelled)|INTEGER|
    |CANCELLATION_REASON|Reason for Cancellation of flight: A - Airline/Carrier; B - Weather; C - National Air System; D - Security|STRING|
    |AIR_SYSTEM_DELAY|Delay caused by air system|INTEGER|
    |SECURITY_DELAY|Delay caused by security|INTEGER|
    |AIRLINE_DELAY|Delay caused by the airline|INTEGER|
    |LATE_AIRCRAFT_DELAY|Delay caused by aircraft|INTEGER|
    |WEATHER_DELAY|Delay caused by weather|INTEGER|
    |DATE|Date of the flight|DATE|
    |origin_weather_station|Weather station closest to origin airport|STRING|
    |destination_weather_station|Weather station closest to destination airport.|STRING|
    |OR_TEMP|Mean temperature for the day in degrees Fahrenheit to tenths. Missing = 9999.9|FLOAT|
    |OR_COUNT_TEMP|Number of observations used in calculating mean temperature|INTEGER|
    |OR_DEWP|Mean dew point for the day in degreesm Fahrenheit to tenths.  Missing = 9999.9|FLOAT|
    |OR_COUNT_DEWP|Number of observations used in calculating mean dew point|INTEGER|
    |OR_SLP|Mean sea level pressure for the day in millibars to tenths. Missing = 9999.9|FLOAT|
    |OR_COUNT_SLP|Number of observations used in calculating mean sea level pressure|INTEGER|
    |OR_STP|Mean station pressure for the day in millibars to tenths. Missing = 9999.9|FLOAT|
    |OR_COUNT_STP|Number of observations used in calculating mean station pressure|INTEGER|
    |OR_VISIB|Mean visibility for the day in miles to tenths.  Missing = 999.9|FLOAT|
    |OR_COUNT_VISIB|Number of observations used in calculating mean visibility|INTEGER|
    |OR_WDSP|Mean wind speed for the day in knots to tenths. Missing = 999.9|STRING|
    |OR_COUNT_WDSP|Number of observations used in calculating mean wind speed|STRING|
    |OR_MXSPD|Maximum sustained wind speed reported for the day in knots to tenths. Missing = 999.9|STRING|
    |OR_GUST|Maximum wind gust reported for the day in knots to tenths. Missing = 999.9|FLOAT|
    |OR_MAX|Maximum temperature reported during the day in Fahrenheit to tenths--time of max temp report varies by country and region, so this will sometimes not be the max for the calendar day. Missing = 9999.9. * indicates max temp was  derived from the hourly data (i.e., highest hourly or synoptic-reported temperature) otherwise max temp was taken from the explicit max temp report and not from the 'hourly' data.|STRING|
    |OR_MIN|Minimum temperature reported during the day in Fahrenheit to tenths--time of min temp report varies by country and region, so this will sometimes not be the min for the calendar day. Missing = 9999.9* indicates min temp was  derived from the hourly data (i.e., lowest hourly or synoptic-reported temperature) otherwise min temp was taken from the explicit min temp report and not from the 'hourly' data.|STRING|
    |OR_PRCP|Total precipitation (rain and/or melted snow) reported during the day in inches and hundredths; will usually not end with the midnight observation--i.e., may include latter part of previous day. .00 indicates no measurable precipitation (includes a trace). Missing = 99.99 Note: Many stations do not report '0' on days with no precipitation--therefore, '99.99' will often appear on these days. Also, for example, a station may only report a 6-hour amount for the period during which rain fell. See Flag field for source of data. A flag is also appended that means: A = 1 report of 6-hour precipitation amount B = Summation of 2 reports of 6-hour precipitation amount C = Summation of 3 reports of 6-hour precipitation amount D = Summation of 4 reports of 6-hour precipitation amount E = 1 report of 12-hour precipitation amount F = Summation of 2 reports of 12-hour precipitation amount G = 1 report of 24-hour precipitation amount H = Station reported '0' as the amount for the day (eg, from 6-hour reports), but also reported at least one occurrence of precipitation in hourly observations--this could indicate a trace occurred, but should be considered as incomplete data for the day. I = Station did not report any precip data for the day and did not report any occurrences of precipitation in its hourly observations--it's still possible that precip occurred but was not reported|STRING|
    |OR_SNDP|Snow depth in inches to tenths--last report for the day if reported more thanonce. Missing = 999.9 Note: Most stations do not report '0' ondays with no snow on the ground--therefore, '999.9' will often appear on these days|FLOAT|
    |OR_FRESHTT|A 6 character field where each character is a indicator for the following events 1. fog 2. rain or drizzle 3. snow, ice or pellets 4. hail 5. thunder 6. tornado, funnel or cloud. The meaning of each is 1 = yes, 0 = no/not reported.|STRING|
    |DES_TEMP|Mean temperature for the day in degrees Fahrenheit to tenths. Missing = 9999.9|FLOAT|
    |DES_COUNT_TEMP|Number of observations used in calculating mean temperature|INTEGER|
    |DES_DEWP|Mean dew point for the day in degreesm Fahrenheit to tenths.  Missing = 9999.9|FLOAT|
    |DES_COUNT_DEWP|Number of observations used in calculating mean dew point|INTEGER|
    |DES_SLP|Mean sea level pressure for the day in millibars to tenths. Missing = 9999.9|FLOAT|
    |DES_COUNT_SLP|Number of observations used in calculating mean sea level pressure|INTEGER|
    |DES_STP|Mean station pressure for the day in millibars to tenths. Missing = 9999.9|FLOAT|
    |DES_COUNT_STP|Number of observations used in calculating mean station pressure|INTEGER|
    |DES_VISIB|Mean visibility for the day in miles to tenths.  Missing = 999.9|FLOAT|
    |DES_COUNT_VISIB|Number of observations used in calculating mean visibility|INTEGER|
    |DES_WDSP|Mean wind speed for the day in knots to tenths. Missing = 999.9|STRING|
    |DES_COUNT_WDSP|Number of observations used in calculating mean wind speed|STRING|
    |DES_MXSPD|Maximum sustained wind speed reported for the day in knots to tenths. Missing = 999.9|STRING|
    |DES_GUST|Maximum wind gust reported for the day in knots to tenths. Missing = 999.9|FLOAT|
    |DES_MAX|Maximum temperature reported during the day in Fahrenheit to tenths--time of max temp report varies by country and region, so this will sometimes not be the max for the calendar day. Missing = 9999.9. * indicates max temp was  derived from the hourly data (i.e., highest hourly or synoptic-reported temperature) otherwise max temp was taken from the explicit max temp report and not from the 'hourly' data.|STRING|
    |DES_MIN|Minimum temperature reported during the day in Fahrenheit to tenths--time of min temp report varies by country and region, so this will sometimes not be the min for the calendar day. Missing = 9999.9* indicates min temp was  derived from the hourly data (i.e., lowest hourly or synoptic-reported temperature) otherwise min temp was taken from the explicit min temp report and not from the 'hourly' data.|STRING|
    |DES_PRCP|Total precipitation (rain and/or melted snow) reported during the day in inches and hundredths; will usually not end with the midnight observation--i.e., may include latter part of previous day. .00 indicates no measurable precipitation (includes a trace). Missing = 99.99 Note: Many stations do not report '0' on days with no precipitation--therefore, '99.99' will often appear on these days. Also, for example, a station may only report a 6-hour amount for the period during which rain fell. See Flag field for source of data. A flag is also appended that means: A = 1 report of 6-hour precipitation amount B = Summation of 2 reports of 6-hour precipitation amount C = Summation of 3 reports of 6-hour precipitation amount D = Summation of 4 reports of 6-hour precipitation amount E = 1 report of 12-hour precipitation amount F = Summation of 2 reports of 12-hour precipitation amount G = 1 report of 24-hour precipitation amount H = Station reported '0' as the amount for the day (eg, from 6-hour reports), but also reported at least one occurrence of precipitation in hourly observations--this could indicate a trace occurred, but should be considered as incomplete data for the day. I = Station did not report any precip data for the day and did not report any occurrences of precipitation in its hourly observations--it's still possible that precip occurred but was not reported|STRING|
    |DES_SNDP|Snow depth in inches to tenths--last report for the day if reported more thanonce. Missing = 999.9 Note: Most stations do not report '0' ondays with no snow on the ground--therefore, '999.9' will often appear on these days|FLOAT|
    |DES_FRESHTT|A 6 character field where each character is a indicator for the following events 1. fog 2. rain or drizzle 3. snow, ice or pellets 4. hail 5. thunder 6. tornado, funnel or cloud. The meaning of each is 1 = yes, 0 = no/not reported.|STRING|  
    |OR_FOG|Indicator for the occurrence of fog during the day|BOOLEAN|
    |OR_RAIN_DRIZZLE|Indicator for the occurrence of rain or drizzle during the day|BOOLEAN|
    |OR_SNOW_ICE_PELLETS|Indicator for the occurrence of snow, ice or pellets during the day|BOOLEAN|
    |OR_HAIL|Indicator for the occurrence of hail during the day|BOOLEAN|
    |OR_THUNDER|Indicator for the occurrence of thunder during the day|BOOLEAN|
    |OR_TORNADO_FUNNEL_CLOUD|Indicator for the occurrence of tornado or funnel clouds during the day|BOOLEAN|
    |DES_FOG|Indicator for the occurrence of fog during the day|BOOLEAN|
    |DES_RAIN_DRIZZLE|Indicator for the occurrence of rain or drizzle during the day|BOOLEAN|
    |DES_SNOW_ICE_PELLETS|Indicator for the occurrence of snow, ice or pellets during the day|BOOLEAN|
    |DES_HAIL|Indicator for the occurrence of hail during the day|BOOLEAN|
    |DES_THUNDER|Indicator for the occurrence of thunder during the day|BOOLEAN|
    |DES_TORNADO_FUNNEL_CLOUD|Indicator for the occurrence of tornado or funnel clouds during the day|BOOLEAN|

    Suggested read statement:
    ```python
    dtypes = {
        'ORIGIN_AIRPORT': 'str', 
        'DESTINATION_AIRPORT': 'str', 
        'IATA_CODE_x': 'str', 
        'origin_weather_station': 'str', 
        'IATA_CODE_y': 'str', 
        'destination_weather_station': 'str', 
        'OR_MAX': 'str', 
        'OR_MIN': 'str', 
        'OR_PRCP': 'str', 
        'DES_MAX': 'str', 
        'DES_MIN': 'str', 
        'DES_PRCP': 'str', 
        'OR_FRSHTT': 'str', 
        'DES_FRSHTT': 'str'
    }
    flights_merged_df= pd.read_csv('../data/flight_delays_2015/flights_weather.csv', dtype=dtypes, parse_dates=['DATE'])
    ```