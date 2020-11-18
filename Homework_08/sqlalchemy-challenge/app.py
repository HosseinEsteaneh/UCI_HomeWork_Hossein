import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt

##############################################################
# Database Setup
##############################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save the references to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session
session = Session(engine)

##############################################################
# Flask Setup
##############################################################

app = Flask(__name__)

##############################################################
# Flask Routes
##############################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Hawaii Climate Page!<br/>"
        f"Available Routes:<br/>"
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"List of Stations: /api/v1.0/stations<br/>"
        f"Temperature Observations: /api/v1.0/tobs<br/>"
        f"Temperature stats from the start date: /api/v1.0/yyyy-mm-dd<br/>"
        f"Temperature stats for given start and end date:/api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a dictionary in JSON format where the date is the key and the value is the precipitation data"""
    # Create session from Python to the DataBase
    session = Session(engine)

    # Calculate the date one year ago from the last data point in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
    last_year = last_date - dt.timedelta(days=365)

    # Query for the dates and precipitation values 
    prcp_results = (
        session.query(Measurement.date, Measurement.prcp)
        .filter(Measurement.date > last_year)
        .order_by(Measurement.date).all())
    
    session.close()
    
    return jsonify(prcp_results)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations"""
    session = Session(engine)

    station_results = session.query(Station.station, Station.name).all()

    session.close()

    return jsonify(station_results)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of temperature observations for the previous year"""
    session = Session(engine)

    # Calculate the date one year ago from the last data point in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
    last_year = last_date - dt.timedelta(days=365)

    temp_results = (
        session.query(Measurement.date, Measurement.tobs)
        .filter(Measurement.date > last_year)
        .order_by(Measurement.date).all())

    session.close()

    return jsonify(temp_results)

@app.route("/api/v1.0/<start>")
def start(start):
    """Returns the JSON list of the minimum, average, and the maximum temperatures for a given start date (YYYY-MM-DD)"""
    session = Session(engine)

    start = dt.datetime.strptime(start, "%Y-%m-%d")

    start_results = (
        session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs))
        .filter(Measurement.date >=start).all())

    session.close()

    tobsall = []
    for min,avg,max in start_results:
        tobs_dict ={}
        tobs_dict["Min"]= min
        tobs_dict["Average"]= avg
        tobs_dict["Max"]= max
        tobsall.append(tobs_dict)
    return jsonify(tobsall)

@app.route("/api/v1.0/<start>/<end>")
def start_stop(start,end):
    """Returns the JSON list of the minimum, average, and the maximum temperatures for a given start date (YYYY-MM-DD)"""
    session = Session(engine)

    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end, "%Y-%m-%d")

    start_end_results = (
        session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs))
        .filter(Measurement.date >=start_date)
        .filter(Measurement.date <= end_date).all())

    session.close()

    tobsall = []
    for min,avg,max in start_end_results:
        tobs_dict ={}
        tobs_dict["Min"]= min
        tobs_dict["Average"]= avg
        tobs_dict["Max"]= max
        tobsall.append(tobs_dict)
    return jsonify(tobsall)   

if __name__== '__main__':
    app.run(debug=True)