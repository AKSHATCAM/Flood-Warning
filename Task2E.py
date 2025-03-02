# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
import matplotlib.pyplot as plt
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirement of Task 2E"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations) # update water levels of the stations

    targets = stations_highest_rel_level(stations, 5)

    for item in targets:
        # Fetch the data over the past dt(10) days
        dt = 10
        dates, levels = fetch_measure_levels(item.measure_id, dt=datetime.timedelta(days=dt))
        # Plot
        plot_water_levels(item, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()