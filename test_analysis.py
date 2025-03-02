"""Unit test for analysis.py file"""
import datetime
import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit

def test_polyfit():

    # Create a list of stations
    stations = build_station_list()
    update_water_levels(stations)

    for x in stations:
        if x.name == "Girton":
            station = x
            break
    # Fetch the data over the past dt(10) days
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    polynomial = polyfit(dates, levels, 4)

    assert len(polynomial) == 2
 
    