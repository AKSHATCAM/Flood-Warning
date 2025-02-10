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

def rivers_with_station(stations):
    """This is for Task 1D, implement a function that returns a list with the names of the rivers with a monitoring station, 
    in alphabetical order"""
    rivers_0 = set()
    for station in stations:
        rivers_0.add(station.river)
    rivers = list(rivers_0)
    rivers.sort()
    return rivers

def stations_by_river(stations):
    rivers = {}
    for station in stations:
        if station.river in rivers.keys():
            rivers[station.river] += [station]
        elif station.river == None:
            continue
        else:
            rivers[station.river]=[station]
    return rivers





