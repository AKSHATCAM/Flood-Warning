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
from floodsystem import utils
from floodsystem.stationdata import build_station_list
from haversine import haversine


stations = build_station_list()

def stations_by_distance(stations, p):

    distances = []
    for station in stations:
        distances.append((station.name, haversine(station.coord, p)))
    return utils.sorted_by_key(distances, 1)

stations_list_final = stations_by_distance(stations, (52.2053, 0.1218))

def stations_within_radius(stations, centre, r):
    stations_within = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            stations_within.append(station.name)
    return stations_within

def



