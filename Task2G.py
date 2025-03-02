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
    stations = stations_level_over_threshold(stations, 1.2)