# SQLAlchemy Homework - Surfs Up
## Background
### Step 1 - Climate Analysis and Exploration
+ Used Python and SQLAlchemy to do a data analysis and data exploration of the climate database provided in a [jupyter notebook](https://github.com/J3N1/UCI_Homework_Hwang/blob/master/10-SQLAlchemy_Challenge/climate_starter.ipynb) file to show:<br>
  - Precipitation Analysis<br>
    + Created a query to retrieve the last 12 months of precipitation data to show only the date and precipitation data values<br>
    + Loaded the query results into a Pandas DataFrame and set the index to the date column<br>
    + Plotted the the [results](https://github.com/J3N1/UCI_Homework_Hwang/blob/master/10-SQLAlchemy_Challenge/Images/prcp_analysis.png) using the DataFrame plot method<br>
  - Station Analysis<br>
    + Created a query to calculate the total number of stations<br>
    + Created a query to find the most active stations:<br>
      - by listing the stations in descending order<br>
      - found the minimum, maximum, average, and count of the station<br>
      - found the station with the highest number of observations<br>
    + Created a query to retrieve the last 12 months of temperature observation data(TOBS)<br>
      - filtered the results to find the station with the highest number of observations<br>
      - Plotted the the [results](https://github.com/J3N1/UCI_Homework_Hwang/blob/master/10-SQLAlchemy_Challenge/Images/tobs_histogram.png) using the DataFrame plot method<br>
### Step 2 - Climate App
+ Designed a [Flask API](https://github.com/J3N1/UCI_Homework_Hwang/blob/master/10-SQLAlchemy_Challenge/app.py) based on the queries developed with the following routes:<br>
  - / : home page which shows all the available api routes<br>
  - /api/v1.0/precipitation : shows a JSON dictionary of the precipitation dates and data <br>
  - /api/v1.0/stations : shows a JSON list of the stations from the dataset <br>
  - /api/v1.0/tobs : shows a JSON list of temperature observations for the previous years <br>
  - /api/v1.0/yyyy-mm-dd : shows a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start date<br>
  - /api/v1.0/yyyy-mm-dd/yyyy-mm-dd : shows a JSON list of the minimum temperature, the average temperature, and the maximum temperature between two dates<br>
## Bonus
### Temperature Analysis I
+ Found the average temperature in June and December and used an independent t-test to determine that the two averages are statistically significantly different.<br>
### Temperature Analysis II
+ Found the minimum, average, and maximum temperatures for a trip between 01-10-17 and 01-20-17<br>
+ Plotted the results into a [bar chart](https://github.com/J3N1/UCI_Homework_Hwang/blob/master/10-SQLAlchemy_Challenge/Images/average_temp.png) with the peak-to-peak value as the y error bar<br>
### Daily Rainfall Average
+ Calculated the rainfall per weather station using the previous year's matching dates<br>
+ Calculated the daily normals(averages for the minimum, average, and maximum temperatures)<br>
+ Created a list of dates for the trip 01-10-18 to 01-20-18 to calculate the daily normals then loaded the results into a Pandas DataFrame<br>
+ Used the daily normals data from the Pandas DataFrame to plot an [area plot](https://github.com/J3N1/UCI_Homework_Hwang/blob/master/10-SQLAlchemy_Challenge/Images/temp_area.png) 
