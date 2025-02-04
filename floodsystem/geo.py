# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""



# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import utils
from stationdata import build_station_list
from haversine import haversine


stations = build_station_list()

def stations_by_distance(stations, p):

    distances = []
    for station in stations:
        distances.append((station.name, haversine(station.coord, p)))
    return utils.sorted_by_key(distances, 1)

print(stations_by_distance(stations, (52.2053, 0.1218))[:10])


