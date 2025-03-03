# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
import matplotlib.pyplot as plt
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import risk, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key

def run():
    """Requirements for Task 2G"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations) # update water levels of the stations

    # Only consider the stations with higher relative water level over an threshold
    targets = stations_level_over_threshold(stations, 1.2)

    # Create a list and a dictionary to store towns and their risk levels
    risk_towns = []
    towns = {}
    for station in targets:
        # Find the station in MonitoringStation datatype
        for i in stations:
            if i.name == station[0]:
                target = i
        risk_level = risk(target)
        if risk_level == None:
            continue
        town = target.town
        if town == None: # if the town name is None, use the station name instead
            town = target.name
        if town not in towns.keys():
            towns[town] = risk
        else:
            if towns[town] < risk:
                towns[town] = risk
        
    # Add the dictionary elements into list, and sort the list by risk level
    for item in towns.keys():
        risk_towns.append([item, towns[item]])
    risk_towns = sorted_by_key(risk_towns, 1, reverse = True)

    # Prepare for the output
    for item in risk_towns:
        if item[1] == 5:
            print(str(item[0])+": severe")
        elif item[1] == 4:
            print(str(item[0])+": relatively high")
        elif item[1] == 3:
            print(str(item[0])+": high")
        elif item[1] == 2:
            print(str(item[0])+": moderate")
        elif item[1] == 1:
            print(str(item[0])+": relatively low")
        elif item[1] == 0:
            print(str(item[0])+": low")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
