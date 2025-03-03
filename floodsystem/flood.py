
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime 
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from .utils import sorted_by_key 
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit



def stations_level_over_threshold(stations, tol):
    full_list = []
    for station in stations:
        level = station.relative_water_level()
        if station.typical_range_consistent() and level is not None:
            if level > tol:
                full_list.append((station, level))
    
    # Sort the list in descending order based on water level
    full_list.sort(key=lambda x: x[1], reverse=True)
    
    return full_list

    
def stations_highest_rel_level(stations, N):
    full_list = []
    for station in stations:
        level = station.relative_water_level()
        if station.typical_range_consistent() and level is not None:
            full_list.append((station, level))

    full_list.sort(key=lambda x: x[1], reverse=True)
    station_list = [num[0] for num in full_list]
    return station_list[:N]

def risk(station):
    """
    The function takes a station as an input, and then returns an integer between 0 to 5 to indicate
    the risk level of the monitoring station.
    0 represents low risk level, 5 represents high risk level.
    """

    # Get the relative water level for the input station
    rel_level = station.relative_water_level()
    
    # Deal with empty data value
    if station.typical_range_consistent() == False or (station.latest_level == None):
        return None
    
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=1))

    if len(levels) == 0:
        return None
    
    # Fit the function
    float_dates = matplotlib.dates.date2num(dates)
    try: 
        result = polyfit(dates, levels, 4)
        func = result[0]
        shift = result[1]
        derivatve = func.deriv()
        gradient = derivatve(float_dates[-1] - shift)
    except:
        return None
    
    # Assess the risk level
    risk = 0

    if rel_level > 3:
        risk = 5
    elif rel_level > 2.5:
        risk = 4
    elif rel_level > 2:
        risk = 3
    elif rel_level > 1.5:
        risk = 2
    elif rel_level > 1:
        risk = 1
    else:
        risk = 0
    
    if gradient >= 0.3:
        risk += 1
    elif gradient <= -0.3:
        risk -= 1
    
    # Normalise the risk level in to range of 0 to 5
    if risk > 5:
        risk = 5
    elif risk < 0:
        risk = 0

    return risk
    

    



